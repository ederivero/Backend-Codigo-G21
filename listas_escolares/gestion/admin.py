from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    # los campos que voy a mostrar de mi tabla producto
    list_display = ['nombre']

    # los campos con los que voy a poder trabajar ya sea para crear, leer y actualizar
    fields = ['nombre', 'descripcion']


# Aca indico que modelos de esta aplicacion puedo gestionar en el panel administrativo
admin.site.register(Producto, ProductoAdmin)
