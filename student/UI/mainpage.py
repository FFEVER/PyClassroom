# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 335)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(12, 12, 422, 311))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.mainTab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.mainTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.mainTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.mainTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("homeicon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.mainTab, icon, "")
        self.materialsTab = QtWidgets.QWidget()
        self.materialsTab.setObjectName("materialsTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.materialsTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.materialsTab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.textEdit = QtWidgets.QTextEdit(self.materialsTab)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.materialsTab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.materialsTab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bookicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.materialsTab, icon1, "")
        self.streamTab = QtWidgets.QWidget()
        self.streamTab.setObjectName("streamTab")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("eyeicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.streamTab, icon2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Room ID:"))
        self.label.setText(_translate("Form", "Course Name: "))
        self.label_3.setText(_translate("Form", "Lecturer: "))
        self.label_4.setText(_translate("Form", "Description:"))
        self.label_5.setText(_translate("Form", "Current Viewers: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("Form", "Main"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.mainTab), _translate("Form", "Main Page"))
        self.label_6.setText(_translate("Form", "Post something! "))
        self.pushButton_2.setText(_translate("Form", "Attach a file .. "))
        self.pushButton.setText(_translate("Form", "Post"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.materialsTab), _translate("Form", "Materials"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.materialsTab), _translate("Form", "Materials"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.streamTab), _translate("Form", "Stream"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.streamTab), _translate("Form", "Watch Stream"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

