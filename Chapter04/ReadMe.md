## Chapter04 : PyQt5基本窗口控件

### QMainWindow 主窗口介绍

1. 创建一个主窗口：qt402_QMainWin.py

   ```
   # 1. 通过QMainWindow中的方法进行创建，之前是通过qt创建的，对应的方法里面也有；
   # 2. 通过showMessage显示消息消息，延时5秒
   # 3. 通过setWindowTitle 设置窗口标题
   ```

2. 创建一个主窗口，放在屏幕中间：qt405_center.py

   ```
   # QDesktopWidget描述显示屏幕的类；screenGeometry获得屏幕的大小
   # 获取QWidget 屏幕大小
   ```

3. 创建一个主窗口，通过button关闭窗口：qt04_CloseMainWin.py

   ```
   # text()函数：获取显示的名称；
   # print()输出可以在Terminal串口里面查看信息
   ```

### QWidget  基础窗口控件

1. widget界面控件：实现屏幕坐标系：qt401_widgetGenmetry.py

   ```
   # PyQt5中坐标系统
   # widget界面控件：实现屏幕坐标系
   ```

2. 创建一个PyQt的应用：qt402_FirstPyQt.py

   ```
   # 创建一个PyQt的应用：只显示一个界面；
   # 介绍了程序的运行过程；
   ```

3. 为PyQt程序设置一个程序图标；：qt403_QIcon.py

   ```
   # 设置一个图标在程序的标题栏内
   ```

4. 设置一个气泡提示问题：qt404_QToolTip.py

   ```
   # 设置一个显示信息：当鼠标在界面上时显示一行文字；
   ```

### Lable 标签控件

1. 标签的使用：：qt406_QLable.py

   ```
   # Lable 标签的使用：作为纯文本、链接、图片等显示
   # （1）重点是lable作为超链接的使用
   # （2）设置的链接没起作用
   ```

2. 标签的使用：作为快捷键qt407_QLable.py

   ```
   # Lable 标签的使用：lable标签作为快捷键
   # PyQt5中Qlabel例子
   # 按住 Alt + N , Alt + P , Alt + O , Alt + C 切换组件控件
   ```

### 文本框类控件

#### QlineEdit

1. 文本类控件：qt408_lineEdit01.py

   ```
   # PyQt5中 QLineEdit.EchoMode效果例子     
   # (1) 可以再lineEidt 文本框内设置在提示词
   （2）# setPlaceholderText：设置文本框浮显字符，起到提示作用，当输入后消失；
   （3）	# setEchoMode：设置文本框显示格式，允许输入的文本显示格式有具体的格式要求；
   		# QLineEdit.Normal：正常显示所输入的字符，默认选项；
   		# QLineEdit.NoEcho：不显示任何输入字符，常用于密码类型的输入，且其密码长度需要保密时；
   		# QLineEdit.Password：显示与平台相关的密码掩码字符，而不是实际输入的字符；
   		# QLineEdit.PasswordEchoOnEdit：在编辑时显示字符，负责显示密码类型的输入；
   ```

2. 文本类控件：通过**验证器**对输入进行限制，qt408_lineEdit02.py

   ```
   PyQt5中 QLineEdit的验证器例子 
   # 验证器：主要是对用户的输入做一些限制；
   # （1）整数的限制：[1, 99]；
   # （2）浮点型的限制：[-360, 360] 精度：小数点后2位
   # （3）字符和数字：("[a-zA-Z0-9]+$")
   # （4）验证器的设置代码；
   ```

3. 文本类控件：通过**掩码**进行限制，qt408_lineEdit03.py

   ```
   PyQt5中 QLineEdit的输入掩码例子        
   # （1）限制用户的输入，出了使用验证器，还可以使用输入掩码；
   # （2）IP, MAC, 日期, 许可证
   ```

