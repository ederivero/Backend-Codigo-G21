from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL_PRINCIPAL')

# Aca agregamos las otras conexiones a otras bases de datos secundarias
app.config['SQLALCHEMY_BINDS'] = {
    'mysql': environ.get('DATABASE_URL_MYSQL')
}

conexion.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
