from flask_restful import Resource, request
from models import Usuario
from instancias import conexion
from .serializers import RegistroSerializer
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw


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
