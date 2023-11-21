import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import uic
import getpass
from datetime import datetime


# REQ 2023-047569

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./app/Gui/pruebaformatoui.ui", self)

        
        
        

       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

