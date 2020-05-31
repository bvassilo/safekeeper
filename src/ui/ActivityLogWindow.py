# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActivityLogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ActivityLogWindow(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def setupUi(self, ActivityLogWindow):
        ActivityLogWindow.setObjectName("ActivityLogWindow")
        ActivityLogWindow.resize(655, 228)
        self.centralwidget = QtWidgets.QWidget(ActivityLogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IncidentsListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.IncidentsListWidget.setGeometry(QtCore.QRect(290, 30, 361, 161))
        self.IncidentsListWidget.setObjectName("IncidentsListWidget")
        item = QtWidgets.QListWidgetItem()
        self.IncidentsListWidget.addItem(item)
        self.IncidentsText = QtWidgets.QLabel(self.centralwidget)
        self.IncidentsText.setGeometry(QtCore.QRect(290, 10, 71, 20))
        self.IncidentsText.setObjectName("IncidentsText")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 281, 181))
        self.groupBox.setObjectName("groupBox")
        self.TypeText = QtWidgets.QLabel(self.groupBox)
        self.TypeText.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.TypeText.setObjectName("TypeText")
        self.TypeInput = QtWidgets.QLineEdit(self.groupBox)
        self.TypeInput.setGeometry(QtCore.QRect(90, 30, 181, 23))
        self.TypeInput.setObjectName("TypeInput")
        self.IncidentIDInput = QtWidgets.QLineEdit(self.groupBox)
        self.IncidentIDInput.setGeometry(QtCore.QRect(90, 60, 181, 23))
        self.IncidentIDInput.setObjectName("IncidentIDInput")
        self.IncidentIDText = QtWidgets.QLabel(self.groupBox)
        self.IncidentIDText.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.IncidentIDText.setObjectName("IncidentIDText")
        self.FromText = QtWidgets.QLabel(self.groupBox)
        self.FromText.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.FromText.setObjectName("FromText")
        self.FromInput = QtWidgets.QLineEdit(self.groupBox)
        self.FromInput.setGeometry(QtCore.QRect(90, 90, 181, 23))
        self.FromInput.setObjectName("FromInput")
        self.ToText = QtWidgets.QLabel(self.groupBox)
        self.ToText.setGeometry(QtCore.QRect(10, 120, 21, 21))
        self.ToText.setObjectName("ToText")
        self.ToInput = QtWidgets.QLineEdit(self.groupBox)
        self.ToInput.setGeometry(QtCore.QRect(90, 120, 181, 23))
        self.ToInput.setObjectName("ToInput")
        self.RFIDInput = QtWidgets.QLineEdit(self.groupBox)
        self.RFIDInput.setGeometry(QtCore.QRect(90, 150, 181, 23))
        self.RFIDInput.setObjectName("RFIDInput")
        self.RFIDText = QtWidgets.QLabel(self.groupBox)
        self.RFIDText.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.RFIDText.setObjectName("RFIDText")
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(570, 200, 80, 23))
        self.OKButton.setObjectName("OKButton")
        self.IncidentNumberText = QtWidgets.QLabel(self.centralwidget)
        self.IncidentNumberText.setGeometry(QtCore.QRect(290, 200, 271, 21))
        self.IncidentNumberText.setObjectName("IncidentNumberText")
        self.ApplyFiltersButton = QtWidgets.QPushButton(self.centralwidget)
        self.ApplyFiltersButton.setGeometry(QtCore.QRect(200, 200, 80, 23))
        self.ApplyFiltersButton.setObjectName("ApplyFiltersButton")
        self.groupBox.raise_()
        self.IncidentsListWidget.raise_()
        self.IncidentsText.raise_()
        self.OKButton.raise_()
        self.IncidentNumberText.raise_()
        self.ApplyFiltersButton.raise_()
        ActivityLogWindow.setCentralWidget(self.centralwidget)
        self.actionDate = QtWidgets.QAction(ActivityLogWindow)
        self.actionDate.setObjectName("actionDate")
        self.actionType = QtWidgets.QAction(ActivityLogWindow)
        self.actionType.setObjectName("actionType")
        self.actionLevel = QtWidgets.QAction(ActivityLogWindow)
        self.actionLevel.setObjectName("actionLevel")

        self.retranslateUi(ActivityLogWindow)
        QtCore.QMetaObject.connectSlotsByName(ActivityLogWindow)

    def retranslateUi(self, ActivityLogWindow):
        _translate = QtCore.QCoreApplication.translate
        ActivityLogWindow.setWindowTitle(_translate("ActivityLogWindow", "Activity Log"))
        __sortingEnabled = self.IncidentsListWidget.isSortingEnabled()
        self.IncidentsListWidget.setSortingEnabled(False)
        item = self.IncidentsListWidget.item(0)
        item.setText(_translate("ActivityLogWindow", "ena"))
        self.IncidentsListWidget.setSortingEnabled(__sortingEnabled)
        self.IncidentsText.setText(_translate("ActivityLogWindow", "Incidents:"))
        self.groupBox.setTitle(_translate("ActivityLogWindow", "Filters..."))
        self.TypeText.setText(_translate("ActivityLogWindow", "Type:"))
        self.IncidentIDText.setText(_translate("ActivityLogWindow", "Incident ID:"))
        self.FromText.setText(_translate("ActivityLogWindow", "From:"))
        self.ToText.setText(_translate("ActivityLogWindow", "To:"))
        self.RFIDText.setText(_translate("ActivityLogWindow", "RFID Card:"))
        self.OKButton.setText(_translate("ActivityLogWindow", "OK"))
        self.IncidentNumberText.setText(_translate("ActivityLogWindow", "# Incidents"))
        self.ApplyFiltersButton.setText(_translate("ActivityLogWindow", "Apply"))
        self.actionDate.setText(_translate("ActivityLogWindow", "Date"))
        self.actionType.setText(_translate("ActivityLogWindow", "Type"))
        self.actionLevel.setText(_translate("ActivityLogWindow", "Level"))
