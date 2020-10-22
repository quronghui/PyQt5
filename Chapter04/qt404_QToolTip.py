# -*- coding: utf-8 -*- 

'''
# 设置一个显示信息：当鼠标在界面上时显示一行文字；
#2020.9.23
'''

import sys
from PyQt5.QtWidgets import QWidget,  QToolTip,  QApplication
from PyQt5.QtGui import QFont

#1 定义一个类继承于QWidget
class Winfrom(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()               # 自定义函数
    
    #2 自定义initUI()函数
    def initUI(self):       # self自带的第一个变量
        QToolTip.setFont(QFont('SansSerif',  10))   # 字体和字号大小
        self.setToolTip('这是一个<b>气泡提示</b>')      # 创建工具提示，调用setToolTip方法；
        self.setGeometry(200,  300,  400,  400)
        self.setWindowTitle('气泡提示demo')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winfrom()
    win.show()
    sys.exit(app.exec_())
