## Chapter03：Qt Designer 的使用方法

1. firstMainWin.ui，firstMainWin.py，CallFirstMainWin.py

   ```
   # firstMainWin.ui：由Qt designer 生成的文件；
   # firstMainWin.py：由.ui —— .py 的界面文件；随着ui文件的编译而发生变化；
   # CallFirstMainWin.py：.py的逻辑文件，实现界面文件和逻辑文件的分离；
   ```

   + 问题1：.ui——>.py文件时，运行.py文件不能显示界面？

     ```
     # pyuic5 -o firstMainWin.py firstMainWin.ui
     # 需要在.py文件中添加 if __name__ == "__main__": 函数代码
     ```

2. MainWin01.ui，Ui_MainWin01.py —— **布局管理器**

   ```
   # MainWin01.ui：对QT的三种布局方式进行尝试，显示了一个计算器；
   ```

   + 问题1：通过.ui——>.py后，界面显示不全，需要在app = QApplication(sys.argv) 语句前加一句

     ```
     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
     ```

3. TowMainWinSpacer.ui，Ui_TowMainWinSpacer.py —— 布局管理器的进阶

   ```
   # （1）如何添加空白lable，为了更好地布局；
   # （2）添加spacer占位符，使得显示效果更好；
   ```

   

