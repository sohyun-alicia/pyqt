import sys
from PyQt5.QtWidgets import*

class MyWindow(QMainWindow):        # QMainWindow 클래스 상속
    def __init__(self):
        super().__init__()          # super() : 파이썬 내장함수. 부모 클래스의 initializer 호출


app = QApplication(sys.argv)    
window = MyWindow()                 # 객체 생성
window.show()
app.exec_()