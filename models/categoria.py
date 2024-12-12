from instancias import conexion
from sqlalchemy import Column, types


class Categoria(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False, unique=True)
    color = Column(type_=types.Text)

    __tablename__ = 'categorias'
