from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDesktopWidget
)

import re
import parametros as p

class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_enviar_ranking = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):

        self.setWindowTitle("Ventana de Inicio")
        self.setWindowIcon(QIcon(p.RUTA_LOGO))
        self.setFixedSize(600, 500)
        self.center()
        
        #Logo de DCCrossy Frog
        self.logo_img = QLabel(self)
        self.logo_img.setPixmap(QPixmap(p.RUTA_LOGO))
        self.logo_img.setScaledContents(True)

        #Input Nombre Usuario
        self.nombre_label = QLabel("Escribe tu nombre de usuario", self)
        self.nombre_form = QLineEdit("", self)

        #Boton Iniciar partida
        self.iniciar_button = QPushButton("Iniciar partida", self)
        self.iniciar_button.clicked.connect(self.abrir_ventana_juego)
        self.iniciar_button.setAutoDefault(True)

        #Boton Ver ranking
        self.ranking_button = QPushButton("Ver ranking", self)
        self.ranking_button.clicked.connect(self.abrir_ventana_ranking)

        vbox = QVBoxLayout()
        vbox.addWidget(self.logo_img)
        vbox.addStretch(1)
        vbox.addWidget(self.nombre_label)
        vbox.addWidget(self.nombre_form)
        vbox.addStretch(1)
        vbox.addWidget(self.iniciar_button)
        vbox.addStretch(1)
        vbox.addWidget(self.ranking_button)
        self.setLayout(vbox)
    
    #Envia la senal para abrir la ventana de ranking
    def abrir_ventana_ranking(self):
        self.senal_enviar_ranking.emit()
        self.hide()

    #Envia la senal para abrir la ventana de juego
    def abrir_ventana_juego(self):
        nombre_usuario = self.nombre_form.text()
        valido, errores = self.validar_nombre(nombre_usuario)

        if valido:
            self.senal_enviar_login.emit(nombre_usuario)
            self.hide()
        else :
            self.alerta_usuario(errores)
            self.nombre_form.setText("")

    #Se alerta al usuario si su nombre no es valido
    def alerta_usuario(self, errores):
        mensaje = QMessageBox()
        mensaje.setWindowIcon(QIcon(p.RUTA_LOGO))
        mensaje.setIcon(QMessageBox.Critical)
        mensaje.setWindowTitle("Error")
        mensaje.setText("\n".join(errores))
        mensaje.exec_()

    #Valida si el nombre ingresado es valido
    def validar_nombre(self, nombre_usuario):
        min, max = p.MIN_CARACTERES, p.MAX_CARACTERES
        alfanumerico = '^[a-zA-Z0-9_]+$' #no incluye ñ 
        cumple_largo = min <= len(nombre_usuario) <= max
        cumple_alfanumerico = re.match(alfanumerico, nombre_usuario)
        errores = []
        valido = True

        if not cumple_largo:
            mensaje = f"El nombre debe tener entre {min} y {max} caracteres."
            errores.append(mensaje)
            valido = False

        if not cumple_alfanumerico:
            mensaje = "El nombre de usuario no es alfanumérico."
            errores.append(mensaje)
            valido = False

        return valido, errores
    
    #Muestra la ventana
    def mostrar(self):
        self.show()
        
    #Funcion para centrar la ventana, independiente del tamañano 
    # de la pantalla donde se muestre  
    # https://python-commandments.org/pyqt-center-window/
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())