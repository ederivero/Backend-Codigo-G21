from flask_restful import Resource, request
from models import ProductoModel
from marshmallow.exceptions import ValidationError
from .serializers import ProductoSerializer
from instancias import conexion


class ProductosController(Resource):
    def post(self):
        data = request.get_json()
        serializador = ProductoSerializer()
        try:
            data_validada = serializador.load(data)
            # TODO: Antes de guardar el producto validar que exista la categoria, si es que se le pasa, porque tbn puede haber productos sin categoria
            nuevo_producto = ProductoModel(**data_validada)

            conexion.session.add(nuevo_producto)
            conexion.session.commit()

            resultado = serializador.dump(nuevo_producto)

            return {
                'content': resultado,
                'message': 'Producto creado exitosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
