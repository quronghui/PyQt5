# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 DateTimeEdit2 例子：
（1）实例：日期可以通过弹出框进行选择；
（2）DateTimeEdit2控件和按钮控件，当单击“获得日期和时间”
（3）setCalendarPopup：设置日期的选择为弹出框内进行选择；
（4）信号与槽函数的连接的函数模板：同样分为日期、日期和时间、时间，三种槽函数；
（5）获取日期、时间的函数模板；	
		
   
  
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,   QDateTime , QTime 

class DateTimeEditDemo(QWidget):	# 继承QWidget交互窗口类；
	def __init__(self):
		super(DateTimeEditDemo, self).__init__()
		self.initUI()	# 自定义UI函数；
		
	def initUI(self): 
		self.setWindowTitle('QDateTimeEdit例子')
		self.resize(300, 90)   
		
		# DateTimeEdit：日期和时间同时进行修改，并且设置其显示的格式；
		vlayout = QVBoxLayout()
		self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)	# 设置日期时间为本机此刻的值
		self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
		
        # 设置最小日期：365天的范围
		self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365)) 
        # 设置最大日期：
		self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365)) 
		self.dateEdit.setCalendarPopup( True)	# setCalendarPopup：设置日期的选择为弹出框内进行选择；
		
		# 信号与槽函数的连接：同样分为日期、日期和时间、时间，三种槽函数；
		self.dateEdit.dateChanged.connect(self.onDateChanged) 
		self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged) 
		self.dateEdit.timeChanged.connect(self.onTimeChanged) 
		
		# 设置一个按钮点击事件
		self.btn = QPushButton('获得日期和时间')  
		self.btn.clicked.connect(self.onButtonClick) 
        
		vlayout.addWidget( self.dateEdit )
		vlayout.addWidget( self.btn )
		self.setLayout(vlayout)   

	#  信号与槽函数	
	def onDateChanged(self , date):
		print(date)
	
	# 无论日期还是时间发生改变，都会执行
	def onDateTimeChanged(self , dateTime ):
		print(dateTime)
			
	# 时间发生改变时执行
	def onTimeChanged(self , time):
		print(time)			
	
	# 输出此时的选择
	def onButtonClick(self ):     
	# 获取日期、时间的函数；	
		dateTime  = self.dateEdit.dateTime()
		# 最大日期
		maxDate = self.dateEdit.maximumDate() 
		# 最大日期时间
		maxDateTime = self.dateEdit.maximumDateTime() 
		# 最大时间
		maxTime = self.dateEdit.maximumTime() 
		# 最小日期
		minDate = self.dateEdit.minimumDate() 
		# 最小日期时间
		minDateTime = self.dateEdit.minimumDateTime() 
		# 最小时间	
		minTime = self.dateEdit.minimumTime() 
		 
		print('\n选择日期时间'  )  	
		print('dateTime=%s' % str(dateTime) ) 
		print('maxDate=%s' % str(maxDate) ) 
		print('maxDateTime=%s' % str(maxDateTime) ) 
		print('maxTime=%s' % str(maxTime) ) 
		print('minDate=%s' % str(minDate) ) 
		print('minDateTime=%s' % str(minDateTime) ) 
		print('minTime=%s' % str(minTime) ) 
		              
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DateTimeEditDemo()
	demo.show()
	sys.exit(app.exec_())
