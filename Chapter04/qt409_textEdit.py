# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QTextEdit例子  
# QTextEdit类是一个多行文本框控件，可以显示多行文本内容，可以显示垂直滚动条；    
# （1）自定义函数：实现按键按下后能够显示文本
# （2）自定义函数：实现按键按下后能够显示HTML文档；
# 2020.9.24
'''
import sys  
from PyQt5.QtWidgets import QApplication,  QWidget ,  QTextEdit, QVBoxLayout , QPushButton


class TextEditDemo(QWidget):
	def __init__(self, parent=None):
		super(TextEditDemo, self).__init__(parent)
		self.setWindowTitle("QTextEdit 例子")
        
		self.resize(300, 270)         # 窗口的大小
        
		self.textEdit = QTextEdit( )      # QTextEdit文本框的控件
		self.btnPress1 = QPushButton("显示文本")	# 两个按钮控件
		self.btnPress2 = QPushButton("显示HTML")    
        
		layout = QVBoxLayout()      # 从上到下垂直布局
		layout.addWidget(self.textEdit)
		layout.addWidget(self.btnPress1)   
		layout.addWidget(self.btnPress2)   		
		self.setLayout(layout)         
		# button 按钮：完成信号和槽函数的连接
		self.btnPress1.clicked.connect(self.btnPress1_Clicked)
		self.btnPress2.clicked.connect(self.btnPress2_Clicked)
		
    # 自定义函数：实现按键按下后能够显示文本
	def btnPress1_Clicked(self):
		self.textEdit.setPlainText("Hello PyQt5!\n点击按钮")
    # 自定义函数：实现按键按下后能够显示HTML文档；
	def btnPress2_Clicked(self):
		self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\n点击按钮。</font>")
		
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = TextEditDemo()	
	win.show()	
	sys.exit(app.exec_())
