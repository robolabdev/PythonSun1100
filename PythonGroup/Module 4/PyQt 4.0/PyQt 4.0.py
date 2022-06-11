#PyQt 4.0 
#work with files READ and WRITE
#presentation link https://docs.google.com/presentation/d/1bdxF5J2j9vmLCPbtVkgYI_0DsI1r05Yv_gwBHwv0ypk/edit?usp=sharing

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QLineEdit,QComboBox 
import sys
import os
 

class ReaderView(QMainWindow):  

    def __init__(self,myViewModel): 
        super(ReaderView,self).__init__()     
        self.myViewModel = myViewModel                       
        self.setGeometry(0,0,600,600)                                        
        self.setWindowTitle("Poem reader") 
        self.poemSelectField              = self.CreateComboBox("Poem:",    150,25)     
        self.poemSelectField.addItems(["WILLIAM SHAKESPEARE","RUDYARD KIPLING"])
        self.poemField              = self.CreateLabel("POEM NOT LOADED",150,100)
        self.getPoembtn             = self.CreateButton("Get poem",      150,500, self.RequestPoem) 

    def RequestPoem(self):
        self.poemString = self.myViewModel.SetPath(self.poemSelectField.currentText())   
        self.UpdateUI()
    
    def CreateLabel(self,text,x,y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x,y)
        return newLabel

    def CreateComboBox(self,label,x,y):
        offsetForInputField = 50
        self.CreateLabel(label,x,y)
        combo = QComboBox(self) 
        combo.move(x+offsetForInputField, y)
        combo.resize(200, 32)
        return combo

    def CreateButton(self,text,x,y,fun):
        newButton = QtWidgets.QPushButton(self)
        newButton.setText(text)
        newButton.resize(250, 50)
        newButton.move(x,y)
        newButton.clicked.connect(fun) 
        return newButton

    def UpdateUI(self):
        self.poemField.setText("")
        total = ""
        lineOffset = 25 
        for x in self.poemString: 
            total += x  + "\n"  
        self.poemField.resize(500,lineOffset * len(self.poemString))
        self.poemField.setText(total)

class ReaderModelView(): 

    def SetPath(self,path):
        currentFilePath     = os.path.dirname(__file__)                  
        poemFilePath = currentFilePath + "/" + path + ".txt"
        return self.GetPoemFromModel(poemFilePath)

    def GetPoemFromModel(self,path):
        return ReaderModel.GetPoem(path)

class ReaderModel():  
    def GetPoem(path):
        poem = list() 
        f = open(path, "r")
        for x in f:
            poem.append(x)
        return poem







app = QApplication(sys.argv)  
myModel = ReaderModel()
myViewModel = ReaderModelView()
myView = ReaderView(myViewModel) 
myView.show()
sys.exit(app.exec_())