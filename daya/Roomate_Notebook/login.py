from PyQt5.QtWidgets import (QMessageBox, QMainWindow, QLabel,
                             QPushButton, QLineEdit)
from verify_user_data import is_email, is_password

from PyQt5.QtGui import QFont
from roomate_db import rommate_db
from user_page import *
from Otp_gen import *
from otp_send import *
import random
class login_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("login pages")
        self.setFixedSize(500,200)

        self.uname = self.in_box(place_hldr="  Enter User Name")
        self.pw = self.in_box(y=90,place_hldr="  Enter Password",echo_mode=True)

        self.lbl("User Name")
        self.lbl("Password",y=90)

        self.btn("Login",function=self.Login)
        self.btn("Close",x=360,function=self.close)
        self.btn("Forget pw",x=300,y=165,function=self.passw_forget)
        self.show()

    # Function for all input boxes
    def in_box(self,x=210,y=50,echo_mode=False,place_hldr=''):
        inp = QLineEdit(self)
        inp.setFixedSize(250,30)
        inp.move(x,y)
        inp.setPlaceholderText(place_hldr)
        inp.setFont(QFont("Times New Roman",14))
        if echo_mode:
            inp.setEchoMode(inp.Password)
        return inp

    # Function for all labels
    def lbl(self,name,x=90,y=50):
        Lbl = QLabel(name,self)
        Lbl.setFixedSize(160,30)
        Lbl.move(x,y)
        Lbl.setFont(QFont("Times New Roman",16))


    # Function for button
    def btn(self,name,x=210,y=135,function=QPushButton.close):
        Btn = QPushButton(name,self)
        Btn.setFixedSize(100,30)
        Btn.move(x,y)
        Btn.setFont(QFont("Times New Roman",14))
        if Btn:
            Btn.clicked.connect(function)
    def passw_forget(self):
        self.msg_box("Under Development...!","Info...!")
            #




    def Login(self):
        Msg = ''
        ms_type = 'Info..!'
        try:
            uname,pw = self.uname,self.pw
            if is_email(uname.text().lower()) and is_password(str(pw.text()),str(pw.text())):
                dbr = rommate_db()
                user_res = dbr.search_user(str(uname.text()).lower())
                if len(user_res) == 1:
                    if user_res[0][6] == 1:
                        if (str(uname.text().lower()) == user_res[0][0]) and (str(pw.text() == user_res[0][3])):

                            self.b = user_win(str(uname.text().lower()))
                            self.b.show()
                            Msg = f"Login successfull..!"

                            self.close()
                        else:
                            Msg = "Bad Credentials"
                            ms_type = "Alert...!"
                    else:
                        Msg = "Contact To Administrator"
                        ms_type = "Alert...!"
                else:
                    Msg = "Bad Credentials"
                    ms_type = "Alert...!"
            else:
                Msg = "Invalid inputs"
                ms_type = "Alert...!"
        except:
            Msg = "Invalid inputs"
            ms_type = "Alert...!"
        finally:
            self.uname.clear();self.pw.clear()
            self.msg_box(Msg,ms_type)

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



#
# if __name__ == "__main__":
#     APP = QApplication(sys.argv)
#     app = login_ui()
#     sys.exit(APP.exec_())