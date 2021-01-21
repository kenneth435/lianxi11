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

x = ['hello','abc','iplaypy.com']
x.sort(key=len)
print(x)