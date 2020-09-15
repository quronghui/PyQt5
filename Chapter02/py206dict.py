# -*- coding: utf-8 -*-

# 字典：用{ }进行标识，由索引key和对应的值value组成，是除了列表外最灵活的内置数据结构类型
# 列表是有序的对象集合，字典是无序对象集合；
# 字典中的元素通过key关键字进行存取；
#2020.9.14

#1：key和value在{ }外，并进行key和value的对应
print('\n#1')
zdict={}            # dict 的标识 {  }
zdict['w1']='hello'     # dict的key和value进行对应
zdict['w2']='ziwang.com'
print('zdict,',zdict)


#2  key和value 直接在dict{ } 中进行对应
print('\n#2')
vdict={'url1':'TopQuant.vip'
       ,'url2':'www.TopQuant.vip'
       ,'url3':'ziwang.com'}
print('vdict,',vdict)


#3  直接通过key 进行赋值操作
print('\n#3')
s2=zdict['w1'];print('s2,',s2)
s3=vdict['url2'];print('s3,',s3)
