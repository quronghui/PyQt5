# -*- coding: utf-8 -*-
 
"""
    【简介】
    在窗体中绘画出文字的例子
# （1）drawText()方法显示给定坐标处的文字；
#（2）setPen()设置画笔的颜色；
#（3）setFont()设置字体大小；
#（4）def paintEvent(self,event)定义了一个绘制事件： QtGui.QPainter 类负责所有低级别的绘制，所有绘制的事件都在此内（begin—end）
# 2020.9.30
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import QPainter ,QColor ,QFont
from PyQt5.QtCore import Qt 
from PyQt5 import QtCore

class Drawing(QWidget):
	def __init__(self,parent=None):
		super(Drawing,self).__init__(parent)
		self.setWindowTitle("在窗体中绘画出文字例子") 
		
		self.resize(300, 200)        # 设置一个文本显示标签；
		self.text = '欢迎学习 PyQt5'
         
	#定义了一个绘制事件： QtGui.QPainter 类负责所有低级别的绘制，所有绘制的事件都在此内（begin—end）
	def paintEvent(self,event):	# 自定义公有函数
		painter = QPainter(self)   	#    QPainter对象；  
		painter.begin(self)				# 绘制方法需要在对象 begin 和 end 之间；
        # 自定义的绘画方法
		self.drawText(event, painter)	
		painter.end()
	
	# 设置文本的字体和颜色；
	def drawText(self, event, qp):
        # 设置笔的颜色
		#qp.setPen( QColor(168, 34, 3) )
		qp.setPen( QColor(0, 0, 0) )	# 设置为黑色
        # 设置字体
		qp.setFont( QFont('SimSun', 10))
        # 画出文本：drawText()方法显示给定坐标处的文字；
		qp.drawText(event.rect(), Qt.AlignCenter, self.text)	# 绘制出文本内容；
		
if __name__ == "__main__":  
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv) 
	demo = Drawing()
	demo.show()
	sys.exit(app.exec_())
