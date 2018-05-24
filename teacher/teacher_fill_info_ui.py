# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_fill_info.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 323)
        Form.setMinimumSize(QtCore.QSize(395, 323))
        Form.setMaximumSize(QtCore.QSize(395, 323))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 61, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 270, 47, 13))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.teacher_name_edit = QtWidgets.QLineEdit(Form)
        self.teacher_name_edit.setGeometry(QtCore.QRect(100, 30, 261, 20))
        self.teacher_name_edit.setObjectName("teacher_name_edit")
        self.room_name_edit = QtWidgets.QLineEdit(Form)
        self.room_name_edit.setGeometry(QtCore.QRect(100, 70, 261, 20))
        self.room_name_edit.setObjectName("room_name_edit")
        self.capacity_edit = QtWidgets.QLineEdit(Form)
        self.capacity_edit.setGeometry(QtCore.QRect(100, 270, 51, 20))
        self.capacity_edit.setObjectName("capacity_edit")
        self.create_button = QtWidgets.QPushButton(Form)
        self.create_button.setGeometry(QtCore.QRect(290, 270, 75, 23))
        self.create_button.setObjectName("create_button")
        self.description_edit = QtWidgets.QTextEdit(Form)
        self.description_edit.setGeometry(QtCore.QRect(100, 120, 261, 121))
        self.description_edit.setObjectName("description_edit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "Room name"))
        self.label_3.setText(_translate("Form", "Description"))
        self.label_4.setText(_translate("Form", "Capacity"))
        self.create_button.setText(_translate("Form", "Create"))
        self.description_edit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

