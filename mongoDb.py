# En la sección de requerimientos puede instalar las librerías necesarias con el comando pip install -r requirements

import pymongo
from pymongo import MongoClient


CONNECTION_STRING = "mongodb://localhost:27017" # esto depende de lo que mongocompass genere como conexión
client = MongoClient(CONNECTION_STRING)
conexion_db = client['datos'] # en este caso se crea una carpeta con nombre test
colleccion = conexion_db['animales'] # en este paso se crea lo que mongo denomina colección de datos
# ingresar datos de prueba
animales = [
  { "_id": 1, "name": "Perro", "domestico": "si"},
  { "_id": 2, "name": "Gato", "domestico": "si"},
  { "_id": 3, "name": "Pez", "domestico": "si"},
  { "_id": 4, "name": "Murcielago", "domestico": "no"},
]
colleccion.insert_many(animales) #agrega los datos a la base en mongocompass