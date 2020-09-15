# -*- coding: utf-8 -*-
 # (函数)prtial：参数可以在函数被调用之前提前获知；
 # 需要导入functools模块；
 # 先传入一个参数到def函数中，生成一个新的函数；会使得代码更加简洁；
 #2020.9.15
 
import functools

def add(a, b):  # def定义函数
    return a + b

#1
print('\n#1')
rst1 = add(4, 2)
print('add(4, 2)=' , rst1)

plus3 = functools.partial(add, 3)   # 先把参数3传到add中，生成新的plus(3)函数
plus5 = functools.partial(add, 5)   # 先把参数5传到add中，生成新的plus(5)函数

#2
print('\n#2')
rst2 = plus3(4)     # 在传入另外一个参数4：
print('plus3(4)=' , rst2)

rst3 = plus3(7)
print('plus3(7)=' , rst3)

rst4 = plus5(10)
print('plus5(10)=' , rst4)



