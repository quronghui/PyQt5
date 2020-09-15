# -*- coding: utf-8 -*-
# python:只有自定义函数，方便我们重复使用相同的一段程序；
# 函数的定义使用关键字 def;
# 2020.9.15


def f01(a,b,c):             # 函数的定义：有一个def和冒号；
	print('a,b,c,',a,b,c)
	a2,b2,c2,=a+c,b*2,c*2       # python元素的赋值可以一起赋值；
	return a2,b2,c2                 # 带有返回值；


#1
print('\n#1')
x,y,z=f01(1,2,3)
print('x,y,z,',x,y,z)

#2
print('\n#2')
x,y,z=f01(x,y,z)
print('x,y,z,',x,y,z)   # 将上一次运算的输出，作为这次的输入；

