import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QFont
import re

from scan_project.sec_scan import *
class window2(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'scanning....!'
        #self.setStyleSheet("Background-color:green")
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(600, 300)


        self.lbl = QLabel('First name', self)
        self.lbl.move(180, 30)
        self.lbl.setFont(QFont("Arial",12))

        self.lbl2 = QLabel('Email', self)
        self.lbl2.move(180, 68)
        self.lbl2.setFont(QFont("Arial", 12))

        self.lbl3 = QLabel('Company', self)
        self.lbl3.move(180, 105)
        self.lbl3.setFont(QFont("Arial", 12))

        self.lbl4 = QLabel('Password', self)
        self.lbl4.move(180, 146)
        self.lbl4.setFont(QFont("Arial", 12))

        self.lbl5 = QLabel('Confirm Password', self)
        self.lbl5.move(180, 190)
        self.lbl5.resize(200,25)
        self.lbl5.setFont(QFont("Arial", 12))

        # Create textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(340, 30)
        self.textbox1.resize(220, 25)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(340, 70)
        self.textbox2.resize(220, 25)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(340, 110)
        self.textbox3.resize(220, 25)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(340, 150)
        self.textbox4.resize(220, 25)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(340, 190)
        self.textbox5.resize(220, 25)

        # Create a button in the window
        self.button1 = QPushButton('Register', self)
        self.button1.move(340, 240)
        self.button1.clicked.connect(self.on_click)

        self.button = QPushButton('clear', self)
        self.button.move(460, 240)
        self.button.clicked.connect(self.clear_all)
        self.show()

    def on_click(self):
        self.w = Licencekey(self)
        #self.w.setStyleSheet("Background-color:yellow")
        self.w.show()

        # self.label = QLabel('authotication key', self)
        # self.label.move(50, 340)
        # self.label.setFont(QFont("Arial", 12))

        # self.text1 = QLineEdit(self)
        # self.text1.move(100, 340)
        # self.text1.resize(220, 25)
        # self.show()

    def clear_all(self):
        first = self.textbox1.clear()
        last = self.textbox2.clear()
        mail = self.textbox3.clear()
        mob = self.textbox4.clear()
        pasw = self.textbox5.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window2()
    sys.exit(app.exec_())
