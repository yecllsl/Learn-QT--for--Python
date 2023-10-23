from PySide6.QtCore import QObject, Signal


class signalDefinition(QObject):
    s1 = Signal()
    s2 = Signal(int)
    s3 = Signal(float)
    s4 = Signal(str)
    s5 = Signal(int, float, str)
    s6 = Signal(list)
    s7 = Signal(dict)
    s8_int = Signal([int])
    s8_str = Signal([str])
    s9 = Signal(int,str) 
    s9_str = Signal([str])
    s9_list = Signal([list])
    s10 = Signal([])
    s10_bool = Signal([bool])
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.s1.connect(self.slot1)    #信号与槽的连接
        self.s2.connect(self.slot2)
        self.s3.connect(self.slot3)
        self.s4.connect(self.slot4)
        self.s5.connect(self.slot5)
        self.s6.connect(self.slot6)
        self.s7.connect(self.slot7)
        #self.s8.connect(self.slot8_1)   #重载型信号的第一个信号可以指定类型
        self.s8_int.connect(self.slot8_1)
        self.s8_str.connect(self.slot8_2)
        self.s9.connect(self.slot9_1)
        #self.s9[int,str].connect(self.slot9_1)
        self.s9_str.connect(self.slot9_2)
        self.s9_list.connect(self.slot9_3)
        self.s10.connect(self.slot10_1)
        self.s10_bool.connect(self.slot10_2)
        
        self.s1.emit()
        self.s2.emit(10)
        self.s3.emit(11.11)
        self.s4.emit("迩灵思信息技术有限公司")
        self.s5.emit(10, 23.5, "尔灵思信息技术有限公司")
        self.s6.emit([1,8,'hello'])
        self.s7.emit({1:'Noise',2:'DoWell'})
        self.s8_int.emit(200) #重载型信号的第一个信号可以不指定类型
        self.s8_str.emit("Noise DoWell Tech.")
        self.s9.emit(300, "Noise DoWell Tech.")
        self.s9_str.emit("s9")
        self.s9_list.emit(["s9",'overload'])
        self.s10.emit()
        self.s10_bool.emit(True)
        
    def slot1(self):
        print("s1 emit")
    def slot2(self, value):
        print("s2 emit int", value)
    def slot3(self, value):
        print("s3 emit float", value)
    def slot4(self, string):
        print("s4 emit string", string)
    def slot5(self, value1, value2, string):
        print("s5 emit many values:", value1, value2, string)
    def slot6(self, list_value):
        print("s6 emit list", list_value)
    def slot7(self, dict_value):
        print("s7 emit dict", dict_value)
    def slot8_1(self, int_value):
        print("s8_int emit int", int_value)
    def slot8_2(self, string):
        print("s8_str emit string", string)
    def slot9_1(self, value1, string):
        print("s9 emit int and string", value1, string)
    def slot9_2(self, string):
        print("s9 emit string", string)
    def slot9_3(self, list_Value):
        print("s9 emit list", list_Value)
    def slot10_1(self):
        print("s10 emit")
    def slot10_2(self, value):
        print("s10 emit bool", value)
            
if __name__ == '__main__':
    signalTest = signalDefinition()
        

        