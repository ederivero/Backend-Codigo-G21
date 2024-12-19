from flask_restful import Resource, request
from instancias import conexion
from models import Categoria
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required


class CategoriasController(Resource):
    # atributo de la clase
    serializador = CategoriaSerializer()

    @jwt_required()
    def post(self):
        # validamos que el usuario sea admin para poder crear la categoria
        # ...
        data = request.get_json()
        try:
            data_serializada = self.serializador.load(data)
            # { 'nombre': 'blabla', 'color': 'azul' }
            # nombre = 'blabla', color = 'azul'
            nueva_categoria = Categoria(**data_serializada)
            conexion.session.add(nueva_categoria)
            conexion.session.commit()

            resultado = self.serializador.dump(nueva_categoria)

            return {
                'message': 'Categoria creada exitosamente',
                'content': resultado
            }
        except ValidationError as error:
            return {
                'message': 'Error al crear la categoria',
                'content': error.args
            }

    def get(self):
        # SELECT * FROM categorias;
        categorias = conexion.session.query(Categoria).all()

        return {
            'content': self.serializador.dump(categorias, many=True)
        }
