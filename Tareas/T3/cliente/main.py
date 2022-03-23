import sys

from PyQt5.QtWidgets import QApplication

from backend.start_window_logic import StartWindowLogic

from frontend.start_window import StartWindow

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])

    #Initialize Windows
    start_window = StartWindow()
    #Initialize Windows Logic
    start_window_logic = StartWindowLogic()

    #Signal Connection

    #Send login data to the backend
    start_window.verify_login_signal.connect(
        start_window_logic.login_verification_to_server
    )

    start_window.show()

    sys.exit(app.exec_())