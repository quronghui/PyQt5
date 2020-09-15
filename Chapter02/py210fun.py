# -*- coding: utf-8 -*-
# lambda：用于编写简单的函数，而def用来处理更强大的任务
# lambda形式：lambda + 参数(多个)  + “:”   +表达式 ；
# lambda是一个表达式，不是一个语句，返回一个值；
# 2020.9.15
 
fun1 = lambda x,y : x + y   # lambda 表达式的定义
print('fun1(2,3)=' , fun1(2,3))

fun2 = lambda x: x*2
print('fun2(4)=' , fun2(4) )
