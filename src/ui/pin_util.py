from PyQt5 import QtCore, QtGui, QtWidgets
from .PINEntryWidget import Ui_PINEntryWidget

def pin_authorization(ctx, callback):
    ctx.__pin_window = QtWidgets.QMainWindow()
    ctx.__pin_widget = Ui_PINEntryWidget(ctx, callback)
    ctx.__pin_widget.setupUi(ctx.__pin_window)
    ctx.__pin_window.show()