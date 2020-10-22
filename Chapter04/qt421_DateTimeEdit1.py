# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 DateTimeEdit1 例子：提供日期和时间格式的修改
（1） DateEdit、 DateTimeEdit、 TimeEdit：分别对应着日期、日期时间、时间，三种方式的修改；
（2）DateTimeEdit 通过 setDisplayFormat()函数设置显示的日期时间格式；
   
  
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,   QDateTime , QTime 

class DateTimeEditDemo(QWidget):
	def __init__(self):
		super(DateTimeEditDemo, self).__init__()
		self.initUI()		# 设置UI自定义函数；
		
	def initUI(self): 
		self.setWindowTitle('QDateTimeEdit例子')
		self.resize(300, 90)   	# 设置窗口的大小

		vlayout = QVBoxLayout()	# 设置布局为垂直
		
		dateTimeEdit = QDateTimeEdit(self)	# QDateTimeEdit ：默认的日期和时间
		dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime(), self)	# 设置日期时间为本机此刻的日期和时间；
		dateEdit = QDateTimeEdit(QDate.currentDate(), self)	# 只设置日期为本机日期
		timeEdit = QDateTimeEdit(QTime.currentTime(), self)	# 只设置时间为本机时间

		# 通过 setDisplayFormat() 函数，设置日期时间格式
		dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")		# 两种不同的格式
		dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
		dateEdit.setDisplayFormat("yyyy.MM.dd")
		timeEdit.setDisplayFormat("HH:mm:ss")
                
		# 添加到框架内显示
		vlayout.addWidget( dateTimeEdit )
		vlayout.addWidget( dateTimeEdit2)
		vlayout.addWidget( dateEdit )
		vlayout.addWidget( timeEdit )		
		
		self.setLayout(vlayout)   
        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DateTimeEditDemo()
	demo.show()
	sys.exit(app.exec_())
