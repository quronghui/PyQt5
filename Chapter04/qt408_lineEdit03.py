# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QLineEdit的输入掩码例子     
    
# （1）限制用户的输入，出了使用验证器，还可以使用输入掩码；
# （2）IP, MAC, 日期, 许可证
# 2020.9.23
  
'''
import sys 
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
class lineEditDemo(QWidget):
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("QLineEdit的输入掩码例子")
        
        # 1 文本编辑器和布局：表单布局；
		flo = QFormLayout()          		
		pIPLineEdit = QLineEdit()
		pMACLineEdit = QLineEdit()
		pDateLineEdit = QLineEdit()
		pLicenseLineEdit = QLineEdit()		
        
        # 2, 设置setInputMask掩码
		pIPLineEdit.setInputMask("000.000.000.000;_")
		pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
		pDateLineEdit.setInputMask("0000-00-00")
		pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")
        
        #3 界面左边具体的显示栏
		flo.addRow("数字掩码", pIPLineEdit)
		flo.addRow("Mac掩码", pMACLineEdit)
		flo.addRow("日期掩码", pDateLineEdit)
		flo.addRow("许可证掩码", pLicenseLineEdit)
        
        # pIPLineEdit.setPlaceholderText("111")
        # pMACLineEdit.setPlaceholderText("222")
        # pLicenseLineEdit.setPlaceholderText("333")
        # pLicenseLineEdit.setPlaceholderText("444")

		self.setLayout(flo)                        
   
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())

 
