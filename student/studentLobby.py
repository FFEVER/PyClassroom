import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.lobbystudent import Ui_Form
from studentMain import StudentMain


class StudentLobby(QtWidgets.QMainWindow): 
    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self, None) 
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        
        self.ui.searchButton.clicked.connect(self.searchClicked) 
        self.ui.refreshButton.clicked.connect(self.refreshClicked) 
        self.ui.joinButton.clicked.connect(self.joinClicked) 
        self.model = QtGui.QStandardItemModel(self.ui.listView) 

        self.allCourses = None

        
    
    def updateRoomList(self): 
        for course in self.allCourses: 
            courseString = course.id + " " + course.name + " " + course.teacher.name 
            item = QtGui.QStandardItem(courseString) 
            item.setCheckable(False) 
            self.model.appendRow(item) 
        
        self.ui.listView.setModel(self.model) 
        
        
    def setRoomList(self, roomList): 
        self.allCourses = roomList

    def joinClicked(self): 
        index = QtCore.QModelIndex()
        index = self.ui.listView.currentIndex() 

        if index == -1:
            return

        #selected course from the listView 
        self.selectedCourse = self.model.itemFromIndex(index).text()
        tosend = self.selectedCourse.split(' ')

        i = 0
        #avoiding empty key
        while True: 
            
            if not tosend[i] == '': 
                break
            i += 1
         
        #use tosend[i] to represent the Room ID 
        #and open StudentMain 
        self.hide() 
        print("tosend[i] = " + tosend[i]) 
        self.nextPage = StudentMain(tosend[i]) 
        self.nextPage.show() 
        




        


        
    def searchClicked(self): 
        filter_text = str(self.ui.searchBox.text()).lower() 
        for row in range(self.model.rowCount()):
            if filter_text in str(self.model.item(row).text()).lower(): 
                self.ui.listView.setRowHidden(row, False) 
            else: 
                self.ui.listView.setRowHidden(row, True) 
            
        
    def refreshClicked(self): 
        #show all courses available 
        for row in range(self.model.rowCount()): 
            self.ui.listView.setRowHidden(row,False) 
       


          