import threading
import tkinter as tk
import socket
class listenThread(threading.Thread):
    def __init__(self,edit,server):
        threading.Thread.__init__(self)
        self.edit=edit
        self.server= server
        def run(self):
            while 1:
                try:
                   client,addr=self.server.accept()
                   self.edit.insert(tk.END,'connect from:%s:%d\n'%addr)
                   data=client.recv(1024)
                   self.edit.insert(tk.END,'receive data:%s \n'%data)
                   client.send(str('i get:%s'% data).encode())
                   client.close()
                   self.edit.insert(tk.END,'close client \n')


                except:
                    self.edit.insert(tk.END,'close connect\n')

class control(threading.Thread):
    def __init__(self,edit):
        threading.Thread.__init__(self)
        self.edit=edit
        self.event= threading.Event()
        self.event.clear()
    def run(self):
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(('',8052))
        server.listen(2)
        self.edit.insert(tk.END,'connect....\n')
        self.lt=listenThread(self.edit,server)
        self.lt.setDaemon(True)
        self.lt.start()
        self.event.wait()
        server.close()

    def stop(self):
        self.event.set()

class window:
    def __init__(self,root):
        self.root =root
        self.butlisten = tk.Button(root,text='start',command=self.listen)
        self.butlisten.place(x=20,y=15)
        self.butclose = tk.Button(root,text='close',command=self.close)
        self.butclose.place(x=120,y=15)
        self.edit=tk.Text(root)
        self.edit.place(y=50)
    def listen(self):
        self.ctr=control(self.edit)
        self.ctr.setDaemon(True)
        self.ctr.start()

    def close(self):
        self.ctr.stop()
root =tk.Tk()
window=window(root)
root= tk.mainloop()
