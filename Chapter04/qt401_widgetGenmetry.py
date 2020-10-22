# -*- coding: utf-8 -*-

'''
    【简介】
PyQt5中坐标系统
#四、widget界面控件：实现屏幕坐标系
#2020.9.21 

'''

from PyQt5.QtWidgets import QApplication  ,QWidget  ,QPushButton
import sys  
              
app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton( widget )
btn.setText("Button")
#以QWidget左上角为(0, 0)点
btn.move(20, 20)   
#不同操作系统可能对窗口最小宽度有规定，若设置宽度小于规定值，则会以规定值进行显示
widget.resize(300, 200) 
#以屏幕左上角为(0, 0)点
widget.move(250, 200)

widget.setWindowTitle('PyQt坐标系统例子')
widget.show()

# QWidget() 直接提供的成员函数，获取坐标
print("#1 QWidget")
print("widget.x()=%d" % widget.x() )
print("widget.y()=%d" % widget.y() )
print("widget.width()=%d" % widget.width() )
print("widget.height()=%d" % widget.height() )

# QWidget.geometry() 提供的成员函数，功能类似
print("#2 QWidget.geometry")
print("widget.geometry().x()=%d" %  widget.geometry().x() )
print("widget.geometry().y()=%d" %  widget.geometry().y() )
print("widget.geometry().width()=%d" %  widget.geometry().width() )
print("widget.geometry().height()=%d" %  widget.geometry().height() )
print("widget.size().width() =%d" %  widget.size().width() )
print("widget.size().height() =%d" %  widget.size().height() )

# QWidget.frameGeometry 获取包含标题栏和边框窗口的高度和宽度。
print("#3 QWidget.frameGeometry")
print("widget.frameGeometry().width()=%d" %  widget.frameGeometry().width() )
print("widget.frameGeometry().height()=%d" %  widget.frameGeometry().height() )
print("widget.pos().x()=%d" %  widget.pos().x() )
print("widget.pos().y()=%d" %  widget.pos().y() )

sys.exit(app.exec_())  



    
