# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NotificationWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotificationWidget(object):

    def __init__(self, ctx, add_buttons=False):
        self.ctx = ctx
        self.add_buttons = add_buttons

    def setupUi(self, NotificationWidget):
        if self.add_buttons:
            NotificationWidget.setObjectName("NotificationWidget")
            NotificationWidget.resize(276, 167)

        if self.add_buttons:
            self.ApproveButton = QtWidgets.QPushButton(NotificationWidget)
            self.ApproveButton.setGeometry(QtCore.QRect(190, 140, 83, 25))
            self.ApproveButton.setObjectName("ApproveButton")
            self.AlarmButton = QtWidgets.QPushButton(NotificationWidget)
            self.AlarmButton.setGeometry(QtCore.QRect(100, 140, 83, 25))
            self.AlarmButton.setObjectName("AlarmButton")

        self.NotificationText = QtWidgets.QLabel()
        
        if self.add_buttons:
            self.NotificationText.setGeometry(QtCore.QRect(10, 30, 261, 101))
        self.NotificationText.setAlignment(QtCore.Qt.AlignLeft)
        self.NotificationText.setObjectName("NotificationText")
        self.NotificationTimestamp = QtWidgets.QLabel()
        if self.add_buttons:
            self.NotificationTimestamp.setGeometry(QtCore.QRect(150, 0, 131, 21))
        self.NotificationTimestamp.setObjectName("NotificationTimestamp")
        self.NotificationType = QtWidgets.QLabel()
        self.NotificationType.setAlignment(QtCore.Qt.AlignCenter)
        if self.add_buttons:
            self.NotificationType.setGeometry(QtCore.QRect(0, 0, 64, 21))
        self.NotificationType.setObjectName("NotificationType")

        self.retranslateUi(NotificationWidget)
        if self.add_buttons:
            QtCore.QMetaObject.connectSlotsByName(NotificationWidget)

    def retranslateUi(self, NotificationWidget):
        _translate = QtCore.QCoreApplication.translate
        if self.add_buttons:
            NotificationWidget.setWindowTitle(_translate("NotificationWidget", "Incoming Notification"))

        if self.add_buttons:
            self.ApproveButton.setText(_translate("NotificationWidget", "Approve"))
            self.AlarmButton.setText(_translate("NotificationWidget", "Alarm"))

        self.NotificationText.setText(_translate("NotificationWidget", self.ctx['title']))
        self.NotificationTimestamp.setText(_translate("NotificationWidget", self.ctx['timestamp']))
        self.NotificationType.setText(_translate("NotificationWidget", self.ctx['type']))
