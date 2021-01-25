#coding:utf-8
'''
import threading
import time

class Test(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self._run_num=num

    def run(self):
        global count,mutex
        threadname= threading.currentThread().getName()

        for x in range(0,int(self._run_num)):
            mutex.acquire()
            count=count+1
            mutex.release()
            print(threadname,x,count)
            time.sleep(1)

if __name__ == '__main__':
    global count,mutex
    thread=[]
    num=4
    count=1
    # 创建锁
    mutex = threading.Lock()

    for x in  range(0,num):
        thread.append(Test(10))#添加线程对象

    for t in thread:
        t.start()#启动线程

    for t in thread:
        t.join()#等待子线程接触
'''


import threading
import time
def thread_main(a):
    global count,mutex
    threadname=threading.currentThread().getName()

    for x in  range(0,int(a)):
        mutex.acquire()
        count=count+1
        mutex.release()
        print(threadname,x,count)
        time.sleep(1)
def main(num):
    global count,mutex
    theads=[]
    count=1
    mutex=threading.Lock()

    for x in range(1,num):
        theads.append(threading.Thread())

    for t in theads:
        t.start()

    for t in theads:
        t.join()
if __name__ == '__main__':
    num =4#创建4个线程
    main(4)
