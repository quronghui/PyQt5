# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中QButton例子
# 按钮类控件继承于QAbstractButton;
(1) 起到一个按钮的作用;可以采用lambda方式传递参数，将参数发给槽函数
(2) 设置一个图片作为按键: 使用setIcon()方法接收一个QPixmap对象的图像图件作为参数输入；
(3) 按键3：设置其不触发，显示就为灰色；可以作为还没有功能的按钮；
(4) 对按键设置快捷键：Alt+D 需要首字母为D并且前面有一个&符号；
  
'''
# 直接通过import*，省事
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):        # 类继承于QDialog（代表对话框类）
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		self.setWindowTitle("Button demo")
		layout = QVBoxLayout()		# 从上到下设置处置布局
		
        
        #  按键1：起到一个按钮的作用
		self.btn1 = QPushButton("Button1")	

		#setCheckable()设置按钮是否已被选中，如果设置为True，表示按钮将保持一点击和释放的状态；
		self.btn1.setCheckable(True)
		self.btn1.toggle()		# 通过toggle来切换按钮状态
		# 通过lambda方式传递参数，将参数发给槽函数
		self.btn1.clicked.connect(lambda:self.whichbtn(self.btn1) )
		# 直接连接槽函数
		self.btn1.clicked.connect(self.btnstate)
		layout.addWidget(self.btn1)
            
        # 按键2：设置一个图片作为按键
		self.btn2 = QPushButton('image')
		# 使用setIcon()方法接收一个QPixmap对象的图像图件作为参数输入；
		self.btn2.setIcon(QIcon(QPixmap("./images/python.jpg")))
		self.btn2.clicked.connect(lambda:self.whichbtn(self.btn2) )
		layout.addWidget(self.btn2)
		self.setLayout(layout) 

        # 按键3：setEnabled() 是否可以使用，设置其不触发，显示就为灰色；可以作为还没有功能的按钮；
		self.btn3 = QPushButton("Disabled")
		self.btn3.setEnabled(False)
		layout.addWidget(self.btn3)
        
        # 按钮4：设置快捷键，Alt+D 需要首字母为D并且前面有一个&符号；
		self.btn4= QPushButton("&Download")
		self.btn4.setDefault(True)
		self.btn4.clicked.connect(lambda:self.whichbtn(self.btn4))
		layout.addWidget(self.btn4)
        

	def btnstate(self):
		if self.btn1.isChecked():
			print("button pressed" ) 
		else:
			print("button released" ) 

	def whichbtn(self,btn):
		print("clicked button is " + btn.text() ) 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	btnDemo = Form()
	btnDemo.show()
	sys.exit(app.exec_())


