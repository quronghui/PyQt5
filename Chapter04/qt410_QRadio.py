# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中QRadio例子
# QRadioButton 按钮的触发方式为：状态改变时才触发—有利于监控
# 当bt2和bt1进行切换的时候，才会触发槽函数；槽函数的功能用来检测按钮的状态；
#  setChecked：设置复选框的状态，设置为True是表示选中，设置为False表示取消复选框
# 2020.9.24
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Radiodemo(QWidget):
	def __init__(self, parent=None):
		super(Radiodemo, self).__init__(parent)
		
		# QRadioButton 按钮的触发方式为：状态改变时才触发—有利于监控
		# setChecked：设置复选框的状态，设置为True是表示选中，设置为False表示取消复选框
		layout = QHBoxLayout()		# horizon 水平布局；
		self.btn1 = QRadioButton("Button1")
		self.btn1.setChecked(True)
		self.btn1.toggled.connect(lambda:self.btnstate(self.btn1))
		layout.addWidget(self.btn1)
        
		# 这个就未设置复选框2的状态；
		self.btn2 = QRadioButton("Button2")
		self.btn2.toggled.connect(lambda:self.btnstate(self.btn2))
		layout.addWidget(self.btn2)
		
		self.setLayout(layout)
		self.setWindowTitle("RadioButton demo")
	
	# 当bt2和bt1进行切换的时候，才会触发槽函数；槽函数的功能用来检测按钮的状态；
	def btnstate(self,btn):
		if btn.text()=="Button1":
			if btn.isChecked() == True:
				print( btn.text() + " is selected" )
			else:
				print( btn.text() + " is deselected" )
		
		if btn.text()=="Button2":
			if btn.isChecked()== True :
				print( btn.text() + " is selected" )
			else:
				print( btn.text() + " is deselected" )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	radioDemo = Radiodemo()
	radioDemo.show()
	sys.exit(app.exec_())
