import requests

def info_api_curso(token):
    url = "https://www.avanzada.ml/api/v2/bonus/ability"
    response = requests.get(f"{url}?api_token={token}")

    if response.status_code == 200:
        return response.json()
    
    return {}
    
def enviar_test(token, test_id, respuesta):
    url =  f"https://www.avanzada.ml/api/v2/bonus/tests/{test_id}?api_token={token}"
    dict_functions = {
        "1": "obtener_info_habilidad",
        "2": "obtener_pokemones",
        "3": "obtener_pokemon_mas_alto",
        "4": "obtener_pokemon_mas_rapido",
        "5": "obtener_mejores_atacantes",
        "6": "obtener_pokemones_por_tipo"
    }
    data = {
        "test": {
            "function_name": dict_functions[str(test_id)],
            "function_response": respuesta
        }
    }

    response = requests.post(url, json=data)
    response_result = response.json()

    if response_result["result"] == "success":
        return True
    else:
        print(response_result["message"])
        return False
