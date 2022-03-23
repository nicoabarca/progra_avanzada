from PyQt5.QtCore import QLine, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))

        # COMPLETAR
        self.setGeometry(tamano_ventana)

        self.img_label = QLabel(self)
        ruta_img = p.RUTA_LOGO
        pixeles = QPixmap(ruta_img)
        self.img_label.setPixmap(pixeles)
        self.img_label.setScaledContents(True)
        self.img_label.setMaximumSize(400, 400)

        
        self.usuario_label = QLabel('Ingrese su usuario:', self)
        self.usuario_form = QLineEdit('', self)

        self.clave_label = QLabel('Ingrese su clave:', self)
        self.clave_form = QLineEdit('', self)
        self.clave_form.setEchoMode(QLineEdit.Password)

        self.ingresar_button = QPushButton('Ingresar', self) 
        self.ingresar_button.clicked.connect(self.enviar_login)

        hbox_usr = QHBoxLayout()
        hbox_usr.addWidget(self.usuario_label)
        hbox_usr.addWidget(self.usuario_form)

        hbox_pass = QHBoxLayout()
        hbox_pass.addWidget(self.clave_label)
        hbox_pass.addWidget(self.clave_form)

        vbox_usr_pass = QVBoxLayout()
        vbox_usr_pass.addStretch(5)
        vbox_usr_pass.addLayout(hbox_usr)
        vbox_usr_pass.addLayout(hbox_pass)

        vbox_button = QVBoxLayout()
        vbox_button.addStretch(5)
        vbox_button.addWidget(self.ingresar_button)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_usr_pass)
        hbox.addStretch(1)
        hbox.addLayout(vbox_button)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.img_label)
        vbox.addLayout(hbox)


        self.setLayout(vbox)

        self.agregar_estilo()

        self.show()

    def enviar_login(self):
        # COMPLETAR
        nombre_usuario = self.usuario_form.text()
        clave_usuario = self.clave_form.text()
        
        self.senal_enviar_login.emit((nombre_usuario, clave_usuario)) 
        #aca va el payload, que es tupla (nombre, pass)

    def agregar_estilo(self):
        # Acciones y señales
        self.clave_form.returnPressed.connect(
            lambda: self.ingresar_button.click()
        )  # Permite usar "ENTER" para iniciar sesión

        # Estilo extra
        self.setStyleSheet("background-color: #fdf600")
        self.usuario_form.setStyleSheet("background-color: #000000;"
                                        "border-radius: 5px;"
                                        "color: white")
        self.clave_form.setStyleSheet("background-color: #000000;"
                                      "border-radius: 5px;"
                                      "color: white")
        self.ingresar_button.setStyleSheet(p.stylesheet_boton)

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.ocultar()
        else:
            self.clave_form.setText("")
            self.clave_form.setPlaceholderText("Contraseña inválida!")

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
