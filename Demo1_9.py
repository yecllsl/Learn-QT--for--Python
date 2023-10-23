import sys
from PySide6.QtWidgets import QApplication, QWidget

from myUi import MyUi

def myWidget(parent = None):
    widget = QWidget(parent)
    ui = MyUi()
    ui.setupUi(widget)
    ui.button.setText("Close")
    ui.button.clicked.connect(widget.close)
    return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = myWidget()
    myWindow.show()
    sys.exit(app.exec_())
    