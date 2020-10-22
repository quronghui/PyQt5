# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QDialog 例子
# QDialog控件：为了更好地实现人机交互，提供一系列的对话框完成特定场景下的功能；
# （1）WindowModality窗口的模态设置（三种模态），Qt.ApplicationModal不与其他窗口交互；只有关闭了所有的子窗口后才能关闭窗口
# （2）当用户按下Esc按键时，对话框窗口将会调用QDialog.reject()方法，用于关闭对话框
# （3）主窗口QMainWindow，通过一个自定义函数包含了子窗口QDialog;
# 2020.9.25
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class DialogDemo( QMainWindow ):

	def __init__(self, parent=None):
		super(DialogDemo, self).__init__(parent) 		
		self.setWindowTitle("Dialog 例子")
		self.resize(350,300)
		
		# 设置一个按键button；
		self.btn = QPushButton( self)
		self.btn.setText("弹出对话框")  
		self.btn.move(50,50)		# 起点的位置；
		self.btn.clicked.connect(self.showdialog)  
                
	def showdialog(self ):
		dialog = QDialog()			# 对话框dialog；
		btn = QPushButton("ok", dialog )	# 对话框里面显示的内容
		btn.move(50,50)
		dialog.setWindowTitle("Dialog")
		dialog.setWindowModality(Qt.ApplicationModal)	# 窗口的模态设置，Qt.ApplicationModal不与其他窗口交互；
		dialog.exec_()		# dialog运行完后，还要退出；

	

if __name__ == '__main__':
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	demo = DialogDemo()
	demo.show()
	sys.exit(app.exec_())
