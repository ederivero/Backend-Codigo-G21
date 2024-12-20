from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from os import environ
from dotenv import load_dotenv

load_dotenv()

conexion = SQLAlchemy()
encriptador = Fernet(environ.get('ENCRIPTADOR_KEY'))
