from tkinter import *
import Autohomef
import threading
class WidgetsDemo:
    def __init__(self):
        self.m=None
        self.root=Tk()
        self.var=StringVar()
        # self.text = StringVar()
        self.root.geometry('400x400')#设置窗口大小
        self.root.resizable(False,False)#设置不可改变
        self.root.title('汽车之家顶贴')#设置窗口标题
        labak = Label(self.root, text="汽车之家:", font=('宋体', 12)).grid(column=0, row=0)
        txtak = Entry(self.root, width=22,textvariable =self.var).grid(column=1, row=0)
        self.t = Text(self.root)
        self.but1=Button(self.root,text='开始',command =self.star).grid(column=2,row=5)
        self.but2 = Button(self.root, text='暂停', command=self.sleeps).grid(column=3, row=5)
        self.t.grid(column=0,row=1,columnspan=10,rowspan=4)
        self.bj=True
        self.root.mainloop()
    def dick(self):
        while True:
            if self.bj==False:
                self.but1 = Button(self.root, text="开始", state=NORMAL, command=self.star).grid(column=2, row=5)
                self.insert('已暂停')
                break
            name, req = next(self.m)
            if req == '账号已经被封了':
                self.delete(name)
            self.insert(name+":"+req)
            if req=='执行完毕':
                self.but1 = Button(self.root, text="开始", state=NORMAL, command=self.star).grid(column=2, row=5)
                return
    def delete(self,name):
        with open('汽车之家.txt','r')as f:
            reds=f.readlines()
        with open('汽车之家.txt','w')as w:
            for i in reds:
                if name in i:
                    print(i)
                    reds.remove(i)
                    for i in reds:
                        if i=='\n':
                            continue
                        w.write(i)
                    break
    def tex_var(self):
        text=self.var.get()
        yz = re.findall(r"https://club.autohome.com.cn/bbs/thread-c-\d+-\d+-\d+.html", text)
        if not text:
            self.insert('链接不可为空')
            return '链接不可为空'
        if not yz:
            self.insert('输入的不是汽车之家链接')
            return '输入的不是汽车之家链接'
        return '验证完毕'
    def star(self):
        if self.m==None:
            self.m =Autohomef.main(self.var.get())
        if self.tex_var()!='验证完毕':
            return
        self.bj=True
        print(self.bj)
        self.but1 = Button(self.root, text="开始", state=DISABLED, command=self.star).grid(column=2, row=5)
        self.insert('开始')
        threading.Thread(target=self.dick,).start()
    def sleeps(self):
         self.insert('暂停中')
         self.bj=False
    def insert(self,m):
        self.t.insert(END, m+'\n')
wind=WidgetsDemo()