import sys
from ui import Ui_MainMenuWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from context import Context

if __name__ == '__main__':
    ctx = Context()

    app = QApplication(sys.argv)
    MainMenuWindow = QMainWindow()
    ui = Ui_MainMenuWindow(ctx)
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()

    sys.exit(app.exec_())