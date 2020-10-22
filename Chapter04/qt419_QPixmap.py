# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QPixmap 例子:用于绘图设备的图像显示
（1）它可以作为一个QPaintDevice对象；也可以加载到一个控件中，通常是标签和按钮；
（2）使用setPixmap将图像显示在QLable上；
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	# 使用setPixmap将图像显示在QLable上；
	win = QWidget()	# 继承了QWidget
	lab1 = QLabel()
	lab1.setPixmap(QPixmap("./images/python.jpg"))
	# 布局：
	vbox=QVBoxLayout()
	vbox.addWidget(lab1)
	win.setLayout(vbox)
	
	# 显示标题
	win.setWindowTitle("QPixmap 例子")
	win.show()
	sys.exit(app.exec_())
