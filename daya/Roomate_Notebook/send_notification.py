from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit,QComboBox,QTextEdit)
import sys
from PyQt5.QtGui import QFont
from roomate_db import *
from verify_user_data import user_input_verified
from login import login_ui

class send_window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("notifiction")
        self.setFixedSize(800,400)


        # Input box section
        self.nm = self.in_box(place_hldr="  Enter email")


        self.lbl('User')


        # Button section
        self.btn('send',function=self.user_register)

        self.cbx = self.cmb_bx()

        self.table = QTextEdit(self)
        self.table.resize(500, 200)
        self.table.move(80, 80)
        self.table.setFont(QFont("Times New Roman",16))

        self.show()

    def in_box(self,x=100,y=20,echo_mode=False,place_hldr=''):
        inp = QLineEdit(self)
        inp.setFixedSize(250,30)
        inp.move(x,y)
        inp.setPlaceholderText(place_hldr)
        inp.setFont(QFont("Times New Roman",14))
        if echo_mode:
            inp.setEchoMode(inp.Password)
        return inp

    # Function for all labels
    def lbl(self,name,x=50,y=20,link=QLabel.close):
        Lbl = QLabel(name,self)
        Lbl.setFixedSize(160,30)
        Lbl.move(x,y)
        Lbl.setFont(QFont("Times New Roman",16))
    # def get_emails(self):
    #     try:
    #         files = ["dayaayb@gmail.com","dayayb@gmail.com"]
    #         return files
    #     except:
    #         return False

    def cmb_bx(self):
        try:
            cmb = QComboBox(self)
            cmb.setFixedSize(220,30)
            cmb.move(550,20)
            db_obj = rommate_db()
            self.user_lst = ['Select All']
            for usr in db_obj.get_emails():#.append('Select All')
                self.user_lst.__iadd__(usr)

            cmb.addItems(self.user_lst)
            return cmb
        except:
            return False
    # Function for button
    def btn(self,name,x=500,y=290,function=QPushButton.close):
        Btn = QPushButton(name,self)
        Btn.setFixedSize(100,30)
        Btn.move(x,y)
        Btn.setFont(QFont("Times New Roman",14))
        if Btn:
            Btn.clicked.connect(function)

    def already_user(self,u_mail):
        print("hello")

    def verify_user(self,nm,ml,cmp,p1,p2):
        print("bye")

    def user_register(self):
        print(self.cbx.currentText())
        self.close()
        # if self.cmb_bx():

        # if self.cmb_bx():
        #     print(self.user_lst)


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
        print("show")


# if __name__ == "__main__":
#     APP = QApplication(sys.argv)
#     app = send_window()
#     sys.exit(APP.exec_())


