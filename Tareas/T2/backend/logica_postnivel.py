from PyQt5.QtCore import QObject, pyqtSignal

class LogicaPostNivel(QObject):

    senal_actualizar_valores_juego = pyqtSignal()
    senal_abrir_juego = pyqtSignal()
    senal_data_ranking = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

    #Manda una senal para actualizar los valores de los atributos de
    #LogicaJuego en base al nivel en el cual esta
    def actualizar_valores_nivel(self):
        self.senal_actualizar_valores_juego.emit()

    #Senal para reanudar el juego cuando se apreta el boton
    #de Seguir nivel en el frontend
    def reanudar_juego(self):
        self.senal_abrir_juego.emit()

    #Senal encargada de agregar al jugador en la ventana de ranking
    def recibir_data_ranking(self, tupla_nombre_ptj):
        self.senal_data_ranking.emit(tupla_nombre_ptj)