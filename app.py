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

load_dotenv()

app = Flask(__name__)

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

api.add_resource(CategoriasController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(UsuarioController, '/usuario')
api.add_resource(CategoriaController, '/categoria/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
