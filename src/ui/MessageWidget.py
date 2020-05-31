# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageWidget(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def setupUi(self, MessageWidget):
        MessageWidget.setObjectName("MessageWidget")
        MessageWidget.resize(273, 146)
        self.OKButton = QtWidgets.QPushButton(MessageWidget)
        self.OKButton.setGeometry(QtCore.QRect(190, 120, 80, 23))
        self.OKButton.setObjectName("OKButton")
        self.MessageText = QtWidgets.QLabel(MessageWidget)
        self.MessageText.setGeometry(QtCore.QRect(10, 10, 251, 101))
        self.MessageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MessageText.setAlignment(QtCore.Qt.AlignCenter)
        self.MessageText.setObjectName("MessageText")

        self.retranslateUi(MessageWidget)
        QtCore.QMetaObject.connectSlotsByName(MessageWidget)

    def retranslateUi(self, MessageWidget):
        _translate = QtCore.QCoreApplication.translate
        MessageWidget.setWindowTitle(_translate("MessageWidget", "/!\\ Warning"))
        self.OKButton.setText(_translate("MessageWidget", "OK"))
        self.MessageText.setText(_translate("MessageWidget", "Message Text"))

