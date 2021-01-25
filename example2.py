#coding:utf-8

# class Person:
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def greet(self):
#         print ('hello,%s' % self.nameclass Person:)
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def greet(self):
#         print ('hello,%s' % self.names)
'''
#zip()遍历
a = [1,2,3]
b = [4,5,6]

print(list(zip(a,b)))
c=zip(a,b)
print(c)
print(list(c))


str1='abc'
str2='def123'
print(
list(zip(str1,str2))
)


l1 = [2,3,4]
l2= [4,5,6]
for (x,y) in zip(l1,l2):
    print(x,y,'--',x*y)'''


# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
# print_twice('Spam')
#
# print_twice(17)
#
# print_twice('spam ' *4)
'''#字符串长度排序
x = ['hello','abc','iplaypy.com']
x.sort(key=len)
print(x)
#当然做为key排序依据的函数，不仅仅是len，只要按照你的需求写入对应的函数就可以。假如需要以整型数字来排序，就需要用到int：
a= ['-30','188','50','1225']
a.sort(key=int)
print(a)
#reverse反向排序
a.sort(key=int,reverse=True)
print(a)
#reverse正向排序
a.sort(key=int,reverse=False)
print(a)'''


# def fun_doc(t,n,lenth,angle):
#     '''
#     绘制N个线段，给定长度和角度，单位是：度
#     :param t:
#     :param n:
#     :param lenth:
#     :param angle:
#     :return:
#     '''
#     for i in range(n):
#         fd(t,lenth)
#         lt(t,angle)
#
# fun_doc(t=3,n=4,lenth=3,angle=30)
# print(fun_doc())

'''#： x % 10 可以得到 x 的个位数(10进制)，类似地， x % 100可以获得最后2位数。
print(78 %16)'''

'''#count用法
c = ['a','iplaypython','c','b','a']

print('a的个数是d%:')
print(c.count('a'))

x=[1,2,3,'q',[1,3],[1,2],[1,3]]
print('x.count([1,3])')
print(x.count([1,3]))'''

#类内部的一个函数
# class time:
#     def __str__(self):
#         return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
#

#python处理和控制字符串大小写的问题
s='Hello'
Uppercase = s.upper()

print(Uppercase)

Lowercase = s.lower()
print(Lowercase)
#首字母大写
ll='one tWo thrEE'
print(ll.capitalize())
#每个首字母大写
ls='the monkey is bad'
print(ls.title())
print(ls.isupper())


