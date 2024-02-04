from pymongo import MongoClient

# Conectar a MongoDB (asegúrate de tener tu servidor MongoDB en ejecución)
client = MongoClient('localhost', 27017)

# Seleccionar una base de datos
db = client['platos_candela']

# Seleccionar una colección
collection = db['platos']

# Datos a insertar
platos = [
    {"nombre": "Pollo Dorado con Arroz y Papas Fritas", "precio": 45},
    {"nombre": "Causa de Pollo", "precio": 15},
    {"nombre": "Emoliente Caliente", "precio": 10},
    {"nombre": "Trucha a la Milanesa con Papas Fritas", "precio": 45},
    {"nombre": "Jugo de Piña 0.5L", "precio": 10},
    {"nombre": "Lomo a lo Pobre", "precio": 48},
    {"nombre": "Lomo Fino con Arroz y Papas Fritas", "precio": 46},
    {"nombre": "Ensalada de Palta", "precio": 12},
    {"nombre": "Ensalada Mixta", "precio": 8},
    {"nombre": "Lomo en Salsa de Champiñones con Arroz y Papas Fritas", "precio": 48},
    {"nombre": "Jugo de Fresa 0.5L", "precio": 12},
    {"nombre": "Ensalada de Verduras Cocidas (Caliente)", "precio": 10},
    {"nombre": "Porción de Yucas Fritas", "precio": 15},
    {"nombre": "Seco de Ternera con Arroz y Frejoles", "precio": 43},
    {"nombre": "Arroz con Pato", "precio": 48},
    {"nombre": "Seco de Pollo con Arroz y Puré", "precio": 45},
]

# Insertar los datos en la colección
result = collection.insert_many(platos)

# Imprimir los IDs de los documentos insertados
print(f"Documentos insertados: {result.inserted_ids}")

print("_______________________________________________________________________________________")

# Nombre de la base de datos que quieres verificar
nombre_base_de_datos = 'platos_candela'

# Obtener la lista de nombres de bases de datos
nombres_bases_de_datos = client.list_database_names()

# Verificar si la base de datos existe
if nombre_base_de_datos in nombres_bases_de_datos:
    print(f"La base de datos '{nombre_base_de_datos}' existe.")
else:
    print(f"La base de datos '{nombre_base_de_datos}' no existe.")
    