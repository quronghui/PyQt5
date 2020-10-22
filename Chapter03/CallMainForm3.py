# -*- coding: utf-8 -*-
# 添加一个图片：通过lable标签添加一个静态图片；
# 注意：需要将.prc文件便以为.py文件，才能有图片显示；
# 2020.9.21

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from Ui_MainForm3 import Ui_Form

class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
