from django.shortcuts import render, redirect


def mostrarProductosPlantilla(request):
    # request > toda la informacion desde el navegador
    print(request)
    data = [
        {
            'id': 1,
            'nombre': 'Lapiz Faber Castell',
            'descripcion': 'Lapiz B2'
        },
        {
            'id': 2,
            'nombre': 'Resaltador color amarillo',
            'descripcion': None
        }
    ]
    # podemos retornar un html para cuestiones en que la aplicacion sea un monolito
    return render(request, 'mostrar_productos.html', {'data': data, 'mensaje': 'Bienvenido!'})


def crearProductosFormulario(request):
    if request.method == 'POST':
        # Para recibir la informacion proveniente del formulario en base a sus name
        # print(request.POST.get('descripcionProducto'))
        print(request.POST)
        print('Quieren crear un producto')
        # como en teoria ya se agrego mi producto en la base de datos entonces mandare un redireccionamiento a la vista de listar los productos
        return redirect('mostrar_productos')
    elif request.method == 'GET':
        return render(request, 'formulario_producto.html')