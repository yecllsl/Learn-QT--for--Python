import sys
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from PySide6.QtCore import Slot,Signal
from student_new_ui import Ui_Form

class QmyWidget(QWidget):
    numberSingnal = Signal(int)   #自定义信号
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__student = dict()
        #self.__count = 0
        #self.__score = list()
        self.ui.btnCalculate.clicked.connect(self.scoreCalculate)  #手动连接信号与槽
        self.numberSingnal.connect(self.isNumberExisting)
    
    def scoreCalculate(self):
        s = self.ui.Chinese.value()+self.ui.math.value()+self.ui.english.value()
        self.ui.total.setText(str(s))
        template = "{:.1f}".format(s/3)
        self.ui.average.setText(template)
        #self.__count += 1
        temp = list()
        temp.append(self.ui.name.text())
        temp.append(self.ui.number.value())
        temp.append(self.ui.Chinese.value())
        temp.append(self.ui.math.value())
        temp.append(self.ui.english.value())
        temp.append(s)
        temp.append(float(template))
        #self.__score.append(temp)
        self.__student[self.ui.number.value()] = temp
        
    @Slot()
    def on_btnSave_clicked(self):
        template = "姓名{} 学号{} 语文{} 数学{} 英语{} 总成绩{} 平均分{}\n"
        try:
            fp = open("student_score_number.txt", "a+",encoding="utf-8")
        except:
            print("文件打开失败")
        else:
            for i in self.__student.values():
                score = template.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                fp.write(score)
            fp.close()
            
    @Slot()
    def on_number_editingFinished(self): #输入学号完成时的槽函数
        self.numberSingnal.emit(self.ui.number.value())
    def isNumberExisting(self,value):
        if value in self.__student:
            existing = QMessageBox.question(self,"确认信息","学号已存在，是否覆盖？", QMessageBox.Yes | QMessageBox.No)
            if existing == QMessageBox.No:
                self.ui.number.setValue(0)
                self.ui.number.setFocus()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = QmyWidget()
    myWindow.show()
    sys.exit(app.exec_())
    