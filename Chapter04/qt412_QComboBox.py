# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QComboBox 例子
	
# QComboBox是一个集按钮和下拉选项于一体的控件，也被成为下拉类表框；
#（1）addItem()添加单个选项； addItems()添加多个选项；
#（2）添加了for循环；而且循环的数目是可以在内部显示的；
#（3）下拉选项进行选择，当选中某一选项时，将该文本设置成标签文本；
#（4）count（）返回下拉选项集合中的数目；
#2020.9.24
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ComboxDemo(QWidget):		# 类继承
	def __init__(self, parent=None):
		super(ComboxDemo, self).__init__(parent)
		self.setWindowTitle("combox 例子")        
		self.resize(300, 90)     # 设置界面大小
		
		layout = QVBoxLayout()		# 布局和一个标签框
		self.lbl = QLabel("Programming Language" )  	# 标签是要给显示标签
         
		# currentIndexChanged下拉信号索引发生改变；
		self.cb = QComboBox() 		
		self.cb.addItem("C")			# addItem()添加单个选项
		self.cb.addItem("C++")
		self.cb.addItems(["Java", "C#", "Python"])	# addItems()添加多个选项
		self.cb.currentIndexChanged.connect(self.selectionchange)	
		# 将容器布局的内容显示
		layout.addWidget(self.cb)	
		layout.addWidget(self.lbl )
		self.setLayout(layout)
                                    
	def selectionchange(self,i):
		# 当选中某一选项时，将该文本设置成标签文本
		# currentText 返回选中选项的文本；
		self.lbl.setText( self.cb.currentText() )
		self.lbl.adjustSize()
		
		print( "Items in the list are :" )
		for count in range(self.cb.count()):		# for循环；但是count是怎么来的呢？
			print( 'item'+str(count) + '='+ self.cb.itemText(count) )
			print( "Current index",i,"selection changed ",self.cb.currentText() )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	comboxDemo = ComboxDemo()
	comboxDemo.show()
	sys.exit(app.exec_())
