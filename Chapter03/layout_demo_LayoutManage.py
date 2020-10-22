# -*- coding: utf-8 -*-

"""
Module implementing LayoutDemo.
"""

# 逻辑测试代码：测试py代码关于数据修改后，是否会有输出；
# 和源代码的差别我现在还没有看出来？
# 2020.9.17

from PyQt5.QtCore import pyqtSlot 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_layout_demo_LayoutManage import Ui_LayoutDemo


class LayoutDemo(QMainWindow, Ui_LayoutDemo):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print('收益_min:',self.doubleSpinBox_returns_min.text())
        print('收益_max:',self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:',self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:',self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:',self.doubleSpinBox_sharp_min.text())
        print('sharp比_max:',self.doubleSpinBox_sharp_max.text())


if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())
