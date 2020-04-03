import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QTextEdit, QLineEdit, QMessageBox,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from file_list import *
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'files search'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(800,500)

        # Create a button in the window
        self.button1 = QPushButton('select file for search', self)
        self.button1.move(80, 60)
        self.button1.resize(200,30)
        self.button1.setFont(QFont("Arial", 12))
        self.button1.clicked.connect(self.openFileNameDialog)

        self.b = QPushButton('clear', self)
        self.b.move(320, 60)
        self.b.setFont(QFont("Arial", 12))
        self.b.clicked.connect(self.clear_all)

        self.text = QTextEdit(self)
        self.text.move(10,100)
        self.text.setFixedSize(780,380)

        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*.txt);;Python Files (*.py)", options=options)

        for select_path in fileName:
            result = file_search(select_path)
            for file in result:
                self.text.insertPlainText(f'{file}\n')

    def clear_all(self):
        self.text.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
