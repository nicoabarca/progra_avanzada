from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QRect, QPoint
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QDesktopWidget
)
import parametros as p

class VentanaJuego(QWidget):

    senal_enviar_posicion_rana = pyqtSignal(list)
    senal_enviar_pos_autos = pyqtSignal(list)
    senal_enviar_pos_troncos = pyqtSignal(list)
    senal_enviar_pausar_juego = pyqtSignal()
    senal_enviar_despausar_juego = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.nombre_usuario = ""
        self.pos_y_carreteras = [260, 300, 340, 620, 660, 700]
        self.pos_y_rio = [440, 480, 520]
        self.lista_objetos_activos = []
        self.juego_pausado = False
        self.init_gui()

    def init_gui(self):

        self.setWindowIcon(QIcon(p.RUTA_LOGO))
        self.setFixedSize(1200, 800)
        self.center()
        self.fondo = QLabel(self)
        self.fondo.setGeometry(0, 0, 1200, 800)
        self.fondo.setStyleSheet("background: #063613")

        #Marco de color izquierdo
        self.fondo_color_izq = QLabel(self)
        self.fondo_color_izq.setGeometry(20, 20, 460, 160)
        self.fondo_color_izq.setStyleSheet(
            "background: #F5FFFA; border:4px solid gray;"
            )

        #Marco de color derecho
        self.fondo_color_der = QLabel(self)
        self.fondo_color_der.setGeometry(720, 20, 460, 160)
        self.fondo_color_der.setStyleSheet(
            "background: #F5FFFA; border:4px solid gray;"
            )

        #Logo de DCCrossy Frog
        self.logo_img = QLabel(self)
        self.logo_img.setPixmap(QPixmap(p.RUTA_LOGO))
        self.logo_img.setScaledContents(True)
        self.logo_img.setGeometry(500, 0, 200, 200)

        #Label Vidas
        self.vidas_label = QLabel("VIDAS: 3", self)
        self.vidas_label.setFont(QFont("Times", 20))
        self.vidas_label.setGeometry(180, 30, 200, 40)

        #Label Tiempo
        self.tiempo_label = QLabel("TIEMPO: 60 s", self)
        self.tiempo_label.setFont(QFont("Times", 20))
        self.tiempo_label.setGeometry(180, 80, 200, 40)

        #Label Monedas
        self.monedas_label = QLabel("MONEDAS: 4", self)
        self.monedas_label.setFont(QFont("Times", 20))
        self.monedas_label.setGeometry(180, 130, 200, 40)

        #Label Nivel
        self.nivel_label = QLabel("NIVEL: 1", self)
        self.nivel_label.setFont(QFont("Times", 20))
        self.nivel_label.setGeometry(800, 40, 200, 40)

        #Label Puntaje
        self.puntaje_label = QLabel("PUNTAJE: 25", self)
        self.puntaje_label.setFont(QFont("Times", 20))
        self.puntaje_label.setGeometry(800, 100, 200, 40)

        #Boton Pausar
        self.pausar_button = QPushButton("Pausar", self)
        self.pausar_button.setGeometry(1050, 45, 90, 30)
        # self.pausar_button.clicked.connect()
        # recordar que tambien se puede pausar ocupando la letra P

        #Boton Salir
        self.salir_button = QPushButton("Salir", self)
        self.salir_button.setGeometry(1050, 105, 90, 30)
        self.salir_button.clicked.connect(self.salir)
        
        #Pasto superior
        self.pasto_sup = QLabel(self)
        self.pasto_sup.setPixmap(QPixmap(p.RUTA_PASTO))
        self.pasto_sup.setScaledContents(True)
        self.pasto_sup.setGeometry(20, 210, 1160, 50)

        #Carretera superior
        self.carretera_sup = QLabel(self)
        self.carretera_sup.setPixmap(QPixmap(p.RUTA_CARRETERA))
        self.carretera_sup.setScaledContents(True)
        self.carretera_sup.setGeometry(20, 260, 1160, 120)

        #Pasto medio superior
        self.pasto_medio_sup = QLabel(self)
        self.pasto_medio_sup.setPixmap(QPixmap(p.RUTA_PASTO))
        self.pasto_medio_sup.setScaledContents(True)
        self.pasto_medio_sup.setGeometry(20, 380, 1160, 60)

        #Rio
        self.rio = QLabel(self)
        self.rio.setPixmap(QPixmap(p.RUTA_RIO))
        self.rio.setScaledContents(True)
        self.rio.setGeometry(20, 440, 1160, 120)

        #Pasto medio inferior
        self.pasto_medio_inf = QLabel(self)
        self.pasto_medio_inf.setPixmap(QPixmap(p.RUTA_PASTO))
        self.pasto_medio_inf.setScaledContents(True)
        self.pasto_medio_inf.setGeometry(20, 560, 1160, 60)

        #Carretera inferior
        self.carretera_inf = QLabel(self)
        self.carretera_inf.setPixmap(QPixmap(p.RUTA_CARRETERA))
        self.carretera_inf.setScaledContents(True)
        self.carretera_inf.setGeometry(20, 620, 1160, 120)

        #Pasto inferior
        self.pasto_inf = QLabel(self)
        self.pasto_inf.setPixmap(QPixmap(p.RUTA_PASTO))
        self.pasto_inf.setScaledContents(True)
        self.pasto_inf.setGeometry(20, 740, 1160, 50)

        #Label de pausa
        self.label_pausa = QLabel("JUEGO PAUSADO", self)
        self.label_pausa.setFont(QFont("Times", 20))
        self.label_pausa.setGeometry(500, 400, 230, 30)
        self.label_pausa.hide()
    
    #Inicia el sprite de la Rana
    def iniciar_rana(self):
        self.rana = QLabel("", self)
        self.rana.setPixmap(QPixmap(p.RUTA_RANA_UP1)) 
        self.rana.setScaledContents(True)
        self.rana.setGeometry(600, 750, p.WIDTH_RANA, p.HEIGHT_RANA)
        self.rana.setStyleSheet("border:1px solid black")
        self.rana.show()

    #Inicia el sprite de los autos
    def iniciar_autos(self, lista_autos):
        for auto in lista_autos:
            auto.inicializar_sprite(self)

    #Inicia el sprite de los troncos
    def iniciar_troncos(self, lista_troncos):
        for tronco in lista_troncos:
            tronco.inicializar_sprite(self)

    #Mueve los sprites de los autos
    def animar_autos(self, lista_autos):
        for auto in lista_autos:
            auto.sprite.move(auto.posicion[0], auto.posicion[1])

    #Mueve el sprite de los troncos
    def animar_troncos(self, lista_troncos):
        for tronco in lista_troncos:
            tronco.sprite.move(tronco.posicion[0], tronco.posicion[1])
    
    #Hace aparecer los objetos especiales en pantalla
    def mostrar_objeto(self, objeto):
        objeto.inicializar_sprite(self)
        self.lista_objetos_activos.append(objeto.sprite)

    #Elimina los objetos de la pantalla si estos son tomados
    def eliminar_objeto(self, index):
        self.lista_objetos_activos[index].hide()
        self.lista_objetos_activos.pop(index)
        print(self.lista_objetos_activos, "FRONTEND")
    
    def keyPressEvent(self, event):
        self.avanzar_rana(event.text())

    #Funcion que mueve el sprite de la rana
    #Tambien hace que se pause el juego con la letra p
    #Hace saltar a la rana con la letra j (jump)
    def avanzar_rana(self, event):
        if event == "w":
            self.rana.move(self.rana.pos() + QPoint(0, -1 * p.MOVIMIENTO))
        elif event == "a":
            self.rana.move(self.rana.pos() + QPoint(-1 * p.MOVIMIENTO, 0))
        elif event == "s":
            self.rana.move(self.rana.pos() + QPoint(0, p.MOVIMIENTO)) 
        elif event == "d":
            self.rana.move(self.rana.pos() + QPoint(p.MOVIMIENTO, 0))
        elif event == "j": #j va a ser el boton de salto
            self.rana.move(self.rana.pos() + QPoint(0, -1 * p.PIXELES_SALTO))
        elif event == "p":
            if not self.juego_pausado:
                self.senal_enviar_pausar_juego.emit()
                self.juego_pausado = True
                self.label_pausa.show()
            else:
                self.senal_enviar_despausar_juego.emit()
                self.juego_pausado = False
                self.label_pausa.hide()

        posicion = [self.rana.pos().x(), self.rana.pos().y()]
        self.senal_enviar_posicion_rana.emit(posicion)

    #Mueve el sprite de la rana si esta encima de un tronco
    def rana_en_tronco(self, direccion_tronco):
        self.rana.move(self.rana.pos() + QPoint(direccion_tronco * p.VELOCIDAD_TRONCOS, 0))

    #Reinicia la posicion de la rana si esta muere
    def reiniciar_posicion(self):
        self.rana.setGeometry(600, 750, p.WIDTH_RANA, p.HEIGHT_RANA)

    #Actualiza los datos que se ven en pantalla, gracias
    # a data que viene del backend
    def actualizar_datos(self, datos):
        self.vidas_label.setText(f"VIDAS: {datos['vidas']}")
        self.tiempo_label.setText(f"TIEMPO: {datos['tiempo'][:4]}")
        self.monedas_label.setText(f"MONEDAS: {datos['monedas']}")
        self.puntaje_label.setText(f"PUNTAJE: {datos['puntaje_total']}")
        self.nivel_label.setText(f"NIVEL: {datos['nivel_actual']}")

    #Esconde la ventana de juego
    def esconder(self):
        self.hide()

    #Muestra la ventana de juego
    #Y le asigna un titulo a la ventana dependiendo del nombre de usuario
    def mostrar(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.setWindowTitle(f"Ventana de Juego: Jugador ({self.nombre_usuario})")
        self.show()

    #Cierra la ventana de juego
    def salir(self):
        self.close()

    #Funcion para centrar la ventana, independiente del tamañano de la pantalla donde se muestre  
    # https://python-commandments.org/pyqt-center-window/
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
