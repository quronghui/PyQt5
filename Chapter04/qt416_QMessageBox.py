# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QMessage 例子
# QMessage 通用的弹出式对话框，用于显示消息：可以修改不同的文字，显示不同的图标；
# （1）功能都是一样的：起到一个提示作用；
# （2）infomation信息框  ：有标准的形式；
# （3）实现了五种对话框的代码；
# （4）问题：没有实现布局？解决layout = QVBoxLayout(self)	加入self变量，对其进行布局；
	
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class WinForm( QWidget):  
	def __init__(self):  
		super(WinForm,self).__init__()  
		self.setWindowTitle("QMessageBox 例子")  
		self.resize(300, 200) 
		#layout = QHBoxLayout(self)		# 要在括号里面加上一个self，对这个变量进行布局
		layout = QVBoxLayout(self)	# 在Qt的Object工具栏处看相应的函数
		
		# 设置一个点击按钮；用于触发消息对话框
		self.myButton1 = QPushButton(self)   
		self.myButton1.setText("点击弹出消息框")  
		self.myButton1.clicked.connect(self.msg1)  
		layout.addWidget(self.myButton1)
		
		# 设置一个点击按钮；用于触发提问对话框
		self.myButton2 = QPushButton(self)    
		self.myButton2.setText("点击弹出提示框")  
		self.myButton2.clicked.connect(self.msg2)  
		layout.addWidget(self.myButton2)
		
		# 设置一个点击按钮；用于触发警告对话框
		self.myButton3 = QPushButton(self)    
		self.myButton3.setText("点击弹出警告对话框")  
		self.myButton3.clicked.connect(self.msg3)  
		layout.addWidget(self.myButton3)
		
		# 设置一个点击按钮；用于触发警告对话框
		self.myButton4 = QPushButton(self)    
		self.myButton4.setText("点击弹出严重错误对话框")  
		self.myButton4.clicked.connect(self.msg4)  
		layout.addWidget(self.myButton4)
		
		# 设置一个点击按钮；用于触发警告对话框
		self.myButton5 = QPushButton(self)    
		self.myButton5.setText("点击弹出关于对话框")  
		self.myButton5.clicked.connect(self.msg5)  
		layout.addWidget(self.myButton5)
		
	def msg1(self):  
        # 使用infomation信息框  
		reply = QMessageBox.information(self, "标题", "对话框消息正文", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )  
		print( reply )
		
	def msg2(self):  
        # 使用question信息框  
		reply = QMessageBox.question(self, "标题", "提问框消息正文", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )  
		print( reply )
		
	def msg3(self):  
        # 使用warning信息框  
		reply = QMessageBox.warning(self, "标题", "警告框消息正文", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )  
		print( reply )
	
	def msg4(self):  
        # 使用critical信息框  
		reply = QMessageBox.critical(self, "标题", "严重错误消息正文", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )  
		print( reply )
		
	def msg5(self):  
        # 使用warning信息框  
		reply = QMessageBox.about(self, "标题", "关于对话框")  
		print( reply )
if __name__ == '__main__':
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app= QApplication(sys.argv)    
	demo = WinForm()  
	demo.show() 
	sys.exit(app.exec_())
