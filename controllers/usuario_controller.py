from flask_restful import Resource, request
from models import Usuario
from instancias import conexion
from .serializers import RegistroSerializer, LoginSerializer, ActualizarUsuarioSerializer
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class RegistroController(Resource):
    def post(self):
        data = request.get_json()

        serializador = RegistroSerializer()
        try:
            data_serializada = serializador.load(data)
            # Generar el hash de la password para guardarla en la bd
            salt = gensalt()
            password_hashed = hashpw(
                bytes(data_serializada.get('password'), 'utf-8'), salt).decode('utf-8')

            # ahora reemplazamos el valor de la password con el hasheo de la password
            data_serializada['password'] = password_hashed

            nuevo_usuario = Usuario(**data_serializada)
            conexion.session.add(nuevo_usuario)
            conexion.session.commit()

            return {
                'message': 'Usuario registrado exitosamente',
                'content': serializador.dump(nuevo_usuario)
            }

        except ValidationError as error:
            return {
                'message': 'Error al registrar el usuario',
                'content': error.args
            }


class LoginController(Resource):
    def post(self):
        data = request.get_json()
        serializador = LoginSerializer()
        try:
            data_serializada = serializador.load(data)
            # Buscamos si el usuario existe en la bd
            usuario_encontrado = conexion.session.query(Usuario).filter(
                Usuario.correo == data_serializada.get('correo')).first()
            if usuario_encontrado is None:
                return {
                    'message': 'El usuario no existe'
                }

            password_en_bytes = bytes(
                data_serializada.get('password'), 'utf-8')
            password_bd_en_bytes = bytes(usuario_encontrado.password, 'utf-8')

            # el checkpw contrastara la password guardada en la bd con la password enviada en el login y si es, retornara True, caso contrario, False
            resultado = checkpw(password_en_bytes, password_bd_en_bytes)

            if resultado == True:
                # identity > es el identificador para reconocer a que usuario le pertenece esa token
                # el identificador de la token siempre debe de ser un string
                token = create_access_token(
                    identity=str(usuario_encontrado.id))
                return {
                    'message': 'Bienvenido',
                    'token': token
                }
            else:
                return {
                    'message': 'Credenciales incorrectas'
                }
        except ValidationError as error:
            return {
                'message': 'Error al hacer el login',
                'content': error.args
            }


class UsuarioController(Resource):
    # Este metodo get sera una ruta PROTEGIDA, es decir se necesitara una token de acceso para poder ingresar al controlador, caso contrario sera rechazada la peticion
    @jwt_required()
    def get(self):
        identificador = get_jwt_identity()
        print(identificador)
        # BUSCAR EL USUARIO EN LA BD SEGUN EL IDENTIFICADOR
        usuario_encontrado = conexion.session.query(
            Usuario).filter(Usuario.id == identificador).first()

        if usuario_encontrado is None:
            return {
                'message': 'El usuario no existe'
            }
        serializador = RegistroSerializer()

        resultado = serializador.dump(usuario_encontrado)

        return {
            'content': resultado  # RETORNAR EL USUARIO
        }

    @jwt_required()
    def put(self):
        # Actualizar el usuario
        identificador = get_jwt_identity()

        usuario_encontrado = conexion.session.query(
            Usuario).filter(Usuario.id == identificador).first()

        if usuario_encontrado is None:
            return {
                'message': 'El usuario no existe'
            }

        serializador = ActualizarUsuarioSerializer()
        try:
            data_serializada = serializador.load(request.get_json())
            # Si el valor es un string vacio no modificara la informacion, asi lo maneja python e ingresaremos al else
            usuario_encontrado.nombre = data_serializada.get(
                'nombre') if data_serializada.get('nombre') else usuario_encontrado.nombre

            usuario_encontrado.apellido = data_serializada.get(
                'apellido') if data_serializada.get('apellido') else usuario_encontrado.apellido

            if data_serializada.get('password'):
                salt = gensalt()
                password_en_bytes = bytes(
                    data_serializada.get('password'), 'utf-8')

                password_hasheada = hashpw(
                    password_en_bytes, salt).decode('utf-8')

                usuario_encontrado.password = password_hasheada

            conexion.session.commit()

            return {
                'message': 'Usuario actualizado exitosamente'
            }

            # Si se hace el cambio de la password entonces tenemos que generar su hash antes de guardarlo en la bd
        except ValidationError as error:
            return {
                'message': 'Error al actualizar el usuario',
                'content': error.args
            }
