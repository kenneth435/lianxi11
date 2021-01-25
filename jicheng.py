'''class A(object):
    def __init__(self,arg1):
        print("init func is A,with arg1 '%s' " % arg1)
        super(A, self).__init__()

class B(object):
    def __init__(self,arg1,arg2):
        print("init func is S,with arg2 '%s' " % arg2)
        super(B, self).__init__(arg1)

class C(B,A):
    def __init__(self,arg1,arg2):
        print("init func in C,with arg1 '%s' , arg2 '%s'" % (arg1,arg2))
        super(C, self).__init__(arg1,arg2)
        print(C.__mro__)

c= C("C's arg2","C 's arg2")'''


#传统方式
class A (object):
    def __init__(self,arg1):
        print("init func in A,with arg1 '%s'" % arg1)

class B(object):
    def __init__(selfa,arg1,arg2):
        print("init func in B,with arg1 '%s',arg2 '%s'"%(arg1,arg2))

class C(A,B):
    def __init__(self,arg1,arg2):
        print("init func in C,with arg1 '%s', arg2 '%s'" %(arg1,arg2))
        A.__init__(self,arg1)
        B.__init__(self,arg1,arg2)
        print(C.__mro__)

c=C("C's arg1","C's arg2")

