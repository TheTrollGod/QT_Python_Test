#!/bin/env python

#import system
import sys
#import random
import random
#import modules from pyside6
from PySide6 import QtCore, QtWidgets, QtGui
#import pyautogui for automated keyboard mouse interactions
import pyautogui


#creates the windows class
class first_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #class veriable "hello"
        self.hello = ["Hello!", "Hallo!", "Hola!", "Hei!"]
        #create a button
        self.button1 = QtWidgets.QPushButton("Click ME!")

        #creates text with allignemnt
        #can be used to display html
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
       
       #Sets title
        self.setWindowTitle("First Window")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        self.button1.clicked.connect(self.display)
        self.button2.clicked.connect(self.colour_change)

    #slots allow widgets to communicate with other widgets
    @QtCore.Slot()
    def display(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    #creates the Qapplication instance; Able to pass any command line args into it
    #in order to print to command line, you must use sys.argv in the Qapp
    app = QtWidgets.QApplication([])

    widget = first_window()
    widget.resize(800, 600)
    
    #Makes the app actually open
    widget.show()

    #Makes the app stay open when ran
    sys.exit(app.exec())