# -*- coding: utf-8 -*- 

'''
# 为PyQt程序设置一个程序图标；
#2020.9.23
'''


import sys
from PyQt5.QtGui import QIcon   # QIcon类型必须导入的模块
from PyQt5.QtWidgets  import QWidget , QApplication

#1  类的创建：Icon的构造函数继承QWidget的构造函数；
class Icon(QWidget):  
    def __init__(self,  parent = None):  
        super(Icon,self).__init__(parent)    
        self.initUI()     
     
    #2   自定义方法：设置图标的位置
    def initUI(self):
        self.setGeometry(300,  300,  250,  150)  
        self.setWindowTitle('演示程序图标例子')  
        self.setWindowIcon(QIcon('./images/cartoon1.ico'))  
              
if __name__ == '__main__':   
    app = QApplication(sys.argv)
    icon = Icon()  
    icon.show()  
    sys.exit(app.exec_())  
