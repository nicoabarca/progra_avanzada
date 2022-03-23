from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QDesktopWidget
)

import parametros as p

class VentanaRanking(QWidget):

    senal_enviar_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana de Inicio")
        self.setWindowIcon(QIcon(p.RUTA_LOGO))
        self.setFixedSize(600, 500)
        self.center()

        #Ranking de Puntajes
        self.titulo_label = QLabel("Ranking de Puntajes", self)
        self.titulo_label.setFont(QFont("Arial", 30))
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setGeometry(130, 30, 400, 50)
        
        #Boton Volver
        self.volver_button = QPushButton("Volver", self)
        self.volver_button.setGeometry(250, 250, 100, 30)
        self.volver_button.clicked.connect(self.volver_al_inicio)

    #Crea un layout en base a los puntajes
    #de ranking que existen
    def crear_layout(self, vlayout_lista_puntajes):
        vbox = QVBoxLayout()
        vbox.addWidget(self.titulo_label)
        vbox.addStretch(1)
        vbox.addLayout(vlayout_lista_puntajes)
        vbox.addStretch(1)
        vbox.addWidget(self.volver_button)
        self.setLayout(vbox)

    #Vuelve a la ventana de inicio
    def volver_al_inicio(self):
        self.senal_enviar_inicio.emit()
        self.hide()

    #Funcion que envia una señal cuando se cierra la ventana de ranking
    def closeEvent(self, event):
        self.senal_enviar_inicio.emit()
        event.accept()
        self.hide()

    #Agrega al layout los mejores 5 puntajes
    def lista_mejores_puntajes(self, lista_puntajes):
        vbox_puntajes = QVBoxLayout()
        indice = 1
        for puntaje in lista_puntajes:
            nombre, puntos = puntaje
            label = QLabel(f"{indice}. {nombre} {puntos} puntos", self)
            label.setFont(QFont("Arial", 20))
            label.setAlignment(Qt.AlignCenter)
            vbox_puntajes.addWidget(label)
            indice += 1
        self.crear_layout(vbox_puntajes)

    #Muestra la ventana de ranking
    def mostrar(self):
        self.show()
        
    #Funcion para centrar la ventana, independiente del tamañano
    #  de la pantalla donde se muestre  
    # https://python-commandments.org/pyqt-center-window/
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
