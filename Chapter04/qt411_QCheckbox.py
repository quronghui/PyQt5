# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QCheckBox 例子——多选多
	# 提供了一组带文本标签的复选框，用户可以选择多个选项；
	# （1）setTristate()函数提供三种状态的选择；0-选中，Qt.PartiallyChecked 属于半选中状态；
	# （2）isChecked() 查询是否被选中；checkState() 选中的状态（0, 1,2）
	# （3）str() 函数将对象转化为适于人阅读的形式
	# （4）只要复选框被选中或者取消，都会发射stateChanged信号；
# 2020.9.24
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class CheckBoxDemo(QWidget):	# 继承QWidget类—对话框的类

	def __init__(self, parent=None):
		super(CheckBoxDemo , self).__init__(parent)
		
		# QGroupBox将多个复选框添加到一个水平布局管理器中，并添加到groupBox组里面
		groupBox = QGroupBox("Checkboxes")
		groupBox.setFlat( False )
		
		# 复选框1：提供了快捷键Alt+C;一开始的状态是选上的；
		# 只要复选框被选中或者取消，都会发射stateChanged信号；
		# setChecked设置复选框的状态，true为选中状态；
		layout = QHBoxLayout()		# 空间布局
		self.checkBox1= QCheckBox("&Checkbox1")	
		self.checkBox1.setChecked(True)
		self.checkBox1.stateChanged.connect( lambda:self.btnstate(self.checkBox1) )
		layout.addWidget(self.checkBox1)		# 显示这个控件
        
		# 复选框2：直接连接到槽函数btnstate
		# toggled() 状态发生改变时，进行变化;
		self.checkBox2 = QCheckBox("Checkbox2")
		self.checkBox2.toggled.connect( lambda:self.btnstate(self.checkBox2) )
		layout.addWidget(self.checkBox2)	# 加入这个容器中的东西
		
		# 复选框3：三种状态的选择
		# setTristate：设置此复选框有三种状态；0-选中
		# setCheckState：设置复选框的状态，Qt.PartiallyChecked 属于半选中状态；
		self.checkBox3 = QCheckBox("tristateBox")
		self.checkBox3.setTristate(True)
		self.checkBox3.setCheckState(Qt.PartiallyChecked )		
		self.checkBox3.stateChanged.connect( lambda:self.btnstate(self.checkBox3) )
		layout.addWidget(self.checkBox3)
        
		# groupBox组的一个布局；
		groupBox.setLayout(layout)
		mainLayout = QVBoxLayout()	# 水平布局
		mainLayout.addWidget(groupBox)
		
		self.setLayout(mainLayout)
		self.setWindowTitle("checkbox demo")
	
	# isChecked() 查询是否被选中；checkState() 选中的状态（0, 1,2）
	# str() 函数将对象转化为适于人阅读的形式
	def btnstate(self,btn ):
		chk1Status = self.checkBox1.text()+", isChecked="+  str( self.checkBox1.isChecked() ) + ', chekState=' + str(self.checkBox1.checkState())   +"\n"		 
		chk2Status = self.checkBox2.text()+", isChecked="+  str( self.checkBox2.isChecked() ) + ', checkState=' + str(self.checkBox2.checkState())   +"\n"	
		chk3Status = self.checkBox3.text()+", isChecked="+  str( self.checkBox3.isChecked() ) + ', checkState=' + str(self.checkBox3.checkState())   +"\n"			
		print(chk1Status + chk2Status + chk3Status )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	checkboxDemo = CheckBoxDemo()
	checkboxDemo.show()
	sys.exit(app.exec_())
