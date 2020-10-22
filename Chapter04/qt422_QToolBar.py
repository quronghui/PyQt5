# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QToolBar 例子:由文本按钮、图标或其他小控件按钮组成的可移动面板，位于菜单栏下方
（1）# addToolBar()方法：在工具栏区域添加文件工具栏；
（2）# 添加具有文本标题的工具按钮，包括图形按钮；
（3）# 将信号连接到槽函数；每当点击工具栏中的按钮时，都会发射actionTriggered信号。这个型号将关联的QAction对象
		# 的引用发送到连接的槽函数;
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolBarDemo( QMainWindow ):

	def __init__(self, parent=None):
		super(ToolBarDemo, self).__init__(parent)
		self.setWindowTitle("toolbar 例子")		
		self.resize(300, 200)
		
		
		layout = QVBoxLayout()		# 垂直布局
		tb = self.addToolBar("File")		# addToolBar()方法：在工具栏区域添加文件工具栏；
		
		# addAction() 添加具有文本标题的工具按钮，包括图形按钮；
		new = QAction(QIcon("./images/new.png"),"new",self)
		tb.addAction(new)
		open = QAction(QIcon("./images/open.png"),"open",self)
		tb.addAction(open)
		save = QAction(QIcon("./images/save.png"),"save",self)
		tb.addAction(save)
		
		# 将信号连接到槽函数；每当点击工具栏中的按钮时，都会发射actionTriggered信号。这个型号将关联的QAction对象
		# 的引用发送到连接的槽函数;
		tb.actionTriggered[QAction].connect(self.toolbtnpressed)
		self.setLayout(layout)
           	
	def toolbtnpressed(self,a):
		print("pressed tool button is",a.text() )
           
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = ToolBarDemo()
	demo.show()
	sys.exit(app.exec_())