4. 综合文本类控件：qt408_lineEdit04.py

   ```
   # 文本编辑器的综合例子；
   #（1）规定文本使用字体、右对齐，允许输入整数
   #（2）限制小数点后两位：0.99 ——99.99
   #（3）设置输入得掩码：应用于电话号码
   #（4）设置发射信号连接到槽函数
   #（5）设置一个只显示的文本框
   #（6）连接到槽函数，一旦用户按下回车，该函数就会执行
   ```


#### QTextEdit

1. 多行文本框控件：可以显示多行文本内容；qt409_textEdit.py

   ```
   PyQt5中 QTextEdit例子  
   # QTextEdit类是一个多行文本框控件，可以显示多行文本内容，可以显示垂直滚动条；    
   # （1）自定义函数：实现按键按下后能够显示文本
   # （2）自定义函数：实现按键按下后能够显示HTML文档；
   ```

   

### 按钮类控件

1. QpushButton：qt410_QButton.py

   ```
   PyQt5中QButton例子
   # 按钮类控件继承于QAbstractButton;
   (1) 起到一个按钮的作用;可以采用lambda方式传递参数，将参数发给槽函数
   (2) 设置一个图片作为按键: 使用setIcon()方法接收一个QPixmap对象的图像图件作为参数输入；
   (3) 按键3：设置其不触发，显示就为灰色；可以作为还没有功能的按钮；
   (4) 对按键设置快捷键：Alt+D 需要首字母为D并且前面有一个&符号；
   ```

2. QRaidoButton-带文本的触发按键，多个中选其一：qt410_QRadio.py

   ```
   PyQt5中QRadio例子：多选一的操作
   # QRadioButton 按钮的触发方式为：状态改变时才触发—有利于监控
   # 当bt2和bt1进行切换的时候，才会触发槽函数；槽函数的功能用来检测按钮的状态；
   ```

3. QCheckBox-带文本的复选框，多个中选多个：qt411_QCheckbox.py

   ```
   PyQt5中 QCheckBox 例子——多选多
   # 提供了一组带文本标签的复选框，用户可以选择多个选项；
   # （1）setTristate()函数提供三种状态的选择；
   # （2）isChecked() 查询是否被选中；checkState() 选中的状态（0, 1,2）
   # （3）str() 函数将对象转化为适于人阅读的形式
   ```

4. QComboBox—下拉选择框：qt412_QComboBox.py

   ```
   PyQt5中 QComboBox 例子
   # QComboBox是一个集按钮和下拉选项于一体的控件，也被成为下拉类表框；
   #（1）addItem()添加单个选项； addItems()添加多个选项；
   #（2）添加了for循环；而且循环的数目是可以在内部显示的，count是怎么来的呢？
   #（3）下拉选项进行选择，当选中某一选项时，将该文本设置成标签文本
   ```

5. QSpinBox—计数器控件：qt413_QSpinBox.py

   ```
   PyQt5中 QSpinBox 例子
   # QSpinBox：计数器的控件，允许输入整数或者浮点数，通过上下箭头增加/减少当前的值；
   #（1）QSpinBox 用于设置整数值；
   #（2）QDoubleSpinBox 用于设置浮点数；
   #（3）还有一些其他功能的函数：用于补充实现计算器的功能；
   ```

6. QSlider—滑动条：qt414_QSlider.py

   ```
   PyQt5中 QSlider 例子
   # QSlider：提供了一个垂直或者水平的滑动条；
   #（1）设置一个标签，并且设置其位置为中间；
   #（2）根据此时滑块value值的大小，设置标签的字号；
   #（3）QSlider 相比计算器显示更加的明显
   ```


### 对话框类控件

