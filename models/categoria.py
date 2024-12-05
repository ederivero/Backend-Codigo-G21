from instancias import conexion
from sqlalchemy import Column, types
from datetime import datetime


# naming de variables
# CamelCase los nombre empiezan con mayus y si en el nombre tuviesemos dos palabras o mas palabras, el inicio de la palabra empieza con mayus
# snake_case cada palabra esta dividida con un '_'
# pascalCase empieza con minus y si tenemos otra palabra esa empezara con mayus
class CategoriaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True,
                primary_key=True, nullable=False)

    nombre = Column(type_=types.Text, nullable=False)

    fechaCreacion = Column(name='fecha_creacion',
                           type_=types.TIMESTAMP, default=datetime.now)

    disponibilidad = Column(type_=types.Boolean, default=True)

    __tablename__ = 'categorias'
    # si en nuestra instancia de sqlalchemy estamos usando mas de un conector, entonces debemos en cada tabla que usemos indicar a que conexion nos referiremos, esto servira para cuestiones de creacion de tabla y para la lectura y modificacion de datos
    __bind_key__ = 'postgres'
