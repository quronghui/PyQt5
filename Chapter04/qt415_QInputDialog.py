# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QInputDialog 例子
# QInputDialog 控件是一个标准的对话框，有一个文本框和两个按钮（OK,Cancle）
# （1）与Dialog的区别便是，其不仅可以起提示作用，还能输入文本；并将信息回馈给主窗口
# （2）layout.addRow(self.btn1,self.le1)	# 将两个控件放在一行进行排列；
# （3）布局要求：self.setLayout(layout)	# layout = QFormLayout(self)	没有带self变量时需要这个

# 2020.9.25
'''


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class InputdialogDemo(QWidget):
	def __init__(self, parent=None):
		super(InputdialogDemo, self).__init__(parent)
		layout = QFormLayout(self)		# 表单布局；
		
		self.btn1 = QPushButton("获得列表里的选项")
		self.btn1.clicked.connect(self.getItem)
		self.le1 = QLineEdit()
		layout.addRow(self.btn1,self.le1)	# 在一个布局里面的两个控件布局在一行上；

		self.btn2 = QPushButton("获得字符串")
		self.btn2.clicked.connect(self.getIext)
		self.le2 = QLineEdit()
		layout.addRow(self.btn2,self.le2)

		self.btn3 = QPushButton("获得整数")
		self.btn3.clicked.connect(self.getInt)
		self.le3 = QLineEdit()
		layout.addRow(self.btn3,self.le3)
		
		#self.setLayout(layout)	# layout = QFormLayout(self)	没有带self变量时需要这个
		self.setWindowTitle("Input Dialog 例子")
		
	# items 多选项框进行输入得选择；
	# 包含一个QCombox控件和两个按钮；
	# getItem（）:从控件中获得列表里的选项输入；
	def getItem(self):
		items = ("C", "C++", "Java", "Python")	 # 参数选择列表
		item, ok = QInputDialog.getItem(self, "select input dialog",
		"语言列表", items, 0, False)	# 获取item中的选项；
		if ok and item:						# 与操作：如果选择Ok并且在item内；
			self.le1.setText(item)
	
	def getIext(self):	
		text, ok = QInputDialog.getText(self, "Text Input Dialog", "输入姓名:")
		if ok:
			self.le2.setText(str(text)) 

	def getInt(self):
		num,ok = QInputDialog.getInt(self,"integer input dualog","输入数字")
		if ok:
			self.le3.setText(str(num))
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = InputdialogDemo()
	demo.show()
	sys.exit(app.exec_())
