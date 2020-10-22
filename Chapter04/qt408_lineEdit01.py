'''
# PyQt5中 QLineEdit.EchoMode效果例子     
# (1) 可以再lineEidt 文本框内设置在提示词
（2）# setPlaceholderText：设置文本框浮显字符，起到提示作用，当输入后消失；
（3）	# setEchoMode：设置文本框显示格式，允许输入的文本显示格式有具体的格式要求；
		# QLineEdit.Normal：正常显示所输入的字符，默认选项；
		# QLineEdit.NoEcho：不显示任何输入字符，常用于密码类型的输入，且其密码长度需要保密时；
		# QLineEdit.Password：显示与平台相关的密码掩码字符，而不是实际输入的字符；
		# QLineEdit.PasswordEchoOnEdit：在编辑时显示字符，负责显示密码类型的输入；
#2020.9.23
'''
import sys 
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
 
 
class lineEditDemo(QWidget):    # 对象lineEditDemo继承于QWidget
	def __init__(self, parent=None):    # 一个.py只有一个init函数，用于初始化
    
        # 1 必备的，有这个才能显示
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("QLineEdit例子")
        
		flo = QFormLayout()     # 表单布局，类似于表格布局，四个lineEdit
		pNormalLineEdit = QLineEdit( )
		pNoEchoLineEdit = QLineEdit()
		pPasswordLineEdit = QLineEdit( )
		pPasswordEchoOnEditLineEdit = QLineEdit( )
        
        # 2 设置左边类似于标签的显示
		flo.addRow("Normal", pNormalLineEdit)
		flo.addRow("NoEcho", pNoEchoLineEdit)
		flo.addRow("Password", pPasswordLineEdit)
		flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEditLineEdit)
        
        
        # 3. 在文本编辑框里面添加提示词；
		# setPlaceholderText：设置文本框浮显字符，起到提示作用，当输入后消失；
		pNormalLineEdit.setPlaceholderText("Normal")
		pNoEchoLineEdit.setPlaceholderText("NoEcho")
		pPasswordLineEdit.setPlaceholderText("Password")
		pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

		# 设置显示效果：没看出有啥改变；
		# setEchoMode：设置文本框显示格式，允许输入的文本显示格式有具体的格式要求；
		# QLineEdit.Normal：正常显示所输入的字符，默认选项；
		# QLineEdit.NoEcho：不显示任何输入字符，常用于密码类型的输入，且其密码长度需要保密时；
		# QLineEdit.Password：显示与平台相关的密码掩码字符，而不是实际输入的字符；
		# QLineEdit.PasswordEchoOnEdit：在编辑时显示字符，负责显示密码类型的输入；
		pNormalLineEdit.setEchoMode(QLineEdit.Normal)
		pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
		pPasswordLineEdit.setEchoMode(QLineEdit.Password)
		pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
		                    
		self.setLayout(flo)
                    
   
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())

