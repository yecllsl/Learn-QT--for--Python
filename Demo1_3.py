import sys
from PySide6.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)
myWindow = QWidget()
myWindow.show()
n= app.exec()               #执行exec()方法，进入事件循环，若遇到窗口推出命令，返回整数n
sys.exit(n)