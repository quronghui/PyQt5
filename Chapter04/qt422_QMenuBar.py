# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 Qmenu 例子:QMenuBar用于显示QMainWindow标题栏；
（1）第一个菜单栏基于menuBar进行创建的；同样，菜单栏下的addAction 动作都是基于此菜单栏的；
（2）基于第一个菜单栏下，再次创建菜单栏，那么此时便是基于第一个菜单栏;
（3）对象.addSeparator() # 在菜单栏中添加横线，在需要添加横线的动作后面添加；
（4）分清楚上一级的父类是谁；
（5）添加第一个动作，基于file：两种方式实现；
（6） 基于file的第二个动作：为动作Action添加一个快捷键的方法；
（7）每一次点此Action都会触发一个信号；如何将不同的Action连接到不同的槽函数？
		
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MenuDemo(QMainWindow):
	def __init__(self, parent=None):
		super(MenuDemo, self).__init__(parent)
		
		# 水平布局
		layout = QHBoxLayout()
		bar = self.menuBar()		# 创建一个menuBar菜单栏对象；
		file = bar.addMenu("File")	# 在菜单栏中添加一个新的QMenu对象；
		file.addSeparator()
		
		# test 平行的第二个菜单项
		ll = bar.addMenu("dd")		# 基于bar创建第二个平行的菜单栏对象；
		
		# 添加第一个动作，基于file：两种方式实现
		New = QAction("New", self)	# 方式1
		file.addAction(New)
		#file.addAction("New")				# 方式2
		file.addSeparator()				# 在菜单栏中添加横线
		
		# 基于file的第二个动作：为动作Action添加一个快捷键的方法；
		save = QAction("Save",self)
		save.setShortcut("Ctrl+S")
		file.addAction(save)
		file.addSeparator()				# 在菜单栏中添加横线
		
		# 添加第二项菜单，基于file菜单下的子菜单，在这个子菜单下添加两个动作：
		edit = file.addMenu("Edit")
		edit.addAction("copy")	
		edit.addSeparator()				
		edit.addAction("paste")
		file.addSeparator()				
		
		# 添加第五个动作，基于self;
		quit = QAction("Quit",self)
		file.addAction(quit)
		file.addSeparator()				# 在菜单栏中添加横线
		
		# 每一次点此Action都会触发一个信号；
		# 如何将不同的Action连接到不同的槽函数？
		file.triggered[QAction].connect(self.processtrigger) 
		
		# 窗口的布局、Title、大小
		self.setLayout(layout)
		self.setWindowTitle("menu 例子")
		self.resize(350,300)
		
	def processtrigger(self,q):
		print( q.text()+" is triggered" )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = MenuDemo()
	demo.show()
	sys.exit(app.exec_())
