from json import loads
from bcrypt import gensalt, hashpw
from controllers.serializers import ValidarTokenSerializer, ResetPasswordSerializer
from cryptography.fernet import InvalidToken
from marshmallow.exceptions import ValidationError
from flask import request
from instancias import encriptador
from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import *
from controllers import *
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

# origins > los dominios que pueden acceder a mi backend
# methods > metodos HTTP que pueden consultar a mi backend
# allow_headers > los headers permitidos que pueden enviar a mi backend
# si quiero permitir todos los valores permitidos ya sea en los origins, methods, headers colocamos el '*'
CORS(app,
     origins=['http://127.0.0.1:5500', 'http://localhost:5500'],
     methods=['GET', 'PUT', 'POST', 'DELETE'],
     allow_headers='*')

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL_PRINCIPAL')

# Aca agregamos las otras conexiones a otras bases de datos secundarias
app.config['SQLALCHEMY_BINDS'] = {
    'mysql': environ.get('DATABASE_URL_MYSQL')
}
# cuando utilizamos la libreria de JWT tenemos que definir las configuraciones en nuestra variable
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
# Con esto podemos modificar cuanto tiempo durara la token, no se recomienda colocar False para evitar problemas de seguridad
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(
    hours=3, minutes=5, seconds=10)

JWTManager(app)
conexion.init_app(app)

Migrate(app, conexion)

api = Api(app)


@app.route('/validar-token', methods=['POST'])
def validarToken():
    data = request.get_json()

    serializador = ValidarTokenSerializer()
    try:
        data_serializada = serializador.load(data)
        informacion = encriptador.decrypt(data_serializada.get('token'))
        print(informacion)

        return {
            'message': 'Token validada exitosamente'
        }

    except InvalidToken as error:
        return {
            'message': 'Error al validar la token, la token es incorrecta',
            'args': error.args
        }

    except ValidationError as error:
        return {
            'message': 'Error al validar la token',
            'content': error.args
        }, 400


@app.route('/reset-password', methods=['POST'])
def resetPassword():
    data = request.get_json()
    try:
        serializador = ResetPasswordSerializer()
        data_serializada = serializador.load(data)
        informacion = encriptador.decrypt(
            data_serializada.get('token')).decode('utf-8')

        informacion_diccionario = loads(informacion.replace("'", '"'))

        usuario_id = informacion_diccionario.get('usuario_id')
        usuario_encontrado = conexion.session.query(
            Usuario).filter(Usuario.id == usuario_id).first()
        if usuario_encontrado is None:
            return {
                'message': 'Usuario no existe'
            }, 404

        salt = gensalt()
        # Generamos el hash de la nueva password
        password_hasheada = hashpw(bytes(data_serializada.get(
            'password'), 'utf-8'), salt).decode('utf-8')

        # Actualizamos el registro del usuario encontrado con su nueva password
        usuario_encontrado.password = password_hasheada
        # Guardamos los cambios de manera permanente en la base de datos
        conexion.session.commit()

        return {
            'message': 'Password modificada exitosamente'
        }

    except ValidationError as error:
        return {
            'message': 'Error al resetear la password',
            'content': error.args
        }, 400
    except InvalidToken as error:
        return {
            'message': 'Error al resetear la password',
            'content': 'Token invalida'
        }, 400


api.add_resource(CategoriasController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(UsuarioController, '/usuario')
api.add_resource(CategoriaController, '/categoria/<int:id>')
api.add_resource(OlvidePasswordController, '/forgot-password')

if __name__ == '__main__':
    app.run(debug=True)
