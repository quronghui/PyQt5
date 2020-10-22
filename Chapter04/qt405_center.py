# -*- coding: utf-8 -*-

'''
二、PyQT5将窗口放在屏幕中间例子
# 2020.9.21
    
'''

from PyQt5.QtWidgets import QDesktopWidget, QApplication ,QMainWindow
import sys  
    
class Winform( QMainWindow): 
    
    def __init__(self, parent=None):
        super( Winform, self).__init__(parent)
          
        self.setWindowTitle('主窗口放在屏幕中间例子')  
        self.resize(370,  250)  
        self.center()  
          
    # 自定义函数：实现窗口显示在中间
    def center(self):  
        screen = QDesktopWidget().screenGeometry()      # QDesktopWidget描述显示屏幕的类；screenGeometry获得屏幕的大小
        size = self.geometry()       # 获取QWidget 屏幕大小
        self.move((screen.width() - size.width()) / 2,  (screen.height() - size.height()) / 2)  # 移动到中间
  
if __name__ == "__main__": 
    app = QApplication(sys.argv)   
    win = Winform()  
    win.show()  
    sys.exit(app.exec_())  
