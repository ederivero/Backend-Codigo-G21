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


# Cuando queremos trabajar en otra ruta o utilizar otra vez un metodo ya creado
# Cuando ponemos en un metodo http un parametro significa que vamos a recibir ese parametro por la url
# /endpoint/<id>
class ManejoCategoriaController(Resource):
    def validarCategoria(self, id):
        # filter > hace la comparacion entre los atributos de la clase
        # filter_by > hace la comparacion entre PARAMETROS mas no utiliza atributos, SOLO SIRVE PARA HACER BUSQUEDAS IGUAL QUE
        # el filter es mejor porque nos permite hacer busquedas mas avanzadas como LIKE, ILIKE, mayor que, menor que, etc

        # SELECT * FROM categorias WHERE id = '...' LIMIT 1;
        categoria_encontrada = conexion.session.query(CategoriaModel).filter(
            CategoriaModel.id == int(id)).first()

        # Operador ternario
        # RESULTADO_CONDICION_VERDADERA if CONDICION else RESULTADO_CONDICION_FALSA
        return {'message': 'Categoria no existe'} if categoria_encontrada is None else categoria_encontrada

    def get(self, id):
        categoria_encontrada = self.validarCategoria(id)

        # si el tipo de dato que retorna el metodo validarCategoria es un dict entonces vamos a retornar ese contenido, caso contrario procedemos
        # type > podemos validar el tipo de dato de la variable y usarlo para condicionales
        if type(categoria_encontrada) == dict:
            return categoria_encontrada

        serializador = CategoriaSerializer()
        resultado = serializador.dump(categoria_encontrada)

        return {
            'content': resultado
        }

    def put(self, id):
        categoria_encontrada = self.validarCategoria(id)

        # si el tipo de dato que retorna el metodo validarCategoria es un dict entonces vamos a retornar ese contenido, caso contrario procedemos
        # type > podemos validar el tipo de dato de la variable y usarlo para condicionales
        if type(categoria_encontrada) == dict:
            return categoria_encontrada

        data = request.get_json()
        serializador = CategoriaSerializer()
        try:
            data_validada = serializador.load(data)
            # hacemos las modificaciones de los valores del registro
            categoria_encontrada.nombre = data_validada.get('nombre')
            # si me esta enviando la disponibilidad la cambiare, caso contrario, usare la que tengo actualmente almacenada en la bd
            # is not None> la condicion sera verdadera si el contenido de la variable no es None, osea puede ser Falso , 0 u otro valor
            categoria_encontrada.disponibilidad = data_validada.get('disponibilidad') if data_validada.get(
                'disponibilidad') is not None else categoria_encontrada.disponibilidad

            # procedemos con la actualizacion
            conexion.session.commit()

            # transformamos la informacion para ser retornada
            resultado = serializador.dump(categoria_encontrada)

            return {
                'message': 'Categoria actualizada exitosamente',
                'content': resultado
            }
        except ValidationError as error:
            return {
                'message': 'Error al actualizar la categoria',
                'content': error.args
            }

    def delete(self, id):
        categoria_encontrada = self.validarCategoria(id)

        # si el tipo de dato que retorna el metodo validarCategoria es un dict entonces vamos a retornar ese contenido, caso contrario procedemos
        # type > podemos validar el tipo de dato de la variable y usarlo para condicionales
        if type(categoria_encontrada) == dict:
            return categoria_encontrada

        # eliminamos el registro de la bd
        conexion.session.delete(categoria_encontrada)

        # para que sea de manera permanente
        conexion.session.commit()

        return {
            'message': 'Categoria eliminada exitosamente'
        }
