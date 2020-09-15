# -*- coding: utf-8 -*-
# 控制语句：和其他编程语言类似；
# 注意：for循环的用法；
# 2020.9.14


#1 一对 if-else
print('\n1,if')
x,y,z=10,20,5       # python 不需要对数据类型进行定义
if x>y:
    print('x>y')
else:
   print('x<y') 

#2
print('\n#2,elif')
x,y,z=10,20,5
if x>y:
    print('x>y')
elif x>z:
   print('x>z') 

#3  while循环语句；
print('\n#3,while')
x=3
while x>0:      # while循环不需要打{ }
    print(x)
    x-=1

#4
print('\n#4,for')
xlst=['1','b','xxx']       # list 列表操作，
for x in xlst:                  # for循环的一种操作，截止条件是x；没有开始条件
    print(x)

#5
print('\n#5,for')
for x in range(3):      # for循环的另外一种用法，
    print(x)










