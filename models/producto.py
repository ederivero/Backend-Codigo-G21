from instancias import conexion
from sqlalchemy import Column, types, ForeignKey


# https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column
class ProductoModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text)
    precio = Column(type_=types.Float, nullable=False)
    disponibilidad = Column(type_=types.Boolean, default=True)

    # RELACIONES
    # En este caso estariamos utilizando una relacion de 1 a n
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         type_=types.Integer, nullable=False)

    __tablename__ = 'productos'
    __bind_key__ = 'postgres'
