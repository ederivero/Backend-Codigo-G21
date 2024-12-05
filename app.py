from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv

# revisara si hay algun archivo llamado .env y leera las variables definidas en el y las colocara como variables de entorno
load_dotenv()

app = Flask(__name__)
# Si vamos a tener mas de una conexion a diferente base de datos, entonces debemos utilizar la variable SQLALCHEMY_BINDS
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
print(environ.get('DATABASE_URL'))
app.config['SQLALCHEMY_BINDS'] = {
    'postgres': environ.get('DATABASE_URL'),
    # 'mysql': ''
}


# asi se puede inicializar la conexion a la base de datos desde otro archivo
conexion.init_app(app)
# al momento de crear nuestro modelo (tabla) usaremos la variable __bind_key__ para indicar a que base de datos queremos utilizar
# class UsuarioPostgresModel(conexion.Model):
#     __bind_key__='postgres'
#     id = Column(type_=types.Integer)

if __name__ == '__main__':
    app.run(debug=True)
