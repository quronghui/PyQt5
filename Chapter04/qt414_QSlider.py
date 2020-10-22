# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QSlider 例子
	
# QSlider：提供了一个垂直或者水平的滑动条；
#（1）设置一个标签，并且设置其位置为中间；
#（2）根据此时滑块value值的大小，设置标签的字号；
#（3）QSlider 相比计算器显示更加的明显
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SliderDemo(QWidget):
	def __init__(self, parent=None):
		super(SliderDemo, self).__init__(parent)
		self.setWindowTitle("QSlider 例子")  
		self.resize(300, 100)
        
		# 设置一个标签，并且设置其位置为中间；
		layout = QVBoxLayout()
		self.l1 = QLabel("Hello PyQt5")
		self.l1.setAlignment(Qt.AlignCenter)
		layout.addWidget(self.l1)
		
        # 水平方向
		self.sl = QSlider(Qt.Horizontal)
        #设置最小值
		self.sl.setMinimum(10)
		#设置最大值
		self.sl.setMaximum(50)
		# 步长
		self.sl.setSingleStep( 3 ) 
		# 设置当前值
		self.sl.setValue(20)
		# 刻度位置，刻度在下方
		self.sl.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
		self.sl.setTickInterval(5)
		layout.addWidget(self.sl)
        
		# 连接信号槽
		self.sl.valueChanged.connect(self.valuechange)
		self.setLayout(layout)
                      
	def valuechange(self):
		# 这两种print都可以；
		print('current slider value=%s' % self.sl.value() )
		print('current slider value= ',  str(self.sl.value()) )
		# 根据此时滑块value值的大小，设置标签的字号
		size = self.sl.value()
		self.l1.setFont(QFont("Arial",size))
                      
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = SliderDemo()
	demo.show()
	sys.exit(app.exec_())
