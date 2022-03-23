from collections import defaultdict
import requests

def obtener_info_habilidad(url):
    response = requests.get(url)
    response_dict = response.json()
    
    nombre_habilidad = str(response_dict["name"])

    response_descripciones_de_habilidad = response_dict["effect_entries"]

    for descripcion in response_descripciones_de_habilidad:
        if descripcion["language"]["name"] == "en":
            descripcion_habilidad_en = str(descripcion["short_effect"])

    response_pokemones = response_dict["pokemon"]

    lista_pokemones = []
    
    for response_pokemon in response_pokemones:
        lista_pokemones.append(
            {
                "name": str(response_pokemon["pokemon"]["name"]),
                "url": str(response_pokemon["pokemon"]["url"])
            }
        )

    return {
        "name": nombre_habilidad,
        "effect_entries": descripcion_habilidad_en,
        "pokemon": lista_pokemones
    }

def obtener_pokemones(pokemones):
    response = requests.get(pokemones[0]["url"])
    response_dict = response.json()

    lista_data_pokemones = []

    for pokemon in pokemones:
        response = requests.get(pokemon["url"])
        response_dict = response.json()

        pokemon_stats_dict = {}

        for pokemon_stat in response_dict["stats"]:
            nombre_stat = pokemon_stat["stat"]["name"]
            pokemon_stats_dict[nombre_stat] = {
                "base_stat": int(pokemon_stat["base_stat"]),
                "effort": int(pokemon_stat["effort"])
            }

        pokemon_types = []

        for data_type in response_dict["types"]:
            pokemon_types.append(str(data_type["type"]["name"]))  

        lista_data_pokemones.append({
            "id": int(response_dict["id"]),
            "name": str(response_dict["name"]),
            "height": int(response_dict["height"]),
            "weight": int(response_dict["weight"]),
            "stats": pokemon_stats_dict,
            "types": pokemon_types
        })

    return lista_data_pokemones

def obtener_pokemon_mas_alto(pokemones):
    max_altura = 0
    pokemon_mas_alto = ""

    for pokemon in pokemones:
        if pokemon["height"] > max_altura:
            max_altura = pokemon["height"]
            pokemon_mas_alto = pokemon["name"]

    return pokemon_mas_alto

def obtener_pokemon_mas_rapido(pokemones):
    max_velocidad = 0
    pokemon_mas_veloz = ""

    for pokemon in pokemones:
        if "speed" in list(pokemon["stats"].keys()):
            velocidad_pokemon = int(pokemon["stats"]["speed"]["base_stat"])
            if velocidad_pokemon >= max_velocidad:
                max_velocidad = velocidad_pokemon
                pokemon_mas_veloz = pokemon["name"]

    return pokemon_mas_veloz

def obtener_mejores_atacantes(pokemones):
    lista_ataque_pokemones = []

    for pokemon in pokemones:   
        ataque_en_stats = "attack" in list(pokemon["stats"].keys())
        defensa_en_stats = "defense" in list(pokemon["stats"].keys())

        if ataque_en_stats and defensa_en_stats:
            nombre = pokemon["name"]
            ataque = int(pokemon["stats"]["attack"]["base_stat"])
            defensa = int(pokemon["stats"]["defense"]["base_stat"])

            dict_data = {
                "name": nombre,
                "atk_def": ataque / defensa,
            }

            lista_ataque_pokemones.append(dict_data)

    lista_atk_def_ordenada = sorted(
        lista_ataque_pokemones,
        key=lambda dict_data: dict_data["atk_def"],
        reverse=True
    )

    lista_objeto_pokemones_ordenada = []

    for pokemon_atk_def in lista_atk_def_ordenada:
        for index in range(len(pokemones)):   
            if pokemon_atk_def["name"] == pokemones[index]["name"]:
                lista_objeto_pokemones_ordenada.append(pokemones[index])

    if len(lista_objeto_pokemones_ordenada) < 5 :
        return lista_objeto_pokemones_ordenada
    else:
        return lista_objeto_pokemones_ordenada[:5]

def obtener_pokemones_por_tipo(pokemones):
    pokemon_types_dict = {}
    for pokemon in pokemones:
        for type in pokemon["types"]:
            if type not in pokemon_types_dict.keys():
                pokemon_types_dict[str(type)] = []

            pokemon_types_dict[str(type)].append(pokemon["name"])
            
    return pokemon_types_dict