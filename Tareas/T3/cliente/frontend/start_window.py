import os
from PyQt5.QtCore import QLine, pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (
    QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDesktopWidget
)
from utils import get_json_data


class StartWindow(QWidget):

    verify_login_signal = pyqtSignal(tuple)

    
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        
        self.setWindowTitle("Ventana de Inicio")
        self.setStyleSheet("background-color:black")
        self.setFixedSize(600, 500)
        self.center()

        self.title_label = QLabel("¿Te atreves a jugar?", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color:white")
        self.title_label.setFont(QFont("Arial", 20))
        
        ruta_img = os.path.join(*get_json_data("path_logo_blanco"))

        self.logo_img = QLabel(self)
        self.logo_img.setPixmap(QPixmap(ruta_img))
        self.logo_img.setScaledContents(True)

        self.name_label = QLabel("Escribe tu nombre de usuario (alfanumérico)", self)
        self.name_form = QLineEdit("", self)
        self.name_label.setStyleSheet("color:white")
        self.name_form.setStyleSheet("background-color:white; border: 1px solid #E600E7")

        self.date_label = QLabel("Fecha de nacimiento", self)
        self.date_form = QLineEdit("", self)
        self.date_label.setStyleSheet("color:white")
        self.date_form.setStyleSheet("background-color:white; border: 1px solid #E600E7")

        self.sign_button = QPushButton("Firmar", self)
        self.sign_button.setStyleSheet("background-color:white")
        self.sign_button.setAutoDefault(True)
        self.sign_button.clicked.connect(self.send_login_verification)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.logo_img)
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_form)
        vbox.addStretch(1)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.date_form)
        vbox.addStretch(1)
        vbox.addWidget(self.sign_button)

        self.setLayout(vbox)

    #Send login data to backend
    def send_login_verification(self):
        user_name = self.name_form.text()
        birth_date = self.date_form.text()
        
        self.verify_login_signal.emit((user_name, birth_date))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
