import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QTextEdit, QTreeWidget, QMessageBox,QLabel,QCheckBox,QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
from encrept import *
from regex_ import *
item=[]
from my_sql import *



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'files search'
        self.num_of_targets = 3
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(800,500)


        self.button1 = QPushButton('select file for search', self)
        self.button1.move(80, 260)
        self.button1.resize(200,30)

        self.button1.setFont(QFont("Arial", 12))
        self.button1.clicked.connect(self.openFileNameDialog)


        a = self.check_bx("ADHAR", 80, 70)
        b = self.check_bx("PAN", 80, 100)
        c = self.check_bx("EMAIL", 80, 130)
        d = self.check_bx("MOBILE", 80, 160)
        e = self.check_bx("IP", 80, 190)
        glob_lst.lst = [a, b, c, d, e]

        self.b = QPushButton('clear', self)
        self.b.move(320, 260)
        self.b.setFont(QFont("Arial", 12))
        self.b.clicked.connect(self.clear_all)

        self.text = QTextEdit(self)
        self.text.move(10,300)
        self.text.append(f"-----Scan Result Found-----")
        self.text.setReadOnly(True)
        self.text.setHidden(True)
        self.text.setFixedSize(780,190)
        self.show()



    def msg_bx(self,msg,ms_type):
        Msg = QMessageBox(self)
        Msg.setWindowTitle(ms_type)
        Msg.setFixedSize(200,100)
        Msg.setText(msg)
        Msg.show()


    def check_bx(self, name, x, y):
        chk = QCheckBox(self)
        chk.setText(name)
        chk.move(x, y)
        chk.resize(300, 30)
        chk.setFont(QFont("Arial", 12))
        return chk


    def openFileNameDialog(self):
        MSG = "Scan Limit is Over Contact to ABCD Technologies..!"
        ms_type =  "Alert..!"
        try:
            if self.num_of_targets > 1:
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                fileName, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                          "All Files (*.txt);;Python Files (*.py)", options=options)

                for select_path in fileName:
                    if self.num_of_targets > 1:
                        self.scan(select_path)
                    else:
                        self.msg_bx(MSG,ms_type)
                    break
            else:
                self.msg_bx(MSG, ms_type)
        except:
            MSG = "Something went wrong..!"
            self.msg_bx(MSG, ms_type)

    def scan(self,file_path):
        self.num_of_targets -= 1
        #self.text.clear()
        self.text.setHidden(False)
        file_search(file_path)
        self.text.append(f"File Name: {file_path}")
        for key in glob_lst.result:
            if len(glob_lst.result[key]) > 0:
                for value in glob_lst.result[key]:

                    self.text.append(f"       {key} : {value}")
        self.text.append(('---'*5+'End'+'---'*5))

        glob_lst.result = {"ADHAR": [], "PAN": [], "MOBILE": [], "EMAIL": [], "IP": []}


    def clear_all(self):
        self.text.clear()
        self.text.setHidden(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
