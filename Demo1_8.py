import sys
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = QWidget()
    ui = MyUi()
    ui.setupUi(myWindow)
    ui.button.setText(" Close ")
    ui.button.clicked.connect(myWindow.close)
    myWindow.show()
    sys.exit(app.exec_())