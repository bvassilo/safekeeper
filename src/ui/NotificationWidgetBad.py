# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NotificationWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotificationWidgetBad(object):
    def setupUi(self, NotificationWidget):
        NotificationWidget.setObjectName("NotificationWidget")
        NotificationWidget.resize(276, 167)
        self.ApproveButton = QtWidgets.QPushButton(NotificationWidget)
        self.ApproveButton.setGeometry(QtCore.QRect(190, 140, 83, 25))
        self.ApproveButton.setObjectName("ApproveButton")
        self.AlarmButton = QtWidgets.QPushButton(NotificationWidget)
        self.AlarmButton.setGeometry(QtCore.QRect(100, 140, 83, 25))
        self.AlarmButton.setObjectName("AlarmButton")
        self.NotificationText = QtWidgets.QLabel(NotificationWidget)
        self.NotificationText.setGeometry(QtCore.QRect(10, 30, 261, 101))
        self.NotificationText.setAlignment(QtCore.Qt.AlignCenter)
        self.NotificationText.setObjectName("NotificationText")
        self.NotificationTimestamp = QtWidgets.QLabel(NotificationWidget)
        self.NotificationTimestamp.setGeometry(QtCore.QRect(150, 0, 131, 21))
        self.NotificationTimestamp.setObjectName("NotificationTimestamp")
        self.NotificationType = QtWidgets.QLabel(NotificationWidget)
        self.NotificationType.setGeometry(QtCore.QRect(0, 0, 64, 21))
        self.NotificationType.setObjectName("NotificationType")

        self.retranslateUi(NotificationWidget)
        QtCore.QMetaObject.connectSlotsByName(NotificationWidget)

    def retranslateUi(self, NotificationWidget):
        _translate = QtCore.QCoreApplication.translate
        NotificationWidget.setWindowTitle(_translate("NotificationWidget", "/!\\ Notification"))
        self.ApproveButton.setText(_translate("NotificationWidget", "Approve"))
        self.AlarmButton.setText(_translate("NotificationWidget", "Alarm"))
        self.NotificationText.setText(_translate("NotificationWidget", "Notification Text"))
        self.NotificationTimestamp.setText(_translate("NotificationWidget", "DD/MM/YYYY HH:MM"))
        self.NotificationType.setText(_translate("NotificationWidget", "Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NotificationWidget = QtWidgets.QWidget()
    ui = Ui_NotificationWidget()
    ui.setupUi(NotificationWidget)
    NotificationWidget.show()
    sys.exit(app.exec_())
