# 一、创建主窗口QMainWindow
# 1. 通过QMainWindow中的方法进行创建，之前是通过qt创建的，对应的方法里面也有；
# 2. 问题：由于逗号切换成中文的，一直在报错。
# 2020.9.21

import sys
from PyQt5.QtWidgets import QMainWindow,  QApplication
from PyQt5.QtGui import  QIcon

class MainWindow(QMainWindow):  # 对象名是QMainWindow
    def __init__(self, parent=None):       
        super(MainWindow, self).__init__(parent)    # 使用super()初始化窗口
        self.resize(400, 200)
        self.status = self.statusBar()  # 由statusBar产生状态栏
        self.status.showMessage("这是状态栏提示", 5000) # 显通过showMessage显示消息消息，延时5秒
        self.setWindowTitle("PyQt MainWindow 例子")    # 设置窗口标题；
        

if __name__ == "__main__": 
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("./images/cartoon1.ico"))
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())

