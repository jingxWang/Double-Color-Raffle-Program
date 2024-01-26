import random
import time
import datetime
import tkinter
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def gettime(self):
        self.var.set(datetime.datetime.now().strftime("%Y-%m-%d \n%H:%M:%S"))
        self.after(1000, self.gettime)

    def login(self):
        messagebox.showinfo("学习系统", "登录成功！欢迎开始学习")

    def createWidget(self):
        # 创建组件
        self.titlebtn=Label(root,text='双色球抽奖系统',height=3,anchor=CENTER,bg="red")
        self.titlebtn.place(relx=0.35,rely=0.01)
        
        self.var=tkinter.StringVar()
        self.timebtn=Button(root,textvariable=self.var, state='disable', bg="pink")
        self.gettime()
        self.timebtn.place(relx=0.7,rely=0.02)
        
        self.userbtn=Button(root, text="自选", command=self.usermessage,bg="Lightblue")
        self.userbtn.place(relx=0.28,rely=0.2, width=60)

        self.autobtn = Button(root, text="机选", command=self.autochoose,bg="Lightblue")
        self.autobtn.place(relx=0.53, rely=0.2,width=60)

        self.userlab=Label(root,text="用户数字:")
        self.userlab.place(relx=0.1, rely=0.37, width=60)

        self.usernum = StringVar()
        self.subjectTxt = Entry(root, width=30, textvariable=self.usernum)
        self.subjectTxt.place(relx=0.33, rely=0.37, width=160)

        self.autolab = Label(root, text="开奖数字:")
        self.autolab.place(relx=0.1, rely=0.46, width=60)

        self.autonum = StringVar()
        self.autonumTxt = Entry(root, width=30, textvariable=self.autonum)
        self.autonumTxt.place(relx=0.33, rely=0.46, width=160)

        self.resultbtn = Button(root, text="开奖", command=self.result, bg="Lightblue")
        self.resultbtn.place(relx=0.42, rely=0.6, width=60)

    def usermessage(self):
        messagebox.showinfo("自选提示", "您选择自选！\n请自行输如6个红球、1个蓝球\n请先输入一个空格，并用空格间隔数字")

    def autochoose(self):
        self.usernum.set("")
        for i in range(7):
            if i == 6:
                m = random.randint(1, 17)
            else:
                m = random.randint(1, 34)
            self.usernum.set(self.usernum.get()+" "+str(m))

    def result(self):
        self.autonum.set("")
        for i in range(7):
            if i == 6:
                m = random.randint(1, 17)
            else:
                m = random.randint(1, 34)
            self.autonum.set(self.autonum.get()+" "+str(m))
        self.winmumhong = 0
        self.winmumlan = 0
        u=self.usernum.get().split(' ')
        a=self.autonum.get().split(' ')
        for i in range(1,7):
            if u[i] in a[1:-2]:
                self.winmumhong+=1
        if u[-1]==a[-1]:
            self.winmumlan=1
        self.money = 0
        self.level = 0
        if 0 <= self.winmumhong <= 2 and self.winmumlan == 1:
            self.money = 5
            self.level = 6
        elif (self.winmumhong == 5 and self.winmumlan == 1) or self.winmumhong == 4:
            self.money = 10
            self.level = 5
        elif (self.winmumhong == 4 and self.winmumlan == 1) or self.winmumhong == 5:
            self.money = 200
            self.level = 4
        elif self.winmumhong == 5 and self.winmumlan == 1:
            self.money = 3000
            self.level = 3
        elif self.winmumhong == 6 and self.winmumlan != 1:
            self.money = "10万"
            self.level = 2
        elif self.winmumhong == 6 and self.winmumlan == 1:
            self.money = "500万"
            self.level = 1
        else:
            self.money = 0
        messagebox.showinfo("开奖提示", "开奖号码为:" + str(u[1:-1])+"\n您选中"+str(self.winmumhong)+"个红球，"+str(self.winmumlan)+"蓝球\n获得"+str(self.level)+"等奖")


if __name__=='__main__':
    root=Tk()
    root.title("双色球抽奖系统")
    root.geometry('300x360+600+100')
    app=Application(master=root)
    root.mainloop()
