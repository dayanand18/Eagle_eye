import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'scanning....!'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(450,350)


        self.QLabel = QLabel('username',self)
        self.QLabel.move(20,20)


        self.QLabel = QLabel('password',self)

        self.QLabel.move(20,80)

        # Create textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 20)
        self.textbox1.resize(280, 40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.setEchoMode(QLineEdit.Password)
        self.textbox2.move(80,80)
        self.textbox2.resize(280, 40)

        # Create a button in the window
        self.button1 = QPushButton('login', self)
        self.button1.move(80, 130)
        self.button1.clicked.connect(self.success)


        self.daya = QPushButton('clear', self)
        self.daya.move(200, 130)
        # self.daya.resize(200,130)
        self.daya.clicked.connect(self.on_clear)


        self.button = QPushButton('create login', self)
        self.button.move(300, 130)
        self.button.clicked.connect(self.on_click)
        self.show()

    def success(self):
        print("test")

    def on_click(self):
        username = self.textbox.text()
        password = self.textbox1.text()
        self.w = window2()
        self.w.show()

    def on_clear(self):
        tex1 = self.textbox.clear()
        tex2 = self.textbox1.clear()
        try:
            QMessageBox.question(self, "message box", tex1 + tex2,QMessageBox.Ok)
        except Exception as E:
            print(E)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
