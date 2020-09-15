# -*- coding: utf-8 -*-
# 类的变量：全局的变量，每个对象都可以调用，引用方式：对象  .  变量；
# 对象的变量：私有变量，引用方式：self.变量
# __init__：属于构造函数，一个类只能有一个构造函数，用于初始化类及其变量；
# 函数的定义：（对象， 变量）
# % ：类似于C预言要输出对应格式的参数；
# 2020.9.15
 
class MyClass:      # 定义一个MyClass 类
	count = 0           # 全局变量
	name = 'DefaultName' 
   
	def __init__(self, name):       #  __init__ 属于构造函数，一个类只能有一个构造函数，用于初始化类及其变量；
		self.name = name 
		print('类的变量是%s，对象的变量是:%s' % ( MyClass.name,  self.name) )
        
	def setCount(self, count ):
		self.count = count

	def getCount(self):
		return self.count
 
if __name__ == "__main__":      # 主函数；
	cls = MyClass('lisi')           # 定义一个cls的对象；
	cls.setCount(10)
	print('count=%d' % cls.getCount())
