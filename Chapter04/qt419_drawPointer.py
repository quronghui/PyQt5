# -*- coding: utf-8 -*-
 
"""
    【简介】
# drawPointer：在窗体中绘画点的例子
#（1）绘制了[-100, 100]两个周期的正弦函数图像

# 2020.9.30
    
    
"""

import sys, math
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5 import QtCore

class Drawing(QWidget):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		self.resize(600, 200)  
		self.setWindowTitle("在窗体中画点")         
	
	# 绘制函数的方法必须在begin和end之间；
	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		# 自定义画点方法
		self.drawPoints(event, qp)
		qp.end()
		
	def drawPoints(self, event,  qp):
		qp.setPen( Qt.red)		# 设置红色画笔
		size = self.size()		# 获取当前窗口的大小，并在窗口中随机分布工作区中的点；
		
		for i in range(10000):	# 绘制10000个点，可以自己改变
			# [-100, 100]两个周期的正弦函数图像
			x = 100 *(-1+2.0*i/10000)+ size.width()/2.0
			y = -50 * math.sin((x - size.width()/2.0)*math.pi/50) + size.height()/2.0
			qp.drawPoint(x, y)		# 绘制点；

if __name__ == '__main__':
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	demo  = Drawing()
	demo.show()
	sys.exit(app.exec_())
