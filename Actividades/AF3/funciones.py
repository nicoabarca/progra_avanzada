"""
En este archivo se completan las funciones que son utilizadas para
la creación de la lista de reproducción
"""
from functools import reduce

from usuario import Usuario


def filtrar_prohibidos(iterar_peliculas, actor_prohibido):
    """
    Debe filtrar todas películas  que contengan temas prohibidos
    :param actor_prohibido: actor prohibido del usuario
    :param iterar_peliculas: iterador sobre lista de Videos
    :return: filter
    """
    # Debes completar esta función
    return filter(lambda actor: actor != actor_prohibido, list(iterar_peliculas))

def calcular_afinidades(catalogo_peliculas, usuario: Usuario):
    """
    La función debe calcular las afinidades según preferencias del usuario.
    El map retorna tuplas, donde el primer valor es la pelicula,
    y el segundo valor la afinidad.
    :param usuario: Usuario para quien se crearán las afinidades
    :param catalogo_peliculas: zip que retorna peliculas
    :return: mapeo que retorna tuplas.
    """
    # Debes completar esta función
    mapeo_afinidades = map(lambda pelicula: 
    (pelicula, usuario.calcular_afinidad(pelicula)), catalogo_peliculas )
    return mapeo_afinidades

def encontrar_peliculas_comunes(usuarios_watch_party):
    """
    La función debe encontrar las películas comunes entre las favoritas
    de cada usuario, y retornar un set que las contenga.
    :param usuarios_watch_party: lista de usuarios que conforman la watch party
    :return: interseccion de las peliculas favoritas de cada usuario
    """
    # Debes completar esta función
    lista_peliculas_comunes = list(map(lambda usuario: 
    usuario.peliculas_favoritas, usuarios_watch_party))
    return reduce(lambda x,y : x | y, lista_peliculas_comunes)

def encontrar_usuario_mas_afin(usuario, otros_usuarios):
    """
    Esta función debe encontrar el usuario con mayor compatibilidad.
    Debe primero filtrar usuarios que no tengan el mismo actor_prohibido,
    y luego encontrar aquél con quien tenga mayor compatibilidad
    :param usuario: usuario para quien se encontrará un amigue
    :param otros_usuarios: el resto de los usuarios de DCCabritas
    :return: Usuario más compatible
    """
    # Debes completar esta función
    lista_usarios_ap = list(filter(lambda usuario_lista : 
    usuario_lista.actor_prohibido == usuario.actor_prohibido, otros_usuarios))

    lista_compatibilidad = list(map(lambda usuario_lista : 
    usuario_lista + usuario, lista_usarios_ap ))

    lista_usuarios_compatibilidad = list(zip(lista_usarios_ap, lista_compatibilidad))
    return reduce(lambda us_1, us_2: max(us_1[1], us_2[1]), lista_usuarios_compatibilidad)