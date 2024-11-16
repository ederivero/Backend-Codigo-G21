# Listas (Arreglos o Arrays)
# Ordenada y editable
frutas = ['Manzana', 'Platano', 'Papaya', 'Pitahaya']

# Ordenado > Cada elemento de la lista esta en una POSICION determinada
print(frutas[1])
# Editable > agregar y eliminar elementos de la lista
frutas.append('Mandarina')
frutas.append('Piña')

print(len(frutas))

frutas.remove('Platano')
print(frutas)
# el metodo remove solamente si existe ese elemento lo eliminara, sino, lanzara un error
# frutas.remove('Aguaymanto')

# el metodo pop funciona con la POSICION de la fruta
frutas.pop(0)
print(frutas)

# Reemplazando el valor antiguo por un nuevo valor
frutas[0] = 'Kiwi'
print(frutas)

# Colocando como primer paramero el indice donde se agregara el nuevo contenido y como segundo parametro el contenido a agregar
frutas.insert(2, 'Uva')

print(frutas)
usuario = ['Eduardo', 'de Rivero',
           'ederiveroman@gmail.com', '1992/08/01', False, 1.50, ['Nadar', 'Programar', 'Montar bici']]


# Tuplas
# No son EDITABLES! Una vez creada ya no pueden modificar
# Son Ordenadas
alumnos = ('Farit', 'Francesca', 'Cesar', 'Cristhian', 'Eddy')

print(alumnos[0])

# Otra forma de crear una lista en base a una tupla PERO la tupla original sigue siendo una tupla que no se puede editar
copia_alumnos = list(alumnos)

print(id(alumnos))
print(id(alumnos))
print(id(copia_alumnos))
copia_alumnos[0] = 'Brigit'
print(copia_alumnos)

segunda_copia = tuple(copia_alumnos)
print(id(segunda_copia))
# segunda_copia[0] = 'Pedro'


# cuando copiamos una lista a otra variable lo que estamos en realidad es utilizar la misma posicion de memoria
# ahora hago una copia del contenido y esto indica que se guarde en otra posicion de memoria
otras_frutas = frutas[:]
print(id(otras_frutas))
print(id(frutas))

print(otras_frutas)

frutas[1] = 'Fruta del dragon'
print(otras_frutas)


# Set (Conjunto)
# Es DESORDENADA
# Es EDITABLE
inventario = {
    'Monitores',
    'Mouse',
    'Proyectores',
    'Ventiladores',
    'Teclados'
}

print(inventario)
# No se puede realizar porque no es una coleccion de datos ordenada
# print(inventario[0])
inventario.add('Memoria RAM')
inventario.remove('Mouse')
print(inventario)

print('Monitores' in inventario)
print('Laptops' in inventario)


# DICTIONARY - DICCIONARIOS
# Ordenado PERO POR LLAVES no por posicion ni indices
# Editable

persona = {
    'nombre': 'Eduardo',
    'apellido': 'de Rivero',
    'correo': 'ederivero@gmail.com',
    'hobbies': ['Comer', 'Programar', 'Montar bici'],
    'direcciones': {
        'calle': 'Calle los geranios',
        'numero': 870,
        'postal': '04010'
    },
    'viudo': False,
    'familiares': ('Juanito Perez', 'Maria Aguilar', 'Roxana Washington')
}
