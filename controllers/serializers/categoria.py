from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Categoria


class CategoriaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
