# import sys
# from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMessageBox, QLabel,QTextEdit, QDialog
# from PyQt5.QtGui import QFont
# import re
#
#
# class Licencekey(QDialog):
#
#     def __init__(self,parent=None):
#         QDialog.__init__(self,parent)
#         self.title = 'scanning....!'
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setFixedSize(550, 200)
#
#         self.lbl = QLabel('authetication key', self)
#         self.lbl.move(280, 10)
#         self.lbl.setFixedSize(200,30)
#         self.lbl.setFont(QFont("Arial",12))
#
#         self.textbox1 = QTextEdit(self)
#         self.textbox1.move(135, 40)
#         self.textbox1.resize(400, 120)
#
#         # Create a button in the window
#         self.button1 = QPushButton('ENTER', self)
#         self.button1.move(200,165)
#         self.button1.clicked.connect(self.on_click)
#
#         self.button = QPushButton('clear', self)
#         self.button.move(390, 165)
#         self.button.clicked.connect(self.clear_all)
#         self.show()
#
#     def on_click(self):
#
#         # self.label.setFont(QFont("Arial", 12))
#
#         self.text1 = QLineEdit(self)
#         self.text1.move(100, 340)
#         self.text1.resize(220, 25)
#         self.show()
#
#     def clear_all(self):
#         first = self.textbox1.clear()
#
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Licencekey()
#     sys.exit(app.exec_())

