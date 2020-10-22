# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QStatusBar 例子
（1）实例：创建一个file惨淡栏，并为其添加一个动作，并为其创建一个编辑框；最后点击show动作时，提示已被点击；
（2）保留一个水平条，作为状态栏，用于显示永久的或临时的状态信息；
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StatusDemo(QMainWindow):
	def __init__(self, parent=None):
		super(StatusDemo, self).__init__(parent)
		self.setWindowTitle("QStatusBar 例子")
		bar = self.menuBar()		# 创建一个menuBar菜单栏对象；
		
		file = bar.addMenu("File")	# 创建第一个菜单栏项；
		file.addAction("show")			# 为file菜单栏添加动作；
		file.triggered[QAction].connect(self.processTrigger)	# 每次点击file菜单栏便会触发，连接到槽函数；
		self.setCentralWidget(QTextEdit())					# 添加一个编辑框QTextEdit对象，置于中间
		
		# 通过主窗口的QMainWindow的setStatusBar()函数设置状态栏
		self.statusBar= QStatusBar() 	# QStatusBar设置状态栏，创建一个状态栏对象；
		self.setStatusBar(self.statusBar)		# set设置状态栏显示
	
	def processTrigger(self,q):
		if (q.text()=="show"):
			self.statusBar.showMessage(q.text()+" 菜单选项被点击了",5000)	# 延时5秒
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = StatusDemo()
	demo.show()
	sys.exit(app.exec_())
