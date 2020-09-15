# -*- coding: utf-8 -*-
# 列表元素的操作：’ 元素 ‘— 列表操作的是元素，并非字符
# 2020.9.14
#1
print('\n#1')
zlst=['hello','PyQt5','.','com']
vlst=['Top','Quant','.','vip']
print('zlst,',zlst)
print('vlst,',vlst)

#2
print('\n#2')
print("列表元素的操作：’ 元素 ‘— 列表操作的是元素，并非字符")
s2=zlst[1:];print('s2,',s2)     
s3=zlst[1:3];print('s3,',s3)
s4=vlst[:3];print('s4,',s4)

#3
print('\n#3')
print('s2+s3,',s2+s3)
print('s3*2,',s3*2)


