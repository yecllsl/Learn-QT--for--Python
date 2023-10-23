import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class myWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi()
        self.button.clicked.connect(self.bell_alert)
        
    def setupUi(self):
        self.setWindowTitle("Hello")
        self.resize(300, 150)
        
        self.label = QLabel(self)
        self.label.setText("欢迎使用本书学习编程")
        self.label.setGeometry(80, 50, 150, 20)
        
        self.button = QPushButton(self)
        self.button.setText("响铃与预警")
        self.button.setGeometry(90, 100, 100, 20)
        
    def bell_alert(self):
        QApplication.beep()
        QApplication.alert(win, duration = 0)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("欢迎程序")
    app.setEffectEnabled(Qt.UI_AnimateCombo)
    
    win = QWidget()
    win.show()
    myWindow = myWidget()
    myWindow.show()
    sys.exit(app.exec_())
    