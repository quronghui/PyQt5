# -*- coding: utf-8 -*-

'''
    【简介】
  PyQt5中 QLineEdit例子
# 文本编辑器的综合例子；
#（1）setValidator：设置文本的验证器，规定文本使用字体、右对齐，允许输入整数
#（2）限制小数点后两位：0.99 ——99.99
#（3）设置输入得掩码：应用于电话号码
#（4）设置发射信号连接到槽函数
#（5）设置一个只显示的文本框
#（6）连接到槽函数，一旦用户按下回车，该函数就会执行
# 2020.9.23    
  
'''
import sys  
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
from PyQt5.QtGui import QIntValidator , QDoubleValidator , QFont
from PyQt5.QtCore import Qt


class lineEditDemo(QWidget):        # 对象lineEditDemo继承于QWidget
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
        
        # 1 e1 ：显示文本使用字体、右对齐，允许输入整数
		# setValidator：设置文本的验证器，文本的限制
		# setAlignment：设置文本的对齐方式；
		e1 = QLineEdit()
		e1.setValidator( QIntValidator() )  # QIntValidator 设置输入整数
		e1.setMaxLength(4)                      # 最大输入长度
		e1.setAlignment( Qt.AlignRight )    # 右对齐
		e1.setFont( QFont("Arial",20))         # 字体
        
        # e2  限制小数点后两位：0.99 ——99.99
		e2 = QLineEdit()
		e2.setValidator( QDoubleValidator(0.99,99.99,2))    # QDoubleValidator限制输入浮点数
		flo = QFormLayout()
		flo.addRow("integer validator", e1)
		flo.addRow("Double validator",e2)
        
        # 3 设置输入得掩码：应用于电话号码
		e3 = QLineEdit()
		e3.setInputMask('+99_9999_9999999')
		flo.addRow("Input Mask",e3)
        # 4 设置发射信号连接到槽函数
		e4 = QLineEdit()
		e4.textChanged.connect( self.textchanged )
		flo.addRow("Text changed",e4)
        # 设置显示模式为密码模式，
		e5 = QLineEdit()
		e5.setEchoMode( QLineEdit.Password )
		flo.addRow("Password",e5)
        # 设置一个只显示的文本框
		e6 = QLineEdit("Hello PyQt5")
		e6.setReadOnly(True)
		flo.addRow("Read Only",e6 )
        
        # e5 连接到槽函数，一旦用户按下回车，该函数就会执行
		e5.editingFinished.connect( self.enterPress )
		self.setLayout(flo)
		self.setWindowTitle("QLineEdit例子")
	
	def textchanged(self, text):
		print( "输入的内容为: "+text )

	def enterPress( self ):
		print( "已输入值" )

   
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())
