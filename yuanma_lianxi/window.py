import tkinter as tk
import socket
class window:
    def __init__(self,root):
        label1 = tk.Label(root,text='IP')
        label2 = tk.Label(root,text='PORT')
        label3 = tk.Label(root,text='DATA')
        label1.place(x=5,y=5)
        label2.place(x=30,y=5)
        label3.place(x=35,y=5)
        self.entryIP=tk.Entry(root)
        self.entryIP.insert(tk.END,'127.0.0.1')
        self.entryport = tk.Entry(root)
        self.entryport.insert(tk.END, '1051')
        self.entrydata = tk.Entry(root)
        self.entrydata.insert(tk.END, 'hello')

        self.Recv = tk.Text(root)
        self.entryIP.place(x=40, y=5)
        self.entryport.place(x=40, y=30)
        self.entrydata.place(x=40, y=55)
        self.Recv.place(y=115)

        self.send=tk.Button(root,text='send',command=self.send)
        self.send.place(x=40,y=80)

    def send(self):
        try:
            self.entryIP.get()
            port=int(self.entryport.get())
            data=self.entrydata.get()
            client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.send(data)
            rdata = client.recv(1024)
            self.Recv.insert(tk.END,rdata.decode())
            client.close()

        except Exception as e:
            self.Recv.insert(tk.END,'error')
root=tk.Tk()
window=window(root)
root.mainloop()

