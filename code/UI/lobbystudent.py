# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lobbystudent.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 329)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 391, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filter = QtWidgets.QComboBox(self.layoutWidget)
        self.filter.setObjectName("filter")
        self.filter.addItem("")
        self.filter.addItem("")
        self.horizontalLayout_2.addWidget(self.filter)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.searchBox = QtWidgets.QLineEdit(self.layoutWidget)
        self.searchBox.setObjectName("searchBox")
        self.horizontalLayout_2.addWidget(self.searchBox)
        self.searchButton = QtWidgets.QPushButton(self.layoutWidget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.refreshButton = QtWidgets.QPushButton(self.layoutWidget)
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayout_2.addWidget(self.refreshButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(self.layoutWidget)
        self.table.setColumnCount(3)
        self.table.setObjectName("table")
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.table)
        self.joinButton = QtWidgets.QPushButton(self.layoutWidget)
        self.joinButton.setObjectName("joinButton")
        self.verticalLayout.addWidget(self.joinButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.filter.setItemText(0, _translate("Form", "Search By ID"))
        self.filter.setItemText(1, _translate("Form", "Search By Name"))
        self.label.setText(_translate("Form", ":"))
        self.searchButton.setText(_translate("Form", "Search"))
        self.refreshButton.setText(_translate("Form", "refresh"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Course Name"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Teacher"))
        self.joinButton.setText(_translate("Form", "Join Now"))

