import json

dictio = {"enero" : 1,
          "febrero": 2,
          "marzo": 3,
          "abril": 4,
          "mayo": 5, 
          "junio": 6, 
          "julio": 7,
          "agosto": 8, 
          "setiembre": 9, 
          "octubre": 10, 
          "noviembre": 11, 
          "diciembre": 12}

dictio_json = json.dumps(dictio)
print(dictio_json)