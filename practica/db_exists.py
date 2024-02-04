from pymongo import MongoClient

# Conectar a MongoDB (asegúrate de tener tu servidor MongoDB en ejecución)
client = MongoClient('localhost', 27017)

# Nombre de la base de datos que quieres verificar
nombre_base_de_datos = 'platos_candela'

# Obtener la lista de nombres de bases de datos
nombres_bases_de_datos = client.list_database_names()

# Verificar si la base de datos existe
if nombre_base_de_datos in nombres_bases_de_datos:
    print(f"La base de datos '{nombre_base_de_datos}' existe.")
else:
    print(f"La base de datos '{nombre_base_de_datos}' no existe.")
