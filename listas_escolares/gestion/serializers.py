from rest_framework.serializers import ModelSerializer
from .models import Producto


# Hay dos formas de crear serializadores, la primera seria sin un modelo desde 0 como haciamos con marshmallow y la segunda utilizando un modelo
class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        # Ahora, a diferencia de marshmallo tenemos que indicar que atributos vamos a utilizar del modelo
        # fields = ['id', 'nombre']
        # Si queremos utilizar todos los atributos
        fields = '__all__'
        # Otra forma de definir los atributos a utilizar seria
        # exclude = ['id', 'descripcion']
        # NOTA: no se puede utilizar los dos a la vez, es decir, o se usa el fields o se usa el exclude
