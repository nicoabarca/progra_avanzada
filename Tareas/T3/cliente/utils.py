import json
import os

#Gets a key string and returns data from parametros.json
def get_json_data(key):
    ruta = os.path.join("parametros.json")
    with open(ruta, "r", encoding="UTF-8") as file:
        dict_data = json.load(file)
    data = dict_data[key]
    return data
