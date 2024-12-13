from flask_restful import Resource, request
from models import Usuario
from instancias import conexion
from .serializers import RegistroSerializer, LoginSerializer
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw, checkpw


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
                return {
                    'message': 'Bienvenido'
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
