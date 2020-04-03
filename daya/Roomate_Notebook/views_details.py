import sys

from PyQt5.QtWidgets import (QMainWindow, QLabel, QApplication, QWidget, QPushButton, QAction,QCheckBox,
                             QLineEdit, QMessageBox,QComboBox, QTableView, QTableWidget, QTextEdit,QTableWidgetItem)
from PyQt5.QtGui import QFont
from roomate_db import *
from table_user import *
from pd_check import *
from calcultion_ui import cal_window

import time

from test import *
class view_det_window(QMainWindow):

    def __init__(self,user,role):
        super().__init__()
        self.title = 'views all user'
        self.user= user
        self.user_role = role
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(800, 600)

        self.btn('load',function=self.show_data)
        self.btn('Export txt',x=360,y=120,function=self.txt_load)
        # self.btn('Export pdf',x=580,y=120,function=self.pd_convert)
        self.btn('Export csv',x=470,y=120,function=self.csv_load)
        self.btn('send',x=350,y=480,function=self.csv_load)

        self.in_box(place_hldr="  Enter subject")
        self.lbl('subject')
        self.lbl('Message',y=150)

        if self.user_role == 1:
            self.btn('Enble User',x=320,y=30,function=self.enble_user)
            self.btn('Disble User',x=430,y=30,function=self.disble_user)
            self.btn('Delete User',x=540,y=30,function=self.delete_user)
            #self.btn('Export pdf',x=650,y=120,function=self.pd_convert)
            self.btn('Calculations',x=690,y=120,function=self.calculate)
            self.cbx = self.cmb_bx()



        self.table = QTextEdit(self)
        self.table.resize(400, 250)
        self.table.move(25, 200)
        self.table.setFont(QFont("Times New Roman",16))
        self.show()

    def Qbox(self,name,x=400,y=65):
        box = QComboBox()
        box.addItem(name)
    # Function for button
    def btn(self,name,x=200,y=30,function=QPushButton.close):
        Btn = QPushButton(name,self)
        Btn.setFixedSize(100,30)
        Btn.move(x,y)
        Btn.setFont(QFont("Times New Roman",14))
        Btn.clicked.connect(function)

    def cmb_bx(self):
        try:
            cmb = QComboBox(self)
            cmb.setFixedSize(140,30)

            cmb.move(30,30)

            db_obj = rommate_db()
            self.lst = []
            for usr in db_obj.get_emails():
                self.lst.__iadd__(usr)
            self.lst.remove(self.user)

            cmb.addItems(self.lst)
            return cmb
        except:
            return False

    def in_box(self,x=100,y=120,echo_mode=False,place_hldr=''):
        inp = QLineEdit(self)
        inp.setFixedSize(250,30)
        inp.move(x,y)
        inp.setPlaceholderText(place_hldr)
        inp.setFont(QFont("Times New Roman",14))
        if echo_mode:
            inp.setEchoMode(inp.Password)
        return inp


    def lbl(self,name,x=20,y=120):
        Lbl = QLabel(name,self)
        Lbl.setFixedSize(160,30)
        Lbl.move(x,y)
        Lbl.setFont(QFont("Times New Roman",16))

    def enble_user(self):
        usr = str(self.cbx.currentText())
        Msg = "Unable To Change the Status..!"
        ms_type = "Alert..!"
        try:
            if usr:
                db_obj = rommate_db()
                res = db_obj.update_user_status(usr,1)
                if res:
                    Msg = "User Enabled Succssfully..!"
                    ms_type = "Info..!"
            else:
                Msg = "Nothing to delete...!"
                ms_type = "Alert..!"
        except:
            Msg = "Error Occurred While Changing the Status..!"
        finally:
            self.msg_box(Msg,ms_type)

    def disble_user(self):
        usr = str(self.cbx.currentText())
        Msg = "Unable To Change the Status..!"
        ms_type = "Alert..!"
        try:
            db_obj = rommate_db()
            res = db_obj.update_user_status(usr,0)
            if usr:
                if res:
                    Msg = "User Disabled Succssfully..!"
                    ms_type = "Info..!"
            else:
                Msg = "Nothing to delete...!"
                ms_type = "Alert..!"
        except:
            Msg = "Error Occurred While Changing the Status..!"

        finally:
            self.msg_box(Msg,ms_type)
    def pd_convert(self):
        try:
            usr = str(self.cbx.currentText())
            u = usr.split('@gmail.com')
            name = ''.join(u)
            background(c)
            create(name,usr)
            return True
        except:
            return False
    def txt_load(self):
        try:
            file = str(dt.now().strftime('%B%Y'))+'.csv'
            with open(str(self.user).split('@')[0]+'.txt','w') as f:
                files = f.write(str(view_user(self.user,file)))
                return files
        except:
                return False

    def csv_load(self):
        try:
            file = str(dt.now().strftime('%B%Y'))+'.csv'
            df = pd.read_csv(file)
            df.set_index('user',inplace=True)
            df.to_csv(file)
            return True
        except:
            return False
    def delete_user(self):
        user = str(self.cbx.currentText())
        Msg = "Unable To Change the Status..!"
        ms_type = "Alert..!"
        refresh = True
        try:
            if user:
                db_obj = rommate_db()
                res = db_obj.delete_box(user)
                if res:
                    Msg = "User Delete Succssfully..!"
                    ms_type = "Info..!"
            else:
                Msg = "Nothing to delete...!"
                ms_type = "Info..!"
                refresh = False
        except:
            Msg = "Error Occurred While Changing the Status..!"
            refresh = False
        finally:
            self.msg_box(Msg,ms_type)
            if refresh:
                self.close()
                self.u_D = view_det_window(str(self.user),1)
                self.u_D.show()


    def calculate(self):
        try:
            self.cal_win = cal_window(self)
            self.cal_win.cal_ui(self.user)
        except Exception as E:
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
    def show_data(self):
        try:
            usr=self.user
            if self.user_role == 1:
                usr = self.cbx.currentText()
            file = str(dt.now().strftime('%B%Y'))+'.csv'
            self.w = load_data(self)
            self.w.load_dataui(usr,file)
        except:
            pass









