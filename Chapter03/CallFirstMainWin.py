# -*- coding: utf-8 -*-
# .py的逻辑文件，实现界面文件和逻辑文件的分离
# 2020.9.16

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from firstMainWin import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
