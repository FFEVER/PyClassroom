# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 320)
        self.text_browser = QtWidgets.QTextBrowser(Form)
        self.text_browser.setGeometry(QtCore.QRect(10, 10, 221, 301))
        self.text_browser.setObjectName("text_browser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

