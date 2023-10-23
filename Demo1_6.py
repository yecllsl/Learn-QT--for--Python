import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyUi():
    def setupUi(self, window):
        window.setWindowTitle('Hello')
        window.resize(300, 150)

        self.label = QLabel(window)
        self.label.setText("欢迎使用本书学习编程")
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(window)
        self.button.setText("关闭")
        self.button.setGeometry(120, 100, 50, 20)
        # self.button.clicked.connect(Window.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QWidget()

    ui = MyUi()
    ui.setupUi(myWindow)
    ui.button.setText("Close")
    ui.button.clicked.connect(myWindow.close)

    myWindow.show()
    sys.exit(app.exec())
