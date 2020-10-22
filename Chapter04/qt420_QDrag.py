# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  Drag and Drop 例子：拖拽事件的发生
（1）实例：将左边文本框的输入拖拽到右边的下拉菜单栏中——实现下拉菜单的动态输入；
（2）存在两个类：Combo选择继承QComboBox类（下拉选择框）；Example继承了QWidget类；
（3）mimeData()类函数允许检测和使用方便的MIME类型；
（4）允许拖拽数据的控件必须设置QWidget.setDragEnabled()函数为True;
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Combo选择继承QComboBox类（下拉选择框）
class Combo(QComboBox):		
	def __init__(self, title, parent):
		super(Combo, self).__init__( parent)		# 为什么这个还是parent父窗口
		self.setAcceptDrops(True)	
		
	def dragEnterEvent(self, e):
		print( e)
		# mimeData()类函数允许检测和使用方便的MIME类型；
		if e.mimeData().hasText():	# hasText()函数是属于判断函数
			e.accept()
		else:
			e.ignore() 

	def dropEvent(self, e):		# dropEvent拖拽事件的发生；
		self.addItem(e.mimeData().text()) 	# addItem() 添加一个下拉选项；


# Example继承了QWidget类；
class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()		# 自定义的UI显示函数

	def initUI(self):
		lo = QFormLayout()	# 表单布局
		# addRow()添加标签与其他控件在一行上
		lo.addRow(QLabel("请把左边的文本拖拽到右边的下拉菜单中"))
		# 文本编辑框
		edit = QLineEdit()
		#  允许拖拽数据的控件必须设置QWidget.setDragEnabled()函数为True;
		edit.setDragEnabled(True)
		com = Combo("Button", self)		# 调用Combo进行拖拽事件；
		lo.addRow(edit,com)
		
		self.setLayout(lo)
		self.setWindowTitle('简单拖拽例子')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example() 
	ex.show()
	sys.exit(app.exec_())
