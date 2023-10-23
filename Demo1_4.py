import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication(sys.argv)

myWindow = QWidget()
myWindow.setWindowTitle('Hello')
myWindow.resize(300, 150)

myLabel = QLabel(myWindow)
string = '欢迎使用本书学习PySide6'
myLabel.setText(string)
myLabel.setGeometry(80, 50, 150, 20)

myButton = QPushButton(myWindow)
myButton.setText("关闭")
myButton.setGeometry(120, 100, 50, 20)
myButton.clicked.connect(myWindow.close)

myWindow.show()
n = app.exec()
print("n=", n)
try:
    sys.exit(n)
except SystemExit:
    print("请在此做一些退出后的其他工作")
