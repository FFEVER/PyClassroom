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
        Form.resize(596, 377)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 571, 341))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.widget = QtWidgets.QWidget(self.mainTab)
        self.widget.setGeometry(QtCore.QRect(20, 20, 261, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.roomIDLabel = QtWidgets.QLabel(self.widget)
        self.roomIDLabel.setObjectName("roomIDLabel")
        self.horizontalLayout_2.addWidget(self.roomIDLabel)
        self.roomIDinfo = QtWidgets.QLabel(self.widget)
        self.roomIDinfo.setObjectName("roomIDinfo")
        self.horizontalLayout_2.addWidget(self.roomIDinfo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.courseNameLabel = QtWidgets.QLabel(self.widget)
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.horizontalLayout_3.addWidget(self.courseNameLabel)
        self.courseNameInfo = QtWidgets.QLabel(self.widget)
        self.courseNameInfo.setObjectName("courseNameInfo")
        self.horizontalLayout_3.addWidget(self.courseNameInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lecturerLabel = QtWidgets.QLabel(self.widget)
        self.lecturerLabel.setObjectName("lecturerLabel")
        self.horizontalLayout_6.addWidget(self.lecturerLabel)
        self.lecturerInfo = QtWidgets.QLabel(self.widget)
        self.lecturerInfo.setObjectName("lecturerInfo")
        self.horizontalLayout_6.addWidget(self.lecturerInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.descriptionLabel = QtWidgets.QLabel(self.widget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.horizontalLayout_5.addWidget(self.descriptionLabel)
        self.descriptionInfo = QtWidgets.QLabel(self.widget)
        self.descriptionInfo.setObjectName("descriptionInfo")
        self.horizontalLayout_5.addWidget(self.descriptionInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currentViewLabel = QtWidgets.QLabel(self.widget)
        self.currentViewLabel.setObjectName("currentViewLabel")
        self.horizontalLayout_4.addWidget(self.currentViewLabel)
        self.currentViewInfo = QtWidgets.QLabel(self.widget)
        self.currentViewInfo.setObjectName("currentViewInfo")
        self.horizontalLayout_4.addWidget(self.currentViewInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.pushButton_4 = QtWidgets.QPushButton(self.streamTab)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 0, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget1 = QtWidgets.QWidget(self.streamTab)
        self.widget1.setGeometry(QtCore.QRect(370, 40, 181, 261))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget1)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.streamWidget = QtWidgets.QWidget(self.streamTab)
        self.streamWidget.setGeometry(QtCore.QRect(40, 40, 291, 251))
        self.streamWidget.setObjectName("streamWidget")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("eyeicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.streamTab, icon2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.roomIDLabel.setText(_translate("Form", "Room ID:"))
        self.roomIDinfo.setText(_translate("Form", "-"))
        self.courseNameLabel.setText(_translate("Form", "Course Name: "))
        self.courseNameInfo.setText(_translate("Form", "-"))
        self.lecturerLabel.setText(_translate("Form", "Lecturer: "))
        self.lecturerInfo.setText(_translate("Form", "-"))
        self.descriptionLabel.setText(_translate("Form", "Description:"))
        self.descriptionInfo.setText(_translate("Form", "-"))
        self.currentViewLabel.setText(_translate("Form", "Current Viewers: "))
        self.currentViewInfo.setText(_translate("Form", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("Form", "Main"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.mainTab), _translate("Form", "Main Page"))
        self.label_6.setText(_translate("Form", "Post something! "))
        self.pushButton_2.setText(_translate("Form", "Attach a file .. "))
        self.pushButton.setText(_translate("Form", "Post"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.materialsTab), _translate("Form", "Materials"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.materialsTab), _translate("Form", "Materials"))
        self.pushButton_4.setText(_translate("Form", "Leave Room"))
        self.pushButton_3.setText(_translate("Form", "send"))
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

