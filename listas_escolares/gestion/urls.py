from django.urls import path
from .views import (mostrarProductosPlantilla,
                    crearProductosFormulario,
                    validarFuncionamiento,
                    ProductosController,
                    ListarYCrearProductosController,
                    DevolverActualizarEliminarProductoController)

# para definir las rutas que van a comportarse en esta aplicacion usamos la variable urlpatterns
urlpatterns = [
    # si estamos trabajando con redireccionamiento en las plantillas podemos agregar a las rutas un nombre para que estas puedan ser llamadas sin importar su endpoint
    path('mostrar-productos', mostrarProductosPlantilla, name='mostrar_productos'),
    path('crear-producto', crearProductosFormulario, name='crear_producto'),
    # no se recomienda definir un name porque no se hara un redireccionamiento hacia esta ruta al ser una API REST
    path('validar-funcionamiento', validarFuncionamiento),
    # Al momento de usar una clase de DRF tenemos que indicar que vamos a convertirla a una vista para que pueda poder entenderla django
    path('productos', ProductosController.as_view()),
    path('productos-v2', ListarYCrearProductosController.as_view()),
    # Cuando usamos alguna de las vistas genericas que devuelvan, actualicen o eliminen un registro en la ruta tenemos que agregar el `pk`
    # Solamente aceptara el pk, si colocamos otro nombre, lanzara un error y por ende no podremos realizar la accion
    # Si queremos cambiar el nombre debemos establecerlo en el atributo lookup_field
    path('producto/<id>', DevolverActualizarEliminarProductoController.as_view())
]
