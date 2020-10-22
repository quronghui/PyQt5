# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QCalendarWidget 例子:是一个日历控件，提供了一个基于月份的视图
（1）月份、年份、日期的具体选择；
（2）并且通过setText对选择的日期进行显示；
（3）QCalendar的对象是通过QCalendarWidget类进行创建的；
（4）通过QDate()方法设置具体的日期；
（5）从窗口中选定一个日期，会发射一个QtCore.QDate信号，将此信号连接到用户的槽函数中；
（6） selectedDate()方法返回当前选定的日期，检索所选定的日期，并将日期对象转换为制定格式字符串；
（7）lable显示日期的时候：进行了两次日期的设置；
  
'''

import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class CalendarExample( QWidget):
	def __init__(self):
		super(CalendarExample, self).__init__()
		self.initUI()	# 自定义UI函数
		
	def initUI(self): 
		# QCalendar的对象是通过QCalendarWidget类进行创建的；
		self.cal =  QCalendarWidget(self)
		# 设置日期的最小值和最大值；通过QDate()方法设置具体的日期
		self.cal.setMinimumDate(QDate(1980, 1, 1))	
		self.cal.setMaximumDate(QDate(3000, 1, 1))
		self.cal.setGridVisible(True)		# setGridVisible()设置日历控件显示网格
		
		self.cal.move(20, 20)		# 设置了一个位置
		# 从窗口中选定一个日期，会发射一个QtCore.QDate信号，将此信号连接到用户的槽函数中；
		self.cal.clicked[QtCore.QDate].connect(self.showDate)
		
		self.lbl =  QLabel(self)	# 设置了标签控件：用于显示此时选择的日期
		# selectedDate()方法检索所选定的日期，并将日期对象转换为制定格式字符串；
		date = self.cal.selectedDate()
		self.lbl.setText(date.toString("yyyy-MM-dd dddd"))
		
		self.lbl.move(20, 300)
		self.setGeometry(100,100,400,350)	# 具体的坐标
		self.setWindowTitle('Calendar 例子')
		
	def showDate(self, date): 
		self.lbl.setText(date.toString("yyyy-MM-dd dddd") )		#date.toString设置当前的提起；
	

if __name__ == '__main__':
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	demo = CalendarExample()
	demo.show()
	sys.exit(app.exec_())
