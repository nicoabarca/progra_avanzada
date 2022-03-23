from PyQt5.QtCore import QObject, pyqtSignal

class LogicaInicio(QObject):

    senal_abrir_ranking = pyqtSignal()
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    #Manda la senal para abrir el ranking y su logica
    def abrir_ranking(self):
        self.senal_abrir_ranking.emit()

    #Manda la senal para abrir la ventana de juego y su logica
    def abrir_juego(self, nombre_usuario):
        self.senal_abrir_juego.emit(nombre_usuario)