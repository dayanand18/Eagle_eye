from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.Qt import Qt
import sys

def main():
    app     = QtWidgets.QApplication(sys.argv)
    tree    = QtWidgets.QTreeWidget()
    headerItem  = QtWidgets.QTreeWidgetItem()
    item    = QtWidgets.QTreeWidgetItem()

    # for i in range(3):
    parent = QtWidgets.QTreeWidgetItem(tree)
    parent.setText(1, "SELECT ALL")
    parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        # for x in range(5):
    child = QtWidgets.QTreeWidgetItem(parent)
    child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
    child.setText(1, "ADHARA")
    child.setCheckState(0, Qt.Unchecked)

    child = QtWidgets.QTreeWidgetItem(parent)
    child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
    child.setText(0, "PANCARD")
    child.setCheckState(0, Qt.Unchecked)

    child = QtWidgets.QTreeWidgetItem(parent)
    child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
    child.setText(0, "MOBILE")
    child.setCheckState(0, Qt.Unchecked)

    child = QtWidgets.QTreeWidgetItem(parent)
    child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
    child.setText(0, "IP")
    child.setCheckState(0, Qt.Unchecked)
    tree.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# from PyQt5.QtGui import QIcon, QPixmap
#
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 image - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         # Create widget
#         label = QLabel(self)
#         pixmap = QPixmap('mobile.png')
#         label.setPixmap(pixmap)
#         label.resize(80,100)
#         label.move(150,200)
#         self.resize(10, 20)
#
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
