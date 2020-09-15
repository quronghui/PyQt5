# -*- coding: utf-8 -*-
# string字符串的输出：[头下标：尾下标]
# （1）从左到右默认从0开始，最大范围是字符串长度少1；
#（2）从右到左默认从-1开始，最大范围是字符串开头；

dss='hello pyqt5'
print('dss',dss)

#1
print('\n#1')
s2=dss[1:];print('s2,',s2)
s3=dss[1:3];print('s3,',s3)
s4=dss[:3];print('s4,',s4)

#2
print('\n#2')
s2=dss[-1];print('s2,',s2)
s3=dss[1:-2];print('s3,',s3)    # 1从左到右，-2是从右到左；
dn=len(dss);print('dn,',dn)

#3
print('\n#3')
print('s2+s3,',s2+s3)       # 连接字符串；
print('s3*2,',s3*2)         # 复制一个字符串，作为两遍；
