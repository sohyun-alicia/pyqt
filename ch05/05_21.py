import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

form_class = uic.loadUiType("bull.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 타이머 추가
        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        print("5초에요!!")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()