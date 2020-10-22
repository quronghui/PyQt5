# -*- coding: utf-8 -*- 
'''
    【简介】
   三、 PyQT5中关闭窗体例子
(1) 窗口可以进行关闭
 # 2020.9.21
  
'''

from PyQt5.QtWidgets import QMainWindow,QHBoxLayout, QPushButton ,  QApplication, QWidget  
import sys 

class WinForm(QMainWindow):  
	
	def __init__(self, parent=None):        # 桌面控件实现
		super(WinForm, self).__init__(parent)
		self.resize(330,  100)  
		self.setWindowTitle('关闭主窗口例子') 		
		self.button1 = QPushButton('关闭主窗口')  		
		self.button1.clicked.connect(self.onButtonClick)    # 信号与槽函数的连接
		layout = QHBoxLayout()  
		layout.addWidget(self.button1)  
        
		main_frame = QWidget()  	# 这属于子窗口；
		
		main_frame.setLayout(layout)    
		self.setCentralWidget(main_frame)  
    
    # 槽函数onButtonClick：获取QApplication类的对象；发送对象是其名字；
	def onButtonClick(self ):  
        #sender 是发送信号的对象，此处发送信号的对象是button1按钮 
		sender = self.sender()         
		print( sender.text() + ' 被按下了' )    # text()函数：获取显示的名称；print()输出可以在Timenal串口里面查看信息
		qApp = QApplication.instance()
		qApp.quit()
		
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
