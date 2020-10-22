# -*- coding: utf-8 -*-
 
"""
    【简介】
    绘图中QBrush 的例子 ,绘制九个不同样式的矩形。
（1）# 将Qprinter对象的画刷设置成QBrush对象
（2）# 调用drawRect()方法绘制矩形；

    
"""

import sys 
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 

class Drawing(QWidget): 
	def __init__(self):
		super().__init__()  
		self.initUI()			# 自定义函数：UI界面的一个显示

	def initUI(self):   
		self.setGeometry(300, 300, 365, 280)
		self.setWindowTitle('画刷例子')        
		self.show()

	def paintEvent(self, event): 	# 自定义的绘制事件paintEvent，需要在begin 和 end之间；
		qp = QPainter()
		qp.begin(self)
		self.drawLines(event, qp)
		qp.end()

	def drawLines(self, event, qp): 
		brush = QBrush(Qt.SolidPattern)
		qp.setBrush(brush)				# 将Qprinter对象的画刷设置成QBrush对象
		qp.drawRect(10, 15, 90, 60)		# 调用drawRect()方法绘制矩形；

		brush = QBrush(Qt.Dense1Pattern)
		qp.setBrush(brush)
		qp.drawRect(130, 15, 90, 60)

		brush = QBrush(Qt.Dense2Pattern)
		qp.setBrush(brush)
		qp.drawRect(250, 15, 90, 60)

		brush = QBrush(Qt.Dense3Pattern)
		qp.setBrush(brush)
		qp.drawRect(10, 105, 90, 60)

		brush = QBrush(Qt.DiagCrossPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 105, 90, 60)

		brush = QBrush(Qt.Dense5Pattern)
		qp.setBrush(brush)
		qp.drawRect(130, 105, 90, 60)

		brush = QBrush(Qt.Dense6Pattern)
		qp.setBrush(brush)
		qp.drawRect(250, 105, 90, 60)

		brush = QBrush(Qt.HorPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 195, 90, 60)

		brush = QBrush(Qt.VerPattern)
		qp.setBrush(brush)
		qp.drawRect(130, 195, 90, 60)

		brush = QBrush(Qt.BDiagPattern)
		qp.setBrush(brush)
		qp.drawRect(250, 195, 90, 60)
                         		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Drawing()
	demo.show()
	sys.exit(app.exec_())
