# -*- coding: utf-8 -*-

# 六、信号与槽机制：测试选择—显示的逻辑代码
# 理解：相当于抽象了一层接口出来，更改ui文件后产生的ui.py的变化，Call.py直接调用变更之后的ui.py，隐藏了底层的变化；
# 2020.9.18

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWinSignalSlog03 import Ui_Form     # 注意这里的文件名和对象名
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5 import QtCore


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkBox.setChecked(True) # 设置checkBox默认的初始状态为选择


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
