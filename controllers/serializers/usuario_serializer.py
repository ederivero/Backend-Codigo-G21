from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import Usuario, TipoUsuario
from marshmallow_enum import EnumField
from marshmallow import Schema, fields


class RegistroSerializer(SQLAlchemyAutoSchema):
    # si quiero modificar alguna columna del modelo para cuestiones del serializador
    # ahora modificamos la columna password y le indicamos que tiene que ser requerida a la hora de serializar
    # https://marshmallow-sqlalchemy.readthedocs.io/en/stable/api_reference.html#marshmallow_sqlalchemy.auto_field
    # https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Field
    # load_only > la propiedad solo se usara para cargarla a la bd
    # dump_only > la propieda se usara para devolver y convertirla en el diccionario
    password = auto_field(required=True, load_only=True)
    # modificar el comportamiento de la columna que sea enum en la cual se le coloca que enum debe utilizar para hacer las validaciones correspondientes
    tipoUsuario = EnumField(TipoUsuario)

    class Meta:
        model = Usuario


# Este es un serializador MANUAL que no seguira ningun modelo de ejemplo
class LoginSerializer(Schema):
    correo = fields.Email(required=True)
    password = fields.String(required=True)
