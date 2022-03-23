from PyQt5.QtCore import QObject, pyqtSignal
from backend.player import Player

class StartWindowLogic(QObject):

    def __init__(self):
        super().__init__()

    #Send login data to the server
    def login_verification_to_server(self, user_data):
        user_name, birth_date = user_data
        player = Player(user_name, birth_date)
        player.send_login_verification_to_server(user_name, birth_date)