# -*- coding: utf-8 -*-
 
"""
【简介】QPen：是一个基本的图形对象，用于绘制直线、曲线、轮廓画出矩形、椭圆形、多边形和其他形状。
# 绘图中QPen 的例子 ,绘制使用不同样式的6条线
#（1）
    
"""

import sys 
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 

class Drawing(QWidget):
	#def __init__(self):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		# super().__init__()
		self.initUI()	# 	构造函数的窗口显示
		
	# 通过initUI函数：显示窗口的大小和标题
	def initUI(self):   
		self.setGeometry(300, 300, 280, 270)
		self.setWindowTitle('钢笔样式例子')        
	
	# 定义一个绘制事件：在begin—end之间
	def paintEvent(self, event): 	# e 和 event 是一样的作用
		qp = QPainter()
		qp.begin(self)
		self.drawLines(event, qp)
		qp.end()
	
	# 绘制线函数
	def drawLines(self, event, qp):
		pen = QPen(Qt.black, 2, Qt.SolidLine)	# 穿件了QPen对象。黑色、2像素、SolidLine预定义线条样式；
			
		# 预定义的线条样式：5类；
		# 类1：黑色，solidLine 一条简单的线
		qp.setPen(pen)
		qp.drawLine(20, 40, 250, 40)
		
		# 类2：DashLine：由像素分隔的短线
		pen.setStyle(Qt.DashLine)
		qp.setPen(pen)
		qp.drawLine(20, 80, 250, 80)
		
		#类3：DashDotLine：轮流交替的点和短线；
		pen.setStyle(Qt.DashDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 120, 250, 120)
		
		#类4：DotLine：有一些像素分割的点
		pen.setStyle(Qt.DotLine)
		qp.setPen(pen)
		qp.drawLine(20, 160, 250, 160)
		
		# 类5：DashDotDotLine 一条短线、两个点
		pen.setStyle(Qt.DashDotDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 200, 250, 200)
		
		#类6：CustomDashLine自定义的线条样式；
		# setDashPattern()方法使用数字列表定义样式：列表中个数必须是偶数
		# 1—像素宽度的横线，4—像素宽度的空余距离
		pen.setStyle(Qt.CustomDashLine)
		pen.setDashPattern([1, 4, 5, 4])
		qp.setPen(pen)
		qp.drawLine(20, 240, 250, 240)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Drawing()
	demo.show()
	sys.exit(app.exec_())
