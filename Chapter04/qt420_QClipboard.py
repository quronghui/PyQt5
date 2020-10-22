# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QClipboard 例子:对系统剪切板的访问，可以在应用程序之间复制和粘贴数据；
（1）通过QLabel显示文本和图片；
（2）按钮进行点击事件：对不同的呢MIME数据类型进行复制和粘贴；
（3）文本数据(Text)、图像数据(Image)、网页数据（HTML）;
（4）当剪切板内容发生变化的时候，dataChange信号被发射；
  
'''

import os
import sys
from PyQt5.QtCore import  QMimeData 
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,QPushButton)
from PyQt5.QtGui import QPixmap

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		
		# 设置按钮控件
		textCopyButton = QPushButton("&Copy Text")
		textPasteButton = QPushButton("Paste &Text")
		htmlCopyButton = QPushButton("C&opy HTML")
		htmlPasteButton = QPushButton("Paste &HTML")
		imageCopyButton = QPushButton("Co&py Image")
		imagePasteButton = QPushButton("Paste &Image")
		# 设置标签控件
		self.textLabel = QLabel("Original text")	# 用于显示文本
		self.imageLabel = QLabel()							# 用于显示图片
		# 设置image图像的路径？
		self.imageLabel.setPixmap(QPixmap(os.path.join(
		os.path.dirname(__file__), "images/clock.png")))	# 注意图片的格式
		
		# 栅格布局
		layout = QGridLayout(self)
		layout.addWidget(textCopyButton, 0, 0)
		layout.addWidget(imageCopyButton, 0, 1)
		layout.addWidget(htmlCopyButton, 0, 2)
		layout.addWidget(textPasteButton, 1, 0)
		layout.addWidget(imagePasteButton, 1, 1)
		layout.addWidget(htmlPasteButton, 1, 2)
		layout.addWidget(self.textLabel, 2, 0, 1, 2)
		layout.addWidget(self.imageLabel, 2, 2)
		self.setLayout(layout)
		
		# 连接槽函数
		textCopyButton.clicked.connect(self.copyText)
		textPasteButton.clicked.connect(self.pasteText)
		htmlCopyButton.clicked.connect(self.copyHtml)
		htmlPasteButton.clicked.connect(self.pasteHtml)
		imageCopyButton.clicked.connect(self.copyImage)
		imagePasteButton.clicked.connect(self.pasteImage)
		self.setWindowTitle("Clipboard 例子")
		
	def copyText(self):	  # 文本的复制：需要将文本复制到clipboard对象中；
		clipboard = QApplication.clipboard()
		clipboard.setText("I've been clipped!")
	
	def pasteText(self):
		clipboard = QApplication.clipboard()
		self.textLabel.setText(clipboard.text())
	
	def copyImage(self):
		clipboard = QApplication.clipboard()
		clipboard.setPixmap(QPixmap(os.path.join(
		os.path.dirname(__file__), "./images/python.png")))
	
	def pasteImage(self):
		clipboard = QApplication.clipboard()
		self.imageLabel.setPixmap(clipboard.pixmap())
	
	def copyHtml(self):
		mimeData = QMimeData()
		mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
		clipboard = QApplication.clipboard()
		clipboard.setMimeData(mimeData)
	
	def pasteHtml(self):
		clipboard = QApplication.clipboard()
		mimeData = clipboard.mimeData()
		if mimeData.hasHtml():
			self.textLabel.setText(mimeData.html())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	sys.exit(app.exec_())