1. Dialog—提供一系列的标准对话框来完成特定场景下的功能，更好地实现人机交互：qt415_QDialog.py

   ```
   	PyQt5中 QDialog 例子
   # QDialog控件：为了更好地实现人机交互，提供一系列的对话框完成特定场景下的功能；
   # （1）WindowModality窗口的模态设置（三种模态），Qt.ApplicationModal不与其他窗口交互；只有关闭了所有的子窗口后才能关闭窗口
   # （2）当用户按下Esc按键时，对话框窗口将会调用QDialog.reject()方法，用于关闭对话框
   # （3）主窗口QMainWindow，通过一个自定义函数包含了子窗口QDialog;
   ```

2. QMessageBox—通用的弹出式对话框：qt416_QMessageBox.py

   ```
   PyQt5中 QMessage 例子
   # QMessage 通用的弹出式对话框：可以修改不同的文字，显示不同的图标；
   # （1）功能都是一样的：起到一个提示作用；
   # （2）infomation信息框  ：有标准的形式；
   # （3）实现了五种对话框的代码；
   # （4）问题：没有实现布局？解决layout = QVBoxLayout(self)	加入self变量，对其进行布局；
   ```

3. QInputDialog—提供标准的对话框，有一个文本框和两个按钮（OK,Cancle）：qt415_QInputDialog.py

   ```
   PyQt5中 QInputDialog 例子
   # QInputDialog 控件是一个标准的对话框，有一个文本框和两个按钮（OK,Cancle）
   # （1）与Dialog的区别便是，其不仅可以起提示作用，还能输入文本；并将信息回馈给主窗口
   # （2）layout.addRow(self.btn1,self.le1)	# 在一个布局里面的两个控件布局在一行上；
   # （3）布局要求：self.setLayout(layout)	# layout = QFormLayout(self)	没有带self变量时需要这个
   ```

4. QMessage—提示作用的对话框：qt416_QMessageBox.py

   ```
   PyQt5中 QMessage 例子
   # QMessage 通用的弹出式对话框：可以修改不同的文字，显示不同的图标；
   # （1）功能都是一样的：起到一个提示作用；
   # （2）infomation信息框  ：有标准的形式；
   # （3）实现了五种对话框的代码；
   # （4）问题：没有实现布局？解决layout = QVBoxLayout(self)	加入self变量，对其进行布局；
   ```

5. QFontDialog—字体选择对话框：qt417_QFontDialog.py

   ```
   PyQt5中 QFontDialog 例子
   # QFontDialog控件是一个常用的字体选择对话框，可以让用户选择所显示文本的字号大小、样式、格式、
   # QFontDialog.getFont()函数：输出字体选择框；
   # setFont(font)	：将目标字体设置为getFont()函数得到的字体；
   ```

6. QFileDialog—打开和保存文件的标准对话框：qt418_QFileDialog.py

   ```
   # QFileDialog 用于打开和保存文件的标准对话框，同样是继承自QDialog
   #（1） getOpenFileName()调用文件对话框显示图像；
   	# self：显示父组件；第二个参数：对话框的标题；第三个参数：对话框显示默认打开的目录；第四个参数：相当于过滤器filter
   #（2）QFileDialog()	文件对话框的对象exec_来选择文件，并将文件的内容显示在文本编辑控件中；
   	# 显示文件里面的内容，有相关的代码。
   #（3）Pixmap()函数：加载并呈现本地图像
   ```
### 窗口绘图类控件：QPainter

+ 定义了一个绘制事件： QtGui.QPainter 类负责所有低级别的绘制，所有绘制的事件都在此内（begin—end）

1. 通过drawText()函数绘制出给定的文字：qt419_drawText.py

   ```
   # （1）drawText()方法显示给定坐标处的文字；
   #（2）setPen()设置画笔的颜色；
   #（3）setFont()设置字体大小；
   # （4）def paintEvent(self,event)定义了一个绘制事件： QtGui.QPainter 类负责所有低级别的绘制，所有绘制的事件都在此内（begin—end）
   ```

2. drawPointer：在窗体中绘画点的例子：qt419_drawText.py

   ```
   drawPointer—在窗体中绘画点的例子：
   （1）绘制了[-100, 100]两个周期的正弦函数图像
   ```

