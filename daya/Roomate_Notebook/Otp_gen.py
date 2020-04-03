from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit)
import sys
from PyQt5.QtGui import QFont


class Otp_window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("NEW PASSWORD...")
        self.setFixedSize(600,300)
        # self.btn("Enter",function=self.regster)

        #label section

        self.lbl("New password")
        self.lbl("Re-Password",y=100)
        self.lbl("OTP",y=18)

        # Box section

        self.in1=self.in_box(y=65,place_hldr="Enter Username")
        self.in2=self.in_box(y=110,place_hldr="Enter Password",p_mode=True)
        self.in2=self.in_box(y=25,place_hldr="Enter OTP")


    #Button section
        self.btn("login",function=self.user_login)
        self.btn("close",x=335,y=160)
        self.show()


    def lbl(self,name,x=50,y=57):
        lb=QLabel(name,self)
        lb.setFixedSize(130,50)
        lb.setFont(QFont("Time New Roman",14))
        lb.move(x,y)

    def in_box(self,x=200,y=65,place_hldr="place holder",p_mode=False):
        inp=QLineEdit(self)
        inp.setFixedSize(235,30)
        inp.move(x,y)
        if p_mode:
            inp.setEchoMode(inp.Password)
        inp.setPlaceholderText(place_hldr)
        inp.setFont(QFont("Time New Roman",16))
        return inp

    def btn(self,name,w=100,h=30,x=200,y=160,function=QPushButton.close):
        bt=QPushButton(name,self)
        bt.setFixedSize(w,h)
        bt.move(x,y)
        bt.setFont(QFont("Time New Roman",14))
        bt.clicked.connect(function)
        return bt

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


    def user_login(self):
        pass

    def user_register(self):
        pass





