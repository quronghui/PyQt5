# -*- coding: utf-8 -*-
# # 类的动态属性：方法二
#（1）@property()：希望类的属性被修改、访问时会有通知，继承object类，他有一个私有变量 __param；
#（2）可以将python定义的函数“当做”属性访问，提供更友好的访问方式；
# 2020.9.15
 
 
class MyClass(object):      # 定义一个类：继承与object;
	def __init__(self):
		self._param = None     # 私有变量

	@property  
	def param(self):  
		print( "get param: %s" % self._param)
		return self._param  

	@param.setter  
	def param(self, value):  
		print( "set param: %s" % self._param )
		self._param = value  
	 
	@param.deleter  
	def param(self):  
		print( "del param: %s" % self._param)
		del self._param  

if __name__ == "__main__":
	cls = MyClass()
	cls.param = 10
	print("current param : %s " % cls.param )
	del cls.param
    
