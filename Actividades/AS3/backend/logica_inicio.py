from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(tuple)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_contrasena(self, credenciales):
        # COMPLETAR
        nombre, clave = credenciales
        validacion = False

        if clave.lower() == p.CONTRASENA.lower():
            self.senal_abrir_juego.emit(nombre)
            validacion = True
        
        self.senal_respuesta_validacion.emit((nombre, validacion))
