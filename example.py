# # #coding:utf-8
# # a=range(4)
# # print(a)
# # print(range(0,10,3))
# #
# #
# # for i in range(4):
# #     print(i)
# # x='Hello'
# # for i in x:
# #      print(i)
# # for i in range(len(x)):
# #     print(x[i])
# # x = {'title':'python web site','url':'www.iplaypy.com'}
# # print(x.items())
# #
#
# x=1
# y=2
# def function1(x,y):
#
#     return x+y
# function1(x,y)
# print(function1(x,y))


# a = {}
# a['name']='amy'
# print(a)
# a.setdefault('name','lili')
# print(a)
# a.setdefault('name1','zhangdan')
# print(a)
#
# a.setdefault('www.iplaypy.com')
# print(a)

# a,b,c=1,2,3
# print(a,b,c)
#
# a,b=b,a
# print(a,b,c)
#
# #
# values=1,2,3
# print(values)
# a,b,c=values
# print(a,b,c)
# print(values)
#
#
# x='www.ipalypy.com'
# print(x[0])
# print(x[-1])
# print(x[4:-4])
#
#
# num=[99,1,55]
# print(len(num))
# print(min(num))
# print(max(num))

# x=[1,5,2,3,4]
# x.reverse()
# print(x)
#
# x.sort()
# print(x)
# b=sorted(x)
# print(b)
# print(x)
# print(sorted('iplaypython.com'))

'''
a=[1,2,3,4,5,6,7,8,9,10]

print([ 3*x for x in a])


print([3*x for x in range(1,11)])
b=[3*x for x in range(1,11)]
print(b)
print([x for x in a if x%2 ==0])

c= [[x,y] for x in range(2) for y in range(2)]
print(c)'''

# x=['name','ili']
# x=['age',20]
#
# print(x['name'])

'''x={'name':'lili','age':20}
print(x)

x.pop('name')
print(x)
returned_value=x.clear()
print(x)
print(returned_value)

f= {'key':'value'}
a=f
print(a)
f.clear()
print(f)
print(a)'''

'''for i in range(4):
    print(i,'www.iplaypython.com')

x='iplaypython'
# for i in x:
#     print(i)
for i in range(len(x)):
    print(x[i])'''
'''
# +++items返回列表，iteritems返回迭代器
x={'title':'python  web site','url':'www.iplaypy.com'}
print(x.items())
print(x)
a=x.items()
print(a)
print(type(x))
print(type(a))

f= x.iteritems()
print(list(f))
'''
#关键字参数
'''def al(x,y,z):
    return x,y,z
print(al(1,2,3))

def a2(x,y,z):
    return x,z,y
print(a2(1,2,3))

def c(name,Profession):
    return '%s is %s'%(name,Profession)


print(c(name='Amy',Profession='Student'))
print(c(Profession='Student',name='Amy'))



def info(name='Amy',Profession='Student'):
    return '%s is %s'%(name,Profession)
print(info())

print(info('lili'))
print(info('lili','Teacher'))'''
'''
#cmp()方法比较 3.0版本已经废弃，使用operator代替
import operator
num = [6,3,8,7]
num.sort(operator)
print(num)'''

# import logging as log
# a,b,c='aa','bb','cc'
# log.write('spam,name')



# def info(a,b,c=3,*d):
#     print(a+b+c+d[1])
# print(info)
#
# def info(a,b,c):
#     return a+b+c+d[1]
# print(info)

