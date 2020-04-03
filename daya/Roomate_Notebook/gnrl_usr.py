from PyQt5.QtWidgets import (QMessageBox, QLineEdit, QComboBox, QLabel, QPushButton, QWidget, QDialog)

from PyQt5.QtGui import QFont, QDoubleValidator
import os

class gnrlusr(QDialog):

    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setWindowTitle("General User")
        self.setFixedSize(800,400)


        self.cmb_bx()





    def cmb_bx(self):
        cmb = QComboBox(self)
        cmb.setFixedSize(100,30)
        cmb.move(100,50)
        itm = "Item"

        cmb.addItems(self.get_files())
        #cmb.show()

        #cmb.addItem(name)

    def get_files(self):
        files = []
        try:
            for file in os.listdir(os.getcwd()):
                files.append(file)
            return files
        except:
            return files


    # Function for all input boxes
    def in_box(self,w=250,h=30,x=210,y=50,echo_mode=False,place_hldr=''):
        inp = QLineEdit(self)
        inp.setFixedSize(w,h)
        inp.move(x,y)
        inp.setPlaceholderText(place_hldr)
        inp.setFont(QFont("Times New Roman",14))
        if echo_mode:
            inp.setValidator(QDoubleValidator(0.99,99.99,2))
        return inp

    # Function for all labels
    def lbl(self,name,w=400,h=30,x=20,y=20):
        Lbl = QLabel(name,self)
        Lbl.setFixedSize(w,h)
        Lbl.move(x,y)
        Lbl.setFont(QFont("Times New Roman",16))


    # Function for button
    def btn(self,name,x=540,y=130,function=QPushButton.close):
        Btn = QPushButton(name,self)
        Btn.setFixedSize(100,30)
        Btn.move(x,y)
        Btn.setFont(QFont("Times New Roman",14))
        if Btn:
            Btn.clicked.connect(function)

    def msg_box(self,Msg,ms_type):
        try:
            Msg_bx = QMessageBox(self)
            Msg_bx.setFixedSize(300,200)
            Msg_bx.setWindowTitle(ms_type)
            Msg_bx.setFont(QFont("Times New Roman",15))
            Msg_bx.setText(Msg)
            Msg_bx.show()
        except:
            pass
