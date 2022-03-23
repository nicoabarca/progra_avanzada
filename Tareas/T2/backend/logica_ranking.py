from PyQt5.QtCore import QObject, pyqtSignal

from pathlib import Path
import parametros as p

class LogicaRanking(QObject):

    senal_abrir_inicio = pyqtSignal()
    senal_lista_puntajes = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.top5_puntajes = []

        self.crear_archivo_puntajes()
        self.lista_mejores_puntajes()

    #Funcion para crear puntajes.txt si no existe
    #https://appdividend.com/2021/06/03/how-to-create-file-if-not-exists-in-python/
    def crear_archivo_puntajes(self):
        existe_archivo_puntajes = Path("backend", "puntajes.txt")
        existe_archivo_puntajes.touch(exist_ok=True)

    #Ordena en una lista a los cinco mejores puntajes
    def lista_mejores_puntajes(self):
        lista_puntajes = []

        with open(Path("backend", "puntajes.txt"), "r", encoding="UTF-8") as archivo:

            for linea in archivo.readlines():
                tupla_nombre_puntaje = tuple(linea.strip().split(","))
                lista_puntajes.append(tupla_nombre_puntaje)

        lista_puntajes.sort(key=lambda puntaje: puntaje[1], reverse=True)
        self.top5_puntajes = lista_puntajes[:5]

    #Manda la senal para volver a la ventana de inicio
    def abrir_inicio(self):
        self.senal_abrir_inicio.emit()

    #Manda la lista de puntajes a ventana de ranking
    def mandar_puntajes(self):
        self.senal_lista_puntajes.emit(self.top5_puntajes)

    #Se encarga de actualizar la data de los ranking
    #cuando un jugador pierde o no quiere seguir jugando
    def actualizar_data_ranking(self, nuevo_nombre_puntaje):
        lista_puntajes = []
        with open(Path("backend", "puntajes.txt"), "r", encoding="UTF-8") as archivo:
            for linea in archivo.readlines():
                tupla_nombre_puntaje = tuple(linea.strip().split(","))
                lista_puntajes.append(tupla_nombre_puntaje)

        lista_nombres = [nombre_puntaje[0] for nombre_puntaje in lista_puntajes]
        if nuevo_nombre_puntaje[0] not in lista_nombres:
            lista_puntajes.append(nuevo_nombre_puntaje)
        else:
            for index, nombre_puntaje in enumerate(lista_puntajes):
                if nuevo_nombre_puntaje[0] == nombre_puntaje[0]:
                    if tupla_nombre_puntaje[1] > nombre_puntaje[1]:
                        lista_puntajes[index] = nuevo_nombre_puntaje

        with open(Path("backend", "puntajes.txt"), "w", encoding="UTF-8") as archivo:
            for tupla_nombre_puntaje in lista_puntajes:
                archivo.write(f"{tupla_nombre_puntaje[0]},{tupla_nombre_puntaje[1]}\n")







