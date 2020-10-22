# -*- coding: UTF-8 -*-

"""
# 创建一个PyQt的应用：只显示一个界面；
#2020.9.23
    
"""

# Qt5中使用的GUI窗口控件都在这两个模块中；
import sys
from PyQt5.QtWidgets import QApplication, QWidget   

app = QApplication(sys.argv)    # PyQt5程序都需要有一个QApplication对象；sys.argv命令行参数列表

window = QWidget()          # QWidget 是PyQt5中所有用户界面的父类；

window.resize(300, 200)     # resize 标识可以改变窗口控件的大小；
window.move(250, 150)     # move 设置窗口的初始位置；

window.setWindowTitle('Hello PyQt5')    # GUI窗口的标题

window.show()       # 窗口控件显示在屏幕上；

sys.exit(app.exec_())       # 进入程序的主循环，通过sys.exit保证程序完整的结束；
                                        # exec_()返回值为0，表示是程序运行成功，底层是C++;
