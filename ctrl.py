# ch 5.2.1 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.setDisplay) # 버튼 클릭 시 setDisplay 메서드 호출
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b): # 예외 처리 기능 추가
        try:
            return str(a+b)
        except:
            return "Calculation Error"