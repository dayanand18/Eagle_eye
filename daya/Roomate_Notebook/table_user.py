
import pandas as pd1

from PyQt5.QtGui import QStandardItem, QFont
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget, QHeaderView,QApplication
import sys

class load_data(QDialog):

    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.file = ''
        self.user = ''

    def load_dataui(self,user,File):
        self.file = File
        self.user = user
        self.w,self.h = 750,500
        self.setWindowTitle("check table")
        self.setFixedSize(self.w,self.h)

        self.table_item(self.file)

        self.show()

    def table_item(self,fl):
        df = pd1.read_csv(fl)
        if not df.empty:
            columns = df.columns
            itm = QTableWidget(self)
            itm.setFixedSize(self.w,self.h-50)
            itm.setStyleSheet("Background-color:rgb(211,245,227)")
            itm.setFont(QFont("Arial",12))
            itm.move(0,50)


            rows,column = df.shape
            itm.setRowCount(rows)
            itm.setColumnCount(column)
            itm.setEditTriggers(QTableWidget.NoEditTriggers)
            hdr = itm.horizontalHeader()
            hdr1 = itm.verticalHeader()


            for row in range(column):
                item = QStandardItem()
                item.setCheckable(True)
                hdr.setSectionResizeMode(row,QHeaderView.Stretch)
                #hdr1.setSectionResizeMode(row,QHeaderView.Stretch)
                itm.setItem(0,row,QTableWidgetItem(columns[row].capitalize()))
            Row = 1
            for row in range(1,rows):
                if (str(df.loc[row][0]) == str(self.user)):
                    for col in range(column):
                        itm.setItem(Row,col,QTableWidgetItem(str(df.loc[row][col])))
                    Row += 1




#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     obj = load_data()
#     obj.load_dataui('daya.ba007@gmail.com','March2020.csv')
#     # obj.table_item('March2020.csv')
#     sys.exit(app.exec_())

