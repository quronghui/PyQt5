# 四、信号与槽的连接；—— 属于逻辑代码
# 2020.9.17

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow   # 按照逻辑代码编写
from MainWinSignalSlog01 import Ui_closeWinBtn  
# MainWinSignalSlog01界面文件的文件名；Ui_closeWinBtn是对象名，在Qt的对象名Objectname上进行修改 


# 这个函数和类就不知道干啥的了？
class MyMainWindow(QMainWindow, Ui_closeWinBtn):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
