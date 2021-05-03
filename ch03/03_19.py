import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 400)
        # 왼쪽 상단으로부터 윈도우가 출력되는 x축 위치, y축 위치, 윈도우의 너비, 윈도우의 높이
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("building.png"))

        btn = QPushButton("버튼1", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()