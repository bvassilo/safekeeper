# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(424, 254)
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ActivityLogButton = QtWidgets.QPushButton(self.centralwidget)
        self.ActivityLogButton.setGeometry(QtCore.QRect(10, 20, 131, 23))
        self.ActivityLogButton.setObjectName("ActivityLogButton")
        self.DroneControlButton = QtWidgets.QPushButton(self.centralwidget)
        self.DroneControlButton.setGeometry(QtCore.QRect(10, 140, 131, 23))
        self.DroneControlButton.setObjectName("DroneControlButton")
        self.InsertUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.InsertUserButton.setGeometry(QtCore.QRect(10, 60, 131, 23))
        self.InsertUserButton.setObjectName("InsertUserButton")
        self.DeleteUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteUserButton.setGeometry(QtCore.QRect(10, 100, 131, 23))
        self.DeleteUserButton.setObjectName("DeleteUserButton")
        self.IncidentSubmissionButton = QtWidgets.QPushButton(self.centralwidget)
        self.IncidentSubmissionButton.setGeometry(QtCore.QRect(10, 180, 131, 23))
        self.IncidentSubmissionButton.setObjectName("IncidentSubmissionButton")
        self.SilentAlarmButton = QtWidgets.QPushButton(self.centralwidget)
        self.SilentAlarmButton.setGeometry(QtCore.QRect(10, 220, 131, 23))
        self.SilentAlarmButton.setObjectName("SilentAlarmButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 40, 256, 171))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.LatestIncidentsText = QtWidgets.QLabel(self.centralwidget)
        self.LatestIncidentsText.setGeometry(QtCore.QRect(160, 20, 131, 21))
        self.LatestIncidentsText.setObjectName("LatestIncidentsText")
        self.IncidentNumberText = QtWidgets.QLabel(self.centralwidget)
        self.IncidentNumberText.setGeometry(QtCore.QRect(160, 221, 251, 20))
        self.IncidentNumberText.setObjectName("IncidentNumberText")
        MainMenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "Safeguard"))
        self.ActivityLogButton.setText(_translate("MainMenuWindow", "Activity Log"))
        self.DroneControlButton.setText(_translate("MainMenuWindow", "Drone Control"))
        self.InsertUserButton.setText(_translate("MainMenuWindow", "Insert User"))
        self.DeleteUserButton.setText(_translate("MainMenuWindow", "Delete User"))
        self.IncidentSubmissionButton.setText(_translate("MainMenuWindow", "Incident Submission"))
        self.SilentAlarmButton.setText(_translate("MainMenuWindow", "Silent Alarm"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainMenuWindow", "ena"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.LatestIncidentsText.setText(_translate("MainMenuWindow", "Latest Incidents:"))
        self.IncidentNumberText.setText(_translate("MainMenuWindow", "# Incidents"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()
    sys.exit(app.exec_())