3. QPen：是一个基本的图形对象，用于绘制直线、曲线、轮廓画出矩形、椭圆形、多边形和其他形状：qt419_drawPen.py

   ```
   QPen：是一个基本的图形对象，用于绘制直线、曲线、轮廓画出矩形、椭圆形、多边形和其他形状。
   # 绘图中QPen 的例子 ,绘制使用不同样式的6条线
   #类6：CustomDashLine自定义的线条样式；
   	# setDashPattern()方法使用数字列表定义样式：列表中个数必须是偶数
   	# 1—像素宽度的横线，4—像素宽度的空余距离
   ```

4. QBrush：绘制九个不同样式的矩形：qt419_drawBrush.py

   ```
   绘图中QBrush 的例子 ,绘制九个不同样式的矩形。
   （1）# 将Qprinter对象的画刷设置成QBrush对象
   （2）# 调用drawRect()方法绘制矩形；
   ```

5. QPixmap：用于绘图设备的图像显示：qt419_QPixmap.py

   ```
   	PyQt5中 QPixmap 例子:用于绘图设备的图像显示
   （1）它可以作为一个QPaintDevice对象；也可以加载到一个控件中，通常是标签和按钮；
   （2）使用setPixmap将图像显示在QLable上；
   ```

### 拖拽和剪切板

1. Drag与Drop

   + 拖拽功能是基于MIME类型的拖拽数据传输的，其类型是基于QDrag类；QMimeData对象将关联的数据与其对应的MIME类型相关联；
   + MimeData类有相关的函数处理MIME类型的数据：判断函数、设置函数、获取函数；
   + QWidget对象支持拖拽动作：允许拖拽数据的控件必须设置QWidget.setDragEnabled()函数为True;

2. Drag and Drop 例子：拖拽事件的发生：qt420_QDrag.py

   ```
   	PyQt5中  Drag and Drop 例子：拖拽事件的发生
   （1）实例：将左边文本框的输入拖拽到右边的下拉菜单栏中——实现下拉菜单的动态输入；
   （2）存在两个类：Combo选择继承QComboBox类（下拉选择框）；Example继承了QWidget类；
   （3）mimeData()类函数允许检测和使用方便的MIME类型；
   （4）允许拖拽数据的控件必须设置QWidget.setDragEnabled()函数为True;
   ```

3. QClipboard：对系统剪切板的访问，可以在应用程序之间复制和粘贴数据；qt420_QClipboard.py

   ```
   	PyQt5中 QClipboard 例子:对系统剪切板的访问，可以在应用程序之间复制和粘贴数据；
   （1）通过QLabel显示文本和图片；
   （2）按钮进行点击事件：对不同的呢MIME数据类型进行复制和粘贴；
   （3）文本数据(Text)、图像数据(Image)、网页数据（HTML）;
   （4）当剪切板内容发生变化的时候，dataChange信号被发射；
   ```

### 日历与时间

1. QCalendar：是一个日历控件，提供了一个基于月份的视图，允许用户通过鼠标或键盘选择日期，默认选中的是今天的日期；

   + 设置日期的选择范围，最大和最小日期；
   + 设置日历空间是否显示网格

2. QCalendarWidget：是一个日历控件，提供了一个基于月份的视图；qt421_QCalendar.py

   ```
   	PyQt5中 QCalendarWidget 例子:是一个日历控件，提供了一个基于月份的视图
   （1）月份、年份、日期的具体选择；
   （2）并且通过setText对选择的日期进行显示；
   （3）QCalendar的对象是通过QCalendarWidget类进行创建的；
   （4）通过QDate()方法设置具体的日期；
   （5）从窗口中选定一个日期，会发射一个QtCore.QDate信号，将此信号连接到用户的槽函数中；
   （6） selectedDate()方法返回当前选定的日期，检索所选定的日期，并将日期对象转换为制定格式字符串；
   （7）lable显示日期的时候：进行了两次日期的设置；
   ```

