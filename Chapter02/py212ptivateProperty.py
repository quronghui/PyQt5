# -*- coding: utf-8 -*-
# 类的属性和方法：
#（1）类内部使用def定义一个方法，类的方法的第一个参数必须是self;
#（2）类的私有方法：__private__method（两个下划线开头），调用self.__private__method
#（3）类的私有属性：__private_attrs，调用时self.__private_attrs
#（4）只能在类的内部调用调用私有方法，只能在类的内部访问私有属性（变量和方法）；
#2020.9.15
 
 # 这是一整个类：只能在类的内部调用调用私有方法
 # 只能在类的内部访问私有属性（变量和方法）；
 
class MyCounter:        # 累的定义
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def __privateCountFun(self):    # 类的私有方法；
        print('这是私有方法')
        self.__secretCount += 1
        self.publicCount += 1               # 注意：私有方法调用不了公开变量
        #print (self.__secretCount)
        
    def publicCountFun(self):       # 类的共有方法；
        print('这是公共方法')
        self.__privateCountFun()       # 调用私有的方法

 # 这是一整个类：
 
if __name__ == "__main__":
    counter = MyCounter()           # 定义一个counter的对象
    counter.publicCountFun()        # 类的外面，对象不能访问私有属性；
    counter.publicCountFun()
    print ('instance publicCount=%d' % counter.publicCount)
    print ('Class publicCount=%d' % MyCounter.publicCount)
    
    # 报错，实例不能访问私有变量
    # print (counter.__secretCount)  
    # 报错，实例不能访问私有方法
    # counter.__privateCountFun()
