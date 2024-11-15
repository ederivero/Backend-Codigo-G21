# snake_case
nombre_completo = 'Eduardo de Rivero Manrique'

# camelCase
nombreCompleto = 'Eduardo de Rivero Manrique'

# PascalCase
NombreCompleto = 'Eduardo de Rivero Manrique'

# Los nombres de las variables no pueden contener caracteres especiales '-' '@' '/' y simbolos
# nombre@completo = 'eduardo de rivero'

# Tampoco pueden empezar con numeros
nombre1 = 'Eduardo'
n1ombre = 'Juan'
# 1nombre = 'Roberto'


# Al hacer sumas de strings esto se hara una concatenacion
# Solamente la suma puede ser entre strings O int O float mas no combinarlos
resultado = 'Fabiola' + 'Roberta'

print(resultado)


# Nosotros podemos acceder a los strings en base a sus posiciones
nombre = 'Pedrito'
print(nombre[3])

# solamente se puede visualizar el texto en sus posiciones MAS NO modificarlos
# inmutables (no se puede mutar o modificar)
# nombre[6] = 'a'

# para saber la longitud del texto
longitud = len(nombre)
print(longitud)

# se puede sacar un sub string o una sub-cadena
texto = 'El dia de hoy me levante y fui a marchar por mi pais y de ahi me comi un pan con pejerrey'

sub_texto = texto[3:17]

print(sub_texto)
# Empieza desde el inicio hasta la posicion <17
sub_texto = texto[:17]
print(sub_texto)


sub_texto = texto[23:]
print(sub_texto)

# si colocamos [:] haremos una copia del contenido de la variable texto
sub_texto = texto[:]
sub_texto = texto
print(sub_texto)


# NUMERICOS
resultado = 10 + 3.75
# forma para poder hacer mas leible un numero grande con la adherencia de '_', esto sirve solamente para lectura
# esta ayuda esta disponible desde la version 3.6 de python en adelante
numerazo = 1_010_101_010
print(resultado)

print(numerazo)

resultado = 10/9

# Limitar el numero de decimales de una division con redondeo
print("{:.4f}".format(resultado))


# otra forma de declara variables
numero1, numero2, numero3, numero4 = 3, 'Arequipa', True, 4.5
print(numero1)
print(numero2)

# BOOLEAN
libre = True
# En python para utilizar el operador '!' se tiene que utilizar el operador 'not'
print(not libre)
