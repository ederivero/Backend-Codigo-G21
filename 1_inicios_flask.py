from flask import Flask

# __name__ > propia de python que sirve para indicar si el archivo en el cual nos encontramos es el archivo principal (el que se esta ejecutando por la terminal). si es el archivo principal su valor sera '__main__', caso contrario tendra otro valor la variable
app = Flask(__name__)
# Flask solamente puede tener una instancia en todo el proyecto y esa instancia debe de estar en el archivo principal, sino no podra ejecutarse la instancia de la clase

# levanta el servidor de Flask con algunos parametros opcionales
# debug > si su valor es True entonces cada vez que modifiquemos el servidor y guardemos este se reiniciara automaticamente
app.run(debug=True)
