# -*- coding: utf-8 -*-
# 类的动态属性
#（1）property([fget, fset, fdel])：希望类的属性被修改、访问时会有通知，继承object类，他有一个私有变量 __param；
#（2）不太会用
# 2020.9.15
 
class MyClass(object):  # 定义一个类，继承于object
    def __init__(self):     # __init__属于构造函数，一个类只能有一个构造函数，用于初始化类及其变量；
        self._param = None

    # property 的三个固有方法；
    def getParam(self):     # 使用def定义一个方法，类的方法的第一个参数必须是self;
        print( "get param: %s" % self._param)
        return self._param

    def setParam(self, value):
        print( "set param: %s" % self._param )
        self._param = value

    def delParam(self):
        print( "del param: %s" % self._param)
        del self._param

    param = property(getParam, setParam, delParam)  # property：希望类的属性被修改时有通知；

if __name__ == "__main__":
    cls = MyClass()         # 类定义对象；
    cls.param = 10          # 按理说不能在类外面使用类的私有属性；
    print("current param : %s " % cls.param )
    del cls.param