3. DateTimeEdit1：例子：提供日期和时间格式的修改；qt421_DateTimeEdit1.py

   ```
   	PyQt5中 DateTimeEdit1 例子：提供日期和时间格式的修改
   （1） DateEdit、 DateTimeEdit、 TimeEdit：分别对应着日期、日期时间、时间，三种方式的修改；
   （2）DateTimeEdit 通过 setDisplayFormat()函数设置显示的日期时间格式；
   ```

4. DateTimeEdit2：通过弹出框对日期进行选择；qt421_DateTimeEdit2.py

   ```
   	PyQt5中 DateTimeEdit2 例子：
   （1）实例：日期可以通过弹出框进行选择；
   （2）DateTimeEdit2控件和按钮控件，当单击“获得日期和时间”
   （3）setCalendarPopup：设置日期的选择为弹出框内进行选择；
   （4）信号与槽函数的连接的函数模板：同样分为日期、日期和时间、时间，三种槽函数；
   （5）获取日期、时间的函数模板；
   ```

### 菜单栏、工具栏与状态栏

1. 在QMainWindow对象的标题栏下方，水平的QMenuBar被保留显示QMenu对象；

   + QMenu类提供了一个可以添加到菜单栏的小控件；
   + 顶层窗口必须是QMainWindow对象，才可以引用QMenuBar;
   + addMenu()函数可以将菜单添加到菜单栏中；
   + addAction()函数可以在菜单中进行添加操作；

2. Qmenu：QMenuBar用于显示QMainWindow标题栏；qt422_QMenuBar.py

   ```
   PyQt5中 Qmenu 例子:QMenuBar用于显示QMainWindow标题栏；
   （1）第一个菜单栏基于menuBar进行创建的；同样，菜单栏下的addAction 动作都是基于此菜单栏的；
   （2）基于第一个菜单栏下，再次创建菜单栏，那么此时便是基于第一个菜单栏;
   （3）对象.addSeparator() # 在菜单栏中添加横线，在需要添加横线的动作后面添加；
   （4）分清楚上一级的父类是谁；
   ```

3. QToolBar：由文本按钮、图标或其他小控件按钮组成的可移动面板；qt422_QToolBar.py

   ```
   PyQt5中 QToolBar 例子:由文本按钮、图标或其他小控件按钮组成的可移动面板，位于菜单栏下方
   （1）# addToolBar()方法：在工具栏区域添加文件工具栏；
   （2）# 添加具有文本标题的工具按钮，包括图形按钮；
   （3）# 将信号连接到槽函数；
   ```

4.  QStatusBar ：为状态栏添加一个水平条，用于显示超过界面的内容；qt422_QStatusBar.py

   ```
   PyQt5中 QStatusBar 例子
   （1）实例：创建一个file惨淡栏，并为其添加一个动作，并为其创建一个编辑框；最后点击show动作时，提示已被点击；
   （2）创建一个水平条
   ```

### 打印图像

1. QPainter：创建一个QPainter对象进行画图，只是打印使用的是QPrinter，本质上也是一个QPaintDevice绘图设备；qt423_Qpainter.py

   ```
   	QPainter: 创建一个QPainter对象进行画图，只是打印使用的是QPrinter，本质上也是一个QPaintDevice绘图设备；
   （1）创建一个放置图像的QLabel对象imageLabel，并将该QLabel对象设置为中心窗体。 
   （2）创建菜单，工具条等部件 ，用于显示打印这个动作；
   （3）判断打印对话框显示后用户是否单击“打印”按钮，若单击“打印”按钮，
          则相关打印属性可以通过创建QPrintDialog对象时使用的QPrinter对象获得，
          若用户单击“取消”按钮，则不执行后续的打印操作。 
   （4）自定义的打印函数；
   ```

   



