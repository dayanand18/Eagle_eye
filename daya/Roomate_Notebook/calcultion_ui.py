from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow,QCheckBox, QDialog, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox)
import sys
from PyQt5.QtGui import QFont, QDoubleValidator
from test import *
from cal_part import *
from roomate_db import *
from pd_check import *
from send_report import *
from datetime import datetime as dt

class cal_window(QDialog):

    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.user = ''

    def cal_ui(self,usr):
        self.user = usr
        self.setWindowTitle("calculation roomates")
        self.setFixedSize(700,400)


        # Input box section
        self.rent = self.in_box(place_hldr="  Enter room rent",echo_mode=True)
        self.bill = self.in_box(y=60,place_hldr="  Enter current bill",echo_mode=True)
        self.memb = self.in_box(y=100,place_hldr="  Enter present members",echo_mode=True)

        # Label section
        self.lbl('room rent')
        self.lbl('Bill',y=60)
        self.lbl('Member',y=100)

        # Button section
        self.btn('calculation',function=self.user_register1)
        self.btn('clear',x=460,y=150,function=self.clear_all)
        # self.btn('Close',x=460,function=self.close)

        self.table = QTextEdit(self)
        self.table.resize(600, 150)
        self.table.move(25, 200)
        self.table.setFont(QFont("Times New Roman",16))
        self.table.setHidden(True)

        self.box = QCheckBox(self)
        self.box.setText('Send Report')
        self.box.move(310,130)
        # self.box.clicked.connect(self.pdf_select)
        self.show()

    # Function for all input boxes
    def in_box(self,x=310,y=20,echo_mode=False,place_hldr=''):
        inp = QLineEdit(self)
        inp.setFixedSize(250,30)
        inp.move(x,y)
        inp.setPlaceholderText(place_hldr)
        inp.setFont(QFont("Times New Roman",14))
        if echo_mode:
            inp.setValidator(QDoubleValidator(0.99,99.99,2))
        return inp

    # Function for all labels
    def lbl(self,name,x=130,y=20,link=QLabel.close):
        Lbl = QLabel(name,self)
        Lbl.setFixedSize(160,30)
        Lbl.move(x,y)
        Lbl.setFont(QFont("Times New Roman",16))

    def clear_all(self):
        self.rent.clear()
        self.bill.clear()
        self.memb.clear()
        self.table.clear()
    # Function for button
    def btn(self,name,x=310,y=150,function=QPushButton.close):
        Btn = QPushButton(name,self)
        Btn.setFixedSize(100,30)
        Btn.move(x,y)
        Btn.setFont(QFont("Times New Roman",14))
        if Btn:
            Btn.clicked.connect(function)
        return Btn


    def user_register1(self):
        mnth = str(dt.now().strftime('%B%Y'))
        self.table.setHidden(False)
        rent,one_user,total,bill,memb='0','0','0','0','0'
        Msg = ''
        ms_type = 'Info..!'
        try:
            one_user = check_user(self.user,mnth+'.csv')
            total =total_file(mnth+'.csv')

            rent = self.rent.text()

            bill = self.bill.text()
            memb = self.memb.text()
            if len(rent) > 0 and len(bill) >0 and len(memb) >0:
                obj = calcu_room(rent,bill,total,one_user,memb)
                total_rent1= obj.room_rent()

                details = f'room rent:{rent} \n current bill {bill} \n total rent payble {total_rent1}'

                if "REPORT_STORAGE" in os.listdir(os.getcwd()):
                    pass
                else:
                    os.mkdir("REPORT_STORAGE")

                obj = rommate_db()
                val = obj.pdf_generated()


                for k in val:
                    user_storage = os.path.join("REPORT_STORAGE",str(k[0]))

                    if str(k[0]) in os.listdir("REPORT_STORAGE"):
                        pass
                    else:
                        os.mkdir(user_storage)
                    background(c)
                    generate = create(rent,bill,memb,k[1],k[0],user_storage,pending_amount=k[2])

                    if generate and self.box.isChecked():
                        send_mail(str(k[0]),mnth,generate,str(k[1]))
                        self.table.setText(str(details))
                    self.table.setText(str(details))
                    Msg = 'calculation done'

            else:
                Msg = 'Enter input'
                ms_type = 'Alert..!'
        except:
            Msg='something went wong'
            return False
        finally:
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





