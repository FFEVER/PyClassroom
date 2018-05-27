# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectrole.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 334)
        self.indicatorLabel = QtWidgets.QLabel(Form)
        self.indicatorLabel.setGeometry(QtCore.QRect(190, 80, 81, 21))
        self.indicatorLabel.setStyleSheet("font: 18pt \"Avenir\";")
        self.indicatorLabel.setObjectName("indicatorLabel")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 150, 411, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teacherButton = QtWidgets.QPushButton(self.layoutWidget)
        self.teacherButton.setStyleSheet("")
        self.teacherButton.setObjectName("teacherButton")
        self.horizontalLayout.addWidget(self.teacherButton)
        self.studentButton = QtWidgets.QPushButton(self.layoutWidget)
        self.studentButton.setStyleSheet("")
        self.studentButton.setObjectName("studentButton")
        self.horizontalLayout.addWidget(self.studentButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.indicatorLabel.setText(_translate("Form", "You are a: "))
        self.teacherButton.setText(_translate("Form", "Teacher"))
        self.studentButton.setText(_translate("Form", "Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

