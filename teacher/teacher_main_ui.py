# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 451)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 581, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 206, 71, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 51, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 30, 51, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(280, 10, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.id_label = QtWidgets.QLabel(self.tab)
        self.id_label.setGeometry(QtCore.QRect(100, 30, 161, 16))
        self.id_label.setText("")
        self.id_label.setObjectName("id_label")
        self.teacher_name_label = QtWidgets.QLabel(self.tab)
        self.teacher_name_label.setGeometry(QtCore.QRect(100, 90, 161, 16))
        self.teacher_name_label.setText("")
        self.teacher_name_label.setObjectName("teacher_name_label")
        self.room_name_label = QtWidgets.QLabel(self.tab)
        self.room_name_label.setGeometry(QtCore.QRect(100, 150, 161, 16))
        self.room_name_label.setText("")
        self.room_name_label.setObjectName("room_name_label")
        self.description_label = QtWidgets.QLabel(self.tab)
        self.description_label.setGeometry(QtCore.QRect(100, 210, 161, 111))
        self.description_label.setText("")
        self.description_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_label.setObjectName("description_label")
        self.start_button = QtWidgets.QPushButton(self.tab)
        self.start_button.setGeometry(QtCore.QRect(380, 120, 131, 31))
        self.start_button.setObjectName("start_button")
        self.exit_button = QtWidgets.QPushButton(self.tab)
        self.exit_button.setGeometry(QtCore.QRect(380, 230, 131, 31))
        self.exit_button.setObjectName("exit_button")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(40, 340, 51, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.capacity_label = QtWidgets.QLabel(self.tab)
        self.capacity_label.setGeometry(QtCore.QRect(100, 340, 161, 16))
        self.capacity_label.setText("")
        self.capacity_label.setObjectName("capacity_label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.material_edit = QtWidgets.QLineEdit(self.tab_2)
        self.material_edit.setGeometry(QtCore.QRect(40, 340, 401, 21))
        self.material_edit.setObjectName("material_edit")
        self.material_button = QtWidgets.QPushButton(self.tab_2)
        self.material_button.setGeometry(QtCore.QRect(450, 340, 91, 21))
        self.material_button.setObjectName("material_button")
        self.material_browser = QtWidgets.QTextBrowser(self.tab_2)
        self.material_browser.setGeometry(QtCore.QRect(40, 50, 501, 241))
        self.material_browser.setObjectName("material_browser")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.kick_button = QtWidgets.QPushButton(self.tab_3)
        self.kick_button.setGeometry(QtCore.QRect(450, 340, 91, 21))
        self.kick_button.setObjectName("kick_button")
        self.student_list = QtWidgets.QListWidget(self.tab_3)
        self.student_list.setGeometry(QtCore.QRect(40, 50, 501, 241))
        self.student_list.setObjectName("student_list")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Description:"))
        self.label_2.setText(_translate("Form", "Teacher:"))
        self.label_3.setText(_translate("Form", "Room name:"))
        self.label.setText(_translate("Form", "Room ID:"))
        self.start_button.setText(_translate("Form", "Start/Stop streaming"))
        self.exit_button.setText(_translate("Form", "Exit room"))
        self.label_5.setText(_translate("Form", "Capacity:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Main"))
        self.material_button.setText(_translate("Form", "Post"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Material"))
        self.kick_button.setText(_translate("Form", "Kick"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Viewer"))

