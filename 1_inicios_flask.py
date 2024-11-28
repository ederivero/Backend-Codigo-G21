from flask import Flask, request
from psycopg import connect

# __name__ > propia de python que sirve para indicar si el archivo en el cual nos encontramos es el archivo principal (el que se esta ejecutando por la terminal). si es el archivo principal su valor sera '__main__', caso contrario tendra otro valor la variable
app = Flask(__name__)
# Flask solamente puede tener una instancia en todo el proyecto y esa instancia debe de estar en el archivo principal, sino no podra ejecutarse la instancia de la clase


# Para conectarse a la bd:
# Formato standar para las conexion a las bd
# DIALECTO://USUARIO:PASSWORD@HOST:PUERTO/DATABASE_NAME
conexion = connect(
    conninfo='postgresql://postgres:root@localhost:5432/finanzas')


# Mediante el uso de decoradores podemos indicar la ruta y cual sera su comportamiento
# Un decorador sirve para poder reusar un metodo de una clase pero sin la necesidad de editarlo como tal, solamente se modificar el funcionamiento para, en este caso, la ruta configurada


@app.route('/')
def inicio():
    return 'Bienvenido a mi aplicacion de Flask!'


@app.route('/inicio', methods=['POST'])
def inicio_aplicacion():
    return {
        'message': 'Buenas noches, acabas de descubrir otro endpoint'
    }


# Si queremos recibir un parametro por la url que sea dinamico, este parametro tiene que estar entre < >, adicional a ello se puede indicar el tipo de dato (int, string)
@app.route('/usuarios/<int:id>', methods=['GET', 'POST'])
def mostrar_usuario(id):
    # cuando ponemos un parametro dinamico entonces ese parametro tiene que ser registrado con el mismo nombre como parametro de la funcion
    print(id)
    return {
        'message': f'El usuario es {id}'
    }


@app.route('/gestionar-usuario/<int:id>', methods=['POST', 'PUT', 'DELETE'])
def gestionar_usuario(id):
    # para poner manejar la informacion de la peticion se usar el metodo request de flask
    if request.method == 'POST':
        return {
            'message': 'La creacion del usuario fue exitosa'
        }
    elif request.method == 'PUT':
        return {
            'message': 'Usuario actualizado exitosamente'
        }
    elif request.method == 'DELETE':
        return {
            'message': 'Usuario eliminado exitosamente'
        }


@app.route('/listar-clientes', methods=['GET'])
def listar_clientes():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    # Para obtener la informacion proveniente del select
    # fetchall() > devuelve todos los registros del select
    # fetchmany(limite) > devuelve los registros hasta el limite
    # fetchone() > devuelve el primer registro del select
    data = cursor.fetchall()

    print(data)
    return {
        'message': 'Los clientes son'
    }


# Todo la funcionabilidad de nuestro servidor tiene que ir antes del metodo .run
# levanta el servidor de Flask con algunos parametros opcionales
# debug > si su valor es True entonces cada vez que modifiquemos el servidor y guardemos este se reiniciara automaticamente
app.run(debug=True)
