from flask_restful import Resource, request
from models import CategoriaModel
from instancias import conexion
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError


# Al heredar la clase Resource, ahora los metodos de la clase tendran que tener el nombre de los metodos http para que sean llamados correctamente
class CategoriaController(Resource):
    def get(self):
        # SELECT * FROM categorias;
        data = conexion.session.query(CategoriaModel).all()
        # convertir esta informacion de instancias a un diccionario para devolverlo usando marshmallow
        serializador = CategoriaSerializer()
        resultado = serializador.dump(data, many=True)
        return {
            'message': 'Las categorias son',
            'result': resultado
        }

    def post(self):
        # Obtenemos la informacion del body proveniente del request
        data = request.get_json()
        serilizador = CategoriaSerializer()
        try:
            # Carga la informacion y la validara con el serializador, si falla, emitira un error
            data_serializada = serilizador.load(data)

            # Cargo la informacion serializa a la nueva instancia de la categoria
            # CategoriaModel(nombre=data_serializada.get('nombre'),
            #                fechaCreacion=data_serializada.get('fechaCreacion'), ...)

            # Cuando yo quiero pasar un diccionario a parametros de una clase o funcion CON LOS MISMO NOMBRES de los parametros que las llaves del diccionario
            # data_serializada = {'nombre':'xyz', 'fechaCreacion':'2022-12-01'}
            # CategoriaModel(nombre='xyz, fechaCreacion='2022-12-01')
            nueva_categoria = CategoriaModel(**data_serializada)

            # Agregamos el nuevo registro a nuestra bd
            conexion.session.add(nueva_categoria)

            # Indicamos que los cambios deben de guardarse de manera permanente (usando una transaccion)
            conexion.session.commit()

            # Ahora convertimos la instancia a un diccionario para devolverla
            resultado = serilizador.dump(nueva_categoria)
            return {
                'message': 'Categoria creada exitosamente',
                'content': resultado
            }
        except ValidationError as error:
            return {
                'message': 'Error al crear la Categoria',
                'content': error.args  # muestra la descripcion del error
            }
