# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QFileDialog 例子

# QFileDialog 用于打开和保存文件的标准对话框，同样是继承自QDialog
#（1） getOpenFileName()调用文件对话框显示图像；
		# self：显示父组件；第二个参数：对话框的标题；第三个参数：对话框显示默认打开的目录；第四个参数：相当于过滤器filter
#（2）QFileDialog()	文件对话框的对象exec_()方法来选择文件，并将文件的内容显示在文本编辑控件中；
		# 显示文件里面的内容，有相关的代码。
#（3）Pixmap()函数：加载并呈现本地图像
# 2020.9.29
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class filedialogdemo(QWidget):
	def __init__(self, parent=None):
		super(filedialogdemo, self).__init__(parent)
		
		layout = QVBoxLayout()		# 垂直布局 ，后面有对应；
		self.btn = QPushButton("加载图片")		# 按键操作，连接getfile槽函数
		self.btn.clicked.connect(self.getfile)
		layout.addWidget(self.btn)					# 将其显示在界面中；
		
		self.le = QLabel("")	# 添加一个空白标签lable，占位符用于显示图片；
		layout.addWidget(self.le)	# 将lable同样显示在标签中；
		
		self.btn1 = QPushButton("加载文本文件")	# 另外一个按键，同样连接到槽函数getfiles
		self.btn1.clicked.connect(self.getfiles)
		layout.addWidget(self.btn1)					# 并将其显示在界面
		
		self.contents = QTextEdit()						# 可编辑框，显示
		layout.addWidget(self.contents)
		
		self.setLayout(layout)	# 布局控制
		self.setWindowTitle("File Dialog 例子") 	# 标题
	
	# 加载一张图片.jpg和、gif
	def getfile(self):
		# getOpenFileName()调用文件对话框显示图像；
		# self：显示父组件；第二个参数：对话框的标题；第三个参数：对话框显示默认打开的目录；第四个参数：相当于过滤器filter
		fname, _  = QFileDialog.getOpenFileName(self, 'Open file', 'd:\\',"Image files (*.jpg *.gif *.png)")
		self.le.setPixmap(QPixmap(fname))	# 图片设置
	
	# 一个文本文件打开
	def getfiles(self):
		dlg = QFileDialog()	# 文件对话框的对象exec_来选择文件，并将文件的内容显示在文本编辑控件中；
		dlg.setFileMode(QFileDialog.AnyFile)	# setFileMode 设置可选文件的类型，枚举常量；
		dlg.setFilter( QDir.Files  )
	
		if dlg.exec_():
			filenames= dlg.selectedFiles()	# 选择文件
			f = open(filenames[0], 'r') 		# 打开文件；
            
			with f:
				data = f.read()				# 文件只读；
				self.contents.setText(data) 
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = filedialogdemo()
	ex.show()
	sys.exit(app.exec_())
