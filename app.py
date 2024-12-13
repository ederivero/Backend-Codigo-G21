from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import *
from controllers import *
from flask_restful import Api

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL_PRINCIPAL')

# Aca agregamos las otras conexiones a otras bases de datos secundarias
app.config['SQLALCHEMY_BINDS'] = {
    'mysql': environ.get('DATABASE_URL_MYSQL')
}

conexion.init_app(app)

Migrate(app, conexion)

api = Api(app)

api.add_resource(CategoriasController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)
