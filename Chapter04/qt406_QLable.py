# -*- coding: utf-8 -*- 

'''
# Lable 标签的使用：作为纯文本、链接、图片等显示
# （1）重点是lable作为超链接的使用
#2020.9.23
'''

import sys
from PyQt5.QtWidgets import QApplication,  QLabel,  QWidget,  QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel 例子")
		
        
        
        # 1 lable
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        
        # 2 初始化标签控件
        label1.setText("这是一个文本标签")
        label1.setAutoFillBackground(True)
        palette = QPalette()   
        palette.setColor(QPalette.Window,Qt.blue)  
        label1.setPalette(palette) 
        label1.setAlignment( Qt.AlignCenter)    # lable方法，按照固定值方式对齐文本
        
        # 3 lable 可以插入链接
        label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")
        
        # 4 lable 插入图片
        label3.setAlignment( Qt.AlignCenter)    
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap( QPixmap("./images/python.png"))
        
        #5 lable插入超链接
        label4.setText("<A href='https://luckywater.top/'>欢迎访问信平的小屋</a>")
        label4.setAlignment( Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')
        
        
        # 6 在窗口布局中添加控件
        vbox = QVBoxLayout(self)
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget( label3 )
        vbox.addStretch()
        vbox.addWidget( label4)
        
        #7 允许lable1控件访问超链接
        label1.setOpenExternalLinks(True)
        # 打开允许访问超链接,默认是不允许，需要使用 setOpenExternalLinks(True)允许浏览器访问超链接
        label4.setOpenExternalLinks( False )
        # 点击文本框绑定槽事件  
        label4.linkActivated.connect( link_clicked )
        
         # 滑过文本框绑定槽事件       
        label2.linkHovered.connect( link_hovered )
        label1.setTextInteractionFlags( Qt.TextSelectableByMouse )
               
def link_hovered():
    print("当鼠标滑过label-2标签时，触发事件。")
        
def link_clicked():
    print("当鼠标点击label-4标签时，触发事件。" )
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())
