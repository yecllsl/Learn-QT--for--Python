import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


def setupUi(window):
    window.setWindowTitle('Hello')
    window.resize(300, 150)
    label = QLabel(window)
    label.setText("欢迎使用本书学习编程")
    label.setGeometry(80, 50, 150, 20)

    button = QPushButton(window)
    button.setText("关闭")
    button.setGeometry(120, 100, 50, 20)
    button.clicked.connect(myWindow.close)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QWidget()
    setupUi(myWindow)
    myWindow.show()
    sys.exit(app.exec())
