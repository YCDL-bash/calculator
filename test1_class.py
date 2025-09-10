# class의 Inheritence의 개념을 이해하기 위한 테스트 코드
# Inheritence를 하지 않고 QWidget을 직접 사용하는 경우 예제

import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
widget = QWidget() # 빈 창만 생성
widget.show() # 아무 기능 없는 빈 창 표시
sys.exit(app.exec_())