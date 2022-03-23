from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QDesktopWidget
)

import parametros as p

class VentanaPostNivel(QWidget):

    senal_actualizar_valores_juego = pyqtSignal()
    senal_abrir_juego = pyqtSignal(str)
    senal_data_ranking = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana de Post-Nivel")
        self.setWindowIcon(QIcon(p.RUTA_LOGO))
        self.setFixedSize(600, 500)
        self.center()

        #Titulo Resumen de Nivel
        self.titulo_label = QLabel("Resumen de Nivel", self)
        self.titulo_label.setFont(QFont("Arial", 30))
        self.titulo_label.setGeometry(140, 30, 320, 30)

        self.nivel_label = QLabel(f"Nivel actual: ", self)
        self.nivel_label.setGeometry(120, 100, 400, 30)
        self.nivel_label.setFont(QFont("Arial", 20))
        
        self.puntaje_total_label = QLabel(f"Puntaje total: ", self)
        self.puntaje_total_label.setGeometry(120, 140, 500, 30)
        self.puntaje_total_label.setFont(QFont("Arial", 20))
        
        self.puntaje_nivel_label = QLabel(f"Puntaje obtenido en el nivel: ", self)
        self.puntaje_nivel_label.setGeometry(120, 180, 500, 30)
        self.puntaje_nivel_label.setFont(QFont("Arial", 20))
        
        self.vidas_label = QLabel(f"Vidas restantes: ", self)
        self.vidas_label.setGeometry(120, 220, 400, 30)
        self.vidas_label.setFont(QFont("Arial", 20))

        self.monedas_label = QLabel(f"Total de monedas: ", self)
        self.monedas_label.setGeometry(120, 260, 400, 30)
        self.monedas_label.setFont(QFont("Arial", 20))

        self.label_seguir = QLabel('', self)
        self.label_seguir.setGeometry(140, 320, 320, 30)
        self.label_seguir.setFont(QFont("Arial", 10))

        self.boton_tienda = QPushButton("Ir a la Tienda", self)
        self.boton_tienda.setGeometry(120, 400, 100, 30)
        self.boton_tienda.setDisabled(True)

        self.boton_siguiente_nivel = QPushButton("Siguiente nivel", self)
        self.boton_siguiente_nivel.setGeometry(240, 400, 100, 30)
        self.boton_siguiente_nivel.clicked.connect(self.actualizar_valores_juego)
        self.boton_siguiente_nivel.clicked.connect(self.abrir_juego)        

        self.boton_salir = QPushButton("Salir", self)
        self.boton_salir.setGeometry(360, 400, 100, 30)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_salir.clicked.connect(self.mandar_data_ranking)
    
    #Actualiza la data que se va a mostrar en la ventana de postnivel
    def actualizar_atributos(self, dic):
        self.data = dic
        self.resumen_nivel()
        self.label_seguir_jugando()
        self.botones_de_opciones()
        self.mostrar()

    #Despliega un resumen de lo sucedido en el nivel pasado,
    #gracias al cambio de texto de los QLabels
    def resumen_nivel(self): 
        self.nivel_label.setText(f"Nivel actual: {self.data['nivel_actual']}") 
        self.puntaje_total_label.setText(f"Puntaje total: {self.data['puntaje_total']}")
        self.puntaje_nivel_label.setText(
            f"Puntaje obtenido en el nivel: {self.data['puntaje_nivel']}"
            ) 
        self.vidas_label.setText(f"Vidas restantes: {self.data['vidas']}")
        self.monedas_label.setText(f"Total de monedas: {self.data['monedas']}")
    
    #Despliega un QLabel que indica si el jugador,
    #puede seguir jugando o perdio
    def label_seguir_jugando(self):
        if self.data['vidas'] == str(0):
            self.label_seguir.setText("No puedes seguir jugando.")
            self.label_seguir.setStyleSheet("border: 2px solid red")
        else:
            self.label_seguir.setText("Puedes seguir con el siguiente nivel.")
            self.label_seguir.setStyleSheet("border: 2px solid green")

    #En caso de salir del juego,
    #se manda el nombre y puntaje del jugador
    #para ser agregado al ranking de puntajes
    def mandar_data_ranking(self):
        nombre = self.data['nombre']
        puntaje = self.data['puntaje_total']
        self.senal_data_ranking.emit((nombre, puntaje))

    #Deshabilita el boton de siguiente nivel,
    #si el jugador no tiene vidas
    def botones_de_opciones(self):
        if self.data['vidas'] == str(0):
            self.boton_siguiente_nivel.setDisabled(True)
    
    #Senal que actualiza los valores de la Logica de Juego
    #en base al nivel al cual se avanzo
    def actualizar_valores_juego(self):
        self.senal_actualizar_valores_juego.emit()

    #Senal para abrir la ventana de juego
    def abrir_juego(self):
        self.senal_abrir_juego.emit(self.data['nombre'])
        self.salir()
    
    #Cierra la ventana de postnivel
    def salir(self):
        self.close()

    #Muestra la ventana de postnivel
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
