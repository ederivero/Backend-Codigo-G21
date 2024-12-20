from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Libro


class LibroSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Libro
