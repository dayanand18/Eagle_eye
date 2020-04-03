from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow, QDialog, QLabel, QPushButton, QLineEdit)
import sys
from PyQt5.QtGui import QFont
from roomate_db import *
from verify_user_data import user_input_verified
from login import login_ui


class main_window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("project for roomates")
        self.setFixedSize(600,300)


        # Input box section
        self.nm = self.in_box(place_hldr="  Enter Full Name")
        self.cmp = self.in_box(y=60,place_hldr="  Enter Company Name")
        self.mail = self.in_box(y=100,place_hldr="  Enter Email ID")
        self.p1 = self.in_box(y=140,echo_mode=True,place_hldr="  Enter Password")
        self.p2 = self.in_box(y=180,echo_mode=True,place_hldr="  Re-Enter Password")

        # Label section
        self.lbl('Full Name')
        self.lbl('Company Name',y=60)
        self.lbl('E-mail',y=100)
        self.lbl('Password',y=140)
        self.lbl('Confirm-Password',y=180)
        self.lbl('Sign In',x=460,y=210)

        # Button section
        self.btn('Register',function=self.user_register)
        self.btn('Sign In',x=460,y=210,function=self.signin)
        self.btn('Close',x=460,function=self.close)

        self.show()

    # Function for all input boxes
    def in_box(self,x=310,y=20,echo_mode=False,place_hldr=''):
        inp = QLineEdit(self)
        inp.setFixedSize(250,30)
        inp.move(x,y)
        inp.setPlaceholderText(place_hldr)
        inp.setFont(QFont("Times New Roman",14))
        if echo_mode:
            inp.setEchoMode(inp.Password)
        return inp



    # Function for all labels
    def lbl(self,name,x=130,y=20):
        Lbl = QLabel(name,self)
        Lbl.setFixedSize(160,30)
        Lbl.move(x,y)
        Lbl.setFont(QFont("Times New Roman",16))


    # Function for button
    def btn(self,name,x=310,y=240,function=QPushButton.close):
        Btn = QPushButton(name,self)
        Btn.setFixedSize(100,30)
        Btn.move(x,y)
        Btn.setFont(QFont("Times New Roman",14))
        if Btn:
            Btn.clicked.connect(function)

    def already_user(self,u_mail):
        try:
            r_db = rommate_db()
            if r_db.search_user(u_mail):
                return True
            return False
        except:
            return False

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



    def user_register(self):
        msg = ''
        Type = 'Info..!'
        try:
            nm,ml,cmp,p1,p2 = self.nm.text(),self.mail.text().lower(),self.cmp.text(),self.p1.text(),self.p2.text()
            if nm and ml and cmp and p1 and p2:
                if not self.already_user(ml):
                    if user_input_verified(nm,ml,cmp,p1,p2):
                        r_db = rommate_db()
                        res = r_db.insert_user(nm,ml,cmp,p1)
                        if res:
                            msg = "User Registered Successfully..!"
                        else:
                            msg = "Something went wrong..!"
                            Type = "Alert..!"
                    else:
                        msg = "Invalid input..!"
                        Type = "Alert..!"
                else:
                    msg = "User Already Exists..!"
                    Type = "Alert..!"
            else:
                msg = "Enter the all inputs"
                Type = "Alert..!"
        except Exception as E:

            msg = "Error occured during registration...!"
            Type = "Error..!"
        finally:
            self.all_box_clear()
            self.msg_box(msg,Type)

    def all_box_clear(self):
        try:
            self.nm.clear(),self.mail.clear(),self.cmp.clear(),self.p1.clear(),self.p2.clear()
        except:
            pass

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

    def signin(self):
        #self.setHidden(True)
        try:
            self.a = login_ui()
            self.a.show()
            self.close()
        except :
            pass


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    app = main_window()
    sys.exit(APP.exec_())


