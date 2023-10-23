from PySide6.QtWidgets import QLabel, QPushButton

class MyUi(object):
    def setupUi(self, window):
        window.setWindowTitle('Hello')
        window.resize(300, 150)
        
        self.lable = QLabel(window)
        self.lable.setText("欢迎使用本书学习编程")
        self.lable.setGeometry( 80, 50, 150, 20)
        
        self.button = QPushButton(window)
        self.button.setText("关闭")
        self.button.setGeometry(120, 100, 50, 20)