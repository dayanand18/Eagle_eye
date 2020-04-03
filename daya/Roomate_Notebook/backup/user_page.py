from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox)

from roomate_db import *
from PyQt5.QtGui import QFont, QDoubleValidator
from file_read import *


class user_win(QMainWindow):
    def __init__(self,user):
        super().__init__()
        self.setWindowTitle("Shashi-project for roomates")
        self.setFixedSize(800,400)
        self.incr = 130
        self.umail = user
        self.cnt = 1
        self.entered = []
        self.dbr = rommate_db()
        self.user_data = self.dbr.search_user(user)[0]
        Last_login = str(datetime.now()).split('.')[0]
        self.dbr.update_user(user,'last_login',str(Last_login))
        self.unm,self.ucmp,self.urole,self.ulast_log = self.user_data[1],self.user_data[2],self.user_data[4],self.user_data[5]


        self.lbl('Welcome : '+ str(self.unm))
        self.lbl('Last Login on : '+ str(self.ulast_log),x=450)

        self.lbl('Item Description',w=250,x=100,y=100)
        self.lbl('Item Price',w=150,x=430,y=100)

        self.a = self.in_box(w=310,x=100,y=130,place_hldr=" Item Description")
        self.b = self.in_box(w=100,x=430,y=130,place_hldr=" Price",echo_mode=True)
        self.entered.append((self.a,self.b))
        self.btn('+',function=self.plus_btn)
        self.btn("Save Data",x=700,y=360,function=self.save_data)



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

    def plus_btn(self):

        self.incr += 40
        if self.cnt < 6:
            self.item = self.in_box(w=310,x=100,y=self.incr,place_hldr=" Item Description")
            self.price = self.in_box(w=100,x=430,y=self.incr,place_hldr=" Price",echo_mode=True)
            self.entered.append((self.item,self.price))
            self.item.show()
            self.price.show()
            self.cnt += 1

    def save_data(self):
        msg = "Input must be required...!"
        Msg_type = "Alert...!"
        try:
            if self.entered:
                for itm_bx, prc_bx in self.entered:
                    if len(itm_bx.text()) > 0 and len(prc_bx.text()) > 0:
                        sav_res = save_file(str(self.umail),itm_bx.text(),prc_bx.text())
                        itm_bx.clear();prc_bx.clear()
                        if sav_res:
                            msg = "Data saved Successfully...!"
                            Msg_type = "Info...!"
                        else:
                            msg = "Unable to save data..!"
        except:
            msg = "Something went wrong..!"
        finally:
            self.msg_box(msg,Msg_type)









