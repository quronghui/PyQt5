# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QFontDialog 例子
# QFontDialog控件是一个常用的字体选择对话框，可以让用户选择所显示文本的字号大小、样式、格式、
# QFontDialog.getFont()函数：输出字体选择框；
# setFont(font)	：将目标字体设置为getFont()函数得到的字体；
# 2020.9.29
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FontDialogDemo(QWidget):
	def __init__(self, parent=None):
		super(FontDialogDemo, self).__init__(parent)
		
		layout = QVBoxLayout()		# 规定一个布局：垂直布局，和后面的setLayout对应
		
		self.fontButton  = QPushButton("choose font")	# 设置一个按键
		self.fontButton .clicked.connect(self.getFont)		# 连接到槽函数
		layout.addWidget(self.fontButton )						# 将此按钮显示在布局界面中
		
		self.fontLineEdit  = QLabel("Hello,测试字体例子")	# 添加一个lable标签
		layout.addWidget(self.fontLineEdit )					# 将标签进行显示
		
		self.setLayout(layout)	# 布局关联
		self.setWindowTitle("Font Dialog 例子")	#  设置标题名称
		
	def getFont(self):
		font, ok = QFontDialog.getFont()	# 获取字体
		if ok:
			self.fontLineEdit .setFont(font)	# 并将标签的字体设置为getFont
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = FontDialogDemo()
	demo.show()
	sys.exit(app.exec_())
