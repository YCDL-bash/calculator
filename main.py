# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox) # QMessageBox : 메시지박스 위젯
from PyQt5.QtGui import QIcon # icon을 추가하기 위한 라이브러리

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('Message', self) #버튼추가
        self.btn1.clicked.connect(self.activateMessage) #버튼 클릭 시 핸들러 함수 연결
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self): # 버튼을 클릭 시 동작하는 함수:메시지박스 출력
        QMessageBox.information(self, "information", "Button Clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())