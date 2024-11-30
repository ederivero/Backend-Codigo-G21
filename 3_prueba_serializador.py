from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError


class UsuarioSchema(Schema):
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    correo = fields.Email()
    sexo = fields.Str(required=False)


usuario1 = {'nombre': 'Eduardo',
            'apellido': 'Martinez',
            'correo': 'emartinez@gmail.com'
            }

usuario2 = {'nombre': 'Roxana',
            'correo': 'emartinez@gmail.com',
            'sexo': 'F'
            }

validarUsuario = UsuarioSchema()

# load > validara la informacion que le estamos pasadon con las propiedades del serializador y si alguna de las propiedades falta o no cumple entonces emitira un error
# por lo general se usa con un try-except
try:
    resultado = validarUsuario.load(usuario1)

    print(resultado)
except ValidationError as error:
    # en todo error emitido para obtener el mensaje del error usamos el atributo args
    print(error.args)

try:
    resultado2 = validarUsuario.load(usuario2)
    print(resultado2)
except ValidationError as error:
    print(error.args)


class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo


nuevoUsuario = Usuario(
    nombre='Juancito',
    apellido='Gil',
    correo='jgil@gmail.com'
)

# dump > sirve para convertir informacion compleja como instancia de clases u otros a un diccionario simple
resultado3 = validarUsuario.dump(nuevoUsuario)
print(resultado3)
