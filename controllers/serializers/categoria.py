from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Categoria
from marshmallow import fields
from .libro_serializer import LibroSerializer


class CategoriaSerializer(SQLAlchemyAutoSchema):
    # si utilizamos un atributo que no esta debidamente identificado en el modelo, entonces tenemos que utilizar el parametro attribute
    librosDeLaCategoria = fields.Nested(
        LibroSerializer, many=True, attribute='libros')
    # si utilizamos un atributo que ya esta siendo utilizado por otro elemento, lanzara un error, entonces debemos de quitarlo

    class Meta:
        model = Categoria
        # si queremos que este serializador incluya las relaciones
        # include_relationships = True
