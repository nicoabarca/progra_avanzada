import operator
from collections import namedtuple
from datetime import datetime

#Retorna una lista de namedtuples (comentarios_type) de las lineas de comentarios.csv
#Cada elemento de la lista son los datos de cada comentario
def datos_comentarios():
    with open("comentarios.csv", "r", encoding = "utf-8") as archivo_comentarios:
        lista_de_comentarios = []
        comentarios = namedtuple(
            "comentarios_type",
            [
                "id_publicacion",
                "usuario", 
                "fecha_emision", 
                "contenido"
            ]
            )
        for comentario in archivo_comentarios:
            lista_comentario = comentario.strip().split(",", 3)
            
            tupla_comentario = comentarios( *lista_comentario)
            lista_de_comentarios.append(tupla_comentario)
        #el primer elemento de la lista no me sirve, ya que es el header del csv
        del lista_de_comentarios[0]
    #se retorna la lista ordenada de comentarios viejos a nuevos
    return sorted(lista_de_comentarios, key = operator.itemgetter(2))

#Retorna una lista de namedtuples (publicaciones_type) de las lineas de comentarios.csv
#Cada elemento de la lista son los datos de cada publicación
def datos_publicaciones():
    with open("publicaciones.csv", "r", encoding = "utf-8") as archivo_publicaciones:
        lista_de_publicaciones = []
        publicaciones = namedtuple(
            "publicaciones_type",
            [
                "id_publicacion", 
                "nombre_publicacion", 
                "usuario", 
                "fecha_creacion", 
                "precio", 
                "descripcion"
            ]
        )
        for publicacion in archivo_publicaciones:
            lista_publicacion = publicacion.strip().split(",", 5)
            
            tupla_publicacion = publicaciones( *lista_publicacion)
            lista_de_publicaciones.append(tupla_publicacion)
        #el primer elemento de la lista no me sirve, ya que es el header del csv
        del lista_de_publicaciones[0]
    #se retorna la lista ordenada de publicaciones nuevas a viejas
    return sorted(lista_de_publicaciones, key = operator.itemgetter(3), reverse=True)

#Retorna una lista con los usuarios registrados que aparecen en el archivo usuarios.csv
def datos_usuarios_registrados():
    with open("usuarios.csv", "r") as archivo_usuarios:
        lista_de_usuarios = []
        for usuario in archivo_usuarios:
            lista_de_usuarios.append(usuario.strip())
        #el primer elemento de la lista no me sirve, ya que es el header del csv
        del lista_de_usuarios[0]
    return lista_de_usuarios

#Retorna una lista de las publicaciones realizadas por un usuario especifico
def publicaciones_realizadas_usuario(usuario):
    lista_publicaciones_realizadas = []
    for publicacion in datos_publicaciones():
        if publicacion.usuario == usuario:
            lista_publicaciones_realizadas.append(publicacion)
    return lista_publicaciones_realizadas

#Agrega un nombre de usuario al archivo usuarios.csv
def agregar_usuario_nuevo(nombre_usuario):
    with open("usuarios.csv", "a", encoding = "utf-8") as archivo_usuarios:
        archivo_usuarios.write(f"\n{nombre_usuario}")

#Agrega un comentario a una publicación en específico
def agregar_comentario(id_publicacion, nombre_usuario, contenido):
    fecha = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    datos_comentario = f"{id_publicacion},{nombre_usuario},{fecha},{contenido}"

    with open("comentarios.csv", "a", encoding = "utf-8") as archivo_comentarios:
        archivo_comentarios.write(f"""
{datos_comentario}""")

#Crea una publicación con todos los datos que necesita y la agrega a publicaciones.csv
def crear_publicacion(nombre_pub, usuario, precio, descripcion):
    #list_ids_publicaciones y los if-else están para crear una publicación con id única
    lista_ids_publicaciones = [
        int(publicacion.id_publicacion) 
        for publicacion in datos_publicaciones()]

    if len(lista_ids_publicaciones) == 0:
        id_nueva = 1
    else:
        id_nueva =  max(lista_ids_publicaciones) + 1

    fecha = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    datos_publicacion_nueva = f"{id_nueva},{nombre_pub},{usuario},{fecha},{precio},{descripcion}"

    with open("publicaciones.csv", "a", encoding = "utf-8") as archivo_publicaciones:
        archivo_publicaciones.write(f"""
{datos_publicacion_nueva}""") 

#Elimina una publicación y tambien los comentarios de esa publicación
def eliminar_publicacion(input_usuario, usuario):
    publicacion_usuario = publicaciones_realizadas_usuario(usuario)
    publicacion_elegida = publicacion_usuario[int(input_usuario) - 1]
    id_publicacion_eliminar = publicacion_elegida.id_publicacion

    #lista de publicaciones actualizadas (sin la eliminada)
    publicaciones_actualizadas = [publicacion
    for publicacion in datos_publicaciones()
    if publicacion.id_publicacion != id_publicacion_eliminar]

    header_csv = "id_publicacion,nombre_publicacion,usuario,fecha_creacion,precio,descripcion\n"
    
    #publicaciones.csv se escribe denuevo con la una publicación eliminada
    with open("publicaciones.csv", "w", encoding = "utf-8") as archivo_publicaciones:
        archivo_publicaciones.write(header_csv)
        indice = 0
        for publicacion in publicaciones_actualizadas:

            id = publicacion.id_publicacion
            nombre = publicacion.nombre_publicacion
            nombre_usuario = publicacion.usuario
            fecha = publicacion.fecha_creacion
            precio = publicacion.precio
            descripcion = publicacion.descripcion

            #Esta condición esta para no agregar un \n al final de la última línea
            #del archivo publicaciones.csv
            if indice == len(publicaciones_actualizadas) - 1:
                linea = f"{id},{nombre},{nombre_usuario},{fecha},{precio},{descripcion}"
            else:
                linea = f"{id},{nombre},{nombre_usuario},{fecha},{precio},{descripcion}\n"
                indice += 1

            archivo_publicaciones.write(linea)
    
    comentarios_actualizados = [comentario
    for comentario in datos_comentarios()
    if comentario.id_publicacion != id_publicacion_eliminar]

    header_csv = "id_publicacion,usuario,fecha_emision,contenido\n"

    #comentarios.csv se escribe denuevo sin los comentarios de la publicación eliminada
    with open("comentarios.csv", "w", encoding = "utf-8") as archivo_comentarios:
        archivo_comentarios.write(header_csv)
        indice = 0
        for comentario in comentarios_actualizados:
            id = comentario.id_publicacion
            nombre_usuario = comentario.usuario
            fecha = comentario.fecha_emision
            contenido = comentario.contenido

            #Esta condición esta para no agregar un \n al final de la última línea
            #del archivo comentarios.csv
            if indice == len(comentarios_actualizados) - 1:
                linea = f"{id},{nombre_usuario},{fecha},{contenido}"
            else:
                linea = f"{id},{nombre_usuario},{fecha},{contenido}\n"
                indice += 1

            archivo_comentarios.write(linea)

if __name__ == '__main__':
    print("Módulo para leer y modificar los archivos csv")