## Chapter03：Qt Designer 的使用方法

+ 界面文件和逻辑文件的区别便是：界面文件与ui连接，逻辑文件实现界面文件的显示；

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

   + 问题2：通过.ui——>.py后，界面显示不全，需要在app = QApplication(sys.argv) 语句前加一句

     ```
     # from PyQt5 import QtCore
     # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
     ```

3. TowMainWinSpacer.ui，Ui_TowMainWinSpacer.py —— 布局管理器的进阶

   ```
   # （1）如何添加空白lable，为了更好地布局；
   # （2）添加spacer占位符，使得显示效果更好；
   ```

4. layout_demo_LayoutManage.ui，Ui_layout_demo_LayoutManage.py，layout_demo_LayoutManage.py—布局管理器的代码测试

   ```
   # layout_demo_LayoutManage.py：布局管理器的代码测试；
   # 问题：没有找到源.py 和 测试代码.py(逻辑代码) 代码的区别；
   ```

5. 信号与槽——MainWinSignalSlog01.ui，Ui_MainWinSignalSlog01.py，CallMainWinSignalSlog01.py

   ```
   # MainWinSignalSlog01.ui 通过edit/signal，建立关闭按钮的功能；并且修改了ObjectName的名字；
   # CallMainWinSignalSlog01.py	逻辑测试代码文件，编写时注意文件名已经修改了；
   ```

6. 信号与槽——MainWinSignalSlog03.ui，Ui_MainWinSignalSlog03.py，CallMainWinSignalSlog03.py

   ```
   # 六、信号与槽机制：测试选择—显示的逻辑代码
   # 理解：相当于抽象了一层接口出来，更改ui文件后产生的ui.py的变化，Call.py直接调用变更之后的ui.py，隐藏了底层的变化；
   ```

   + 问题3：逻辑文件怎么编写

     + 理解：相当于抽象了一层接口出来，更改ui文件后产生的ui.py的变化，Call.py直接调用变更之后的ui.py，隐藏了底层的变化；

     + ```
       # from MainWinSignalSlog01 import Ui_closeWinBtn 
       # MainWinSignalSlog01——界面文件名；Ui_closeWinBtn是对象名（在Qt的对象名Objectname上进行修改 ）
       # 其余的代码好像都是一样的；
       ```

7. 菜单栏和工具栏的建立：MainFrom.ui，Ui_MainFrom.py，CallMainForm.py

   + 菜单栏：建立主窗口后——双击Type Here——输入想要的名字便可
   + 工具栏：右键Add Tool Bar —— 添加Action —— 将Action拖入到工具栏中

   ```
   # CallMainForm.py：里面有一个问题，fileCloseAction（） 这个函数没有起到作用；
   # bug：连接函数connect写错了
   ```

8. 菜单栏和工具栏的测试：MainForm2.ui，Ui_MainForm2.py，ChildrenForm2.ui，Ui_ChildrenForm2.py，CallMainForm2.py

   + 添加到窗口是一个嵌入的子窗口

   + ```
     # MainForm2.ui，Ui_MainForm2.py：主窗口，添加了一个栅格布局；
     # ChildrenForm2.ui，Ui_ChildrenForm2.py：子窗口，添加了一个要消失的内容；
     # CallMainForm2.py：逻辑代码，同时导入主窗口和子窗口，添加触发方式。
     ```

9. 嵌入一个静态图片：MainForm3.ui，Ui_MainForm3.py，CallMainForm3.py

   + ```
     # MainForm3.ui：在prc资源里添加静态资源图片，将其名字命名为pic；通过lable标签添加一个静态图片，在pixmap属性中添加图片；
     # 注意：需要将.prc文件便以为.py文件，才能有图片显示；
     ```

     