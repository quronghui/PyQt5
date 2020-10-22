# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QSpinBox 例子
# QSpinBox：计数器的控件，允许输入整数或者浮点数，通过上下箭头增加/减少当前的值；
#（1）QSpinBox 用于设置整数值，默认范围是0-99；
#（2）QDoubleSpinBox 用于设置浮点数；
#（3）还有一些其他功能的函数：用于补充实现计算器的功能；
#（4）setMinimum() ,setMaximum() 设置整数计数器的边界值；
#（5）setDecimals() 设置浮点计数器精度的位数

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class spindemo(QWidget):
	def __init__(self, parent=None):
		super(spindemo, self).__init__(parent)
		self.setWindowTitle("SpinBox 例子")
		self.resize(300, 100)
        
		layout = QVBoxLayout()		# 垂直布局；
		self.l1=QLabel("current value:")
		self.l1.setAlignment(Qt.AlignCenter)	# 设置位置为中间；
		self.l2=QLabel("")							# 添加一个标签2，用于显示 
		self.l2.setAlignment(Qt.AlignRight)	# 设置位置为右边；
		layout.addWidget(self.l1)
		layout.addWidget(self.l2)
		
		# 计数器控件：当值发生改变时，触发槽函数
		self.sp = QSpinBox()
		layout.addWidget(self.sp)
		# 设置范围;
		self.sp.setMinimum(-254)
		self.sp.setMaximum(255)
		self.sp.valueChanged.connect(self.valuechange)
		self.setLayout(layout)
		
		# 技术器控件：显示两位精度
		self.sp2 = QDoubleSpinBox()
		layout.addWidget(self.sp2)
		self.sp2.setDecimals(4)		# 设置精度位4位
		self.sp2.valueChanged.connect(self.valuechange2)
		self.setLayout(layout)
		      
		# str(self.sp.value()) 显示成人看的；对标签进行动态的显示
	def valuechange(self):	
		self.l1.setText("current value:" + str(self.sp.value()) )
	def valuechange2(self):	
		self.l2.setText("current value:" + str(self.sp2.value()) )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = spindemo()
	ex.show()
	sys.exit(app.exec_())
