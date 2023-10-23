import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont, QColor,QPalette
from random import randint,seed

class SetPalette(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("设置调色板实例")
        self.setGeometry(200, 200, 1200, 500)
        self.createLabels()
        self.setLabelColor()
        self.getLabelColorRGB()

    def createLabels(self):
        self.labels = list()
        font = QFont("黑体",pointSize=20)
        string = "Nice to meet you! 很高兴认识你！"
        for i in range(10):
            label = QLabel(self)
            label.setGeometry(5, 50*i, 1200,40)
            label.setText(str(i)+':'+string)
            label.setFont(font)
            self.labels.append(label)

    def setLabelColor(self):
        seed(12)
        for label in self.labels:
            colorBase = QColor(randint(0,255),randint(0,255),randint(0,255))
            colorText = QColor(randint(0,255),randint(0,255),randint(0,255))
            palette = label.palette()
            palette.setColor(QPalette.Active, QPalette.Window,colorBase)
            palette.setColor(QPalette.Active,QPalette.WindowText,colorText)
            label.setAutoFillBackground(True)
            label.setPalette(palette)
    def getLabelColorRGB(self):
        for label in self.labels:
            r,g,b,a = label.palette().window().color().getRgb()
            rT,gT,bT,a = label.palette().windowText().color().getRgb()
            
            text = (label.text()+"背景颜色：{} {} {} 文字颜色：{} {} {}").format(r,g,b,rT,gT,bT)
            label.setText(text)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetPalette()
    window.show()
    sys.exit(app.exec_())