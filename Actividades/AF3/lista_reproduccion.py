"""
En este archivo se encuentra la clase ListaReproduccion, la Iterable que
contiene los videos ordenados
"""


class ListaReproduccion:

    def __init__(self, conjunto_videos, usuario, nombre):
        self.conjunto_videos = conjunto_videos
        self.usuario = usuario
        self.nombre = nombre

    def __iter__(self):
        # Debes completar este método
        return IterarLista(self.conjunto_videos.copy())

    def __str__(self):
        return f"Lista de Reproducción de {self.usuario}: {self.nombre}"


class IterarLista:

    def __init__(self, conjunto_videos):
        self.conjunto_videos = conjunto_videos

    def __iter__(self):
        # Debes completar este método
        return self

    def __next__(self):
        # Debes completar este método
        if len(self.conjunto_videos) == 0:
            raise StopIteration("Ya no hay peliculas")
        else:
            #Para hacer esta parte ocupe este código como base
            #https://stackoverflow.com/questions/13145368/find-the-maximum-value-in-a-list-of-tuples-in-python
            
            pelicula_mayor_afinidad = max(self.conjunto_videos, key=lambda item:item[1])
            self.conjunto_videos.remove(pelicula_mayor_afinidad)
            return pelicula_mayor_afinidad
