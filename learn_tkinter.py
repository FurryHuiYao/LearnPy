#设计基本框架
import tkinter as tk
import tkinter.messagebox

win=tk.Tk() #生成一个主窗口对象

#设置变量
var_Name=tk.StringVar()
var_Name.set("")
var_Pwd=tk.StringVar()
var_Pwd.set("")

#设计功能函数

#按钮处理函数
def login():
    name=var_Name.get()
    pwd=var_Pwd.get()
    if name=="admin" and pwd=="python@16":
        tk.messagebox.showinfo(title="用户登录",message="成功！")
    else:
        tk.messagebox.showinfo(title="用户登录",message="失败！")
def cancel():
    var_Name.set("")
    var_Pwd.set("")
def _quit():
    win.destroy()

def main():
    win.title("用户登录")
    win.geometry('500x260') #窗口大小
    #功能代码开始

    #登录窗口各组件设计
    #设计两个提示标签
    labname=tk.Label(win,text="账号",width=160)
    labpwd=tk.Label(win,text="密码",width=160)
    #设计两个输入框
    #textvariable为文本框的值
    #并关联变量var_Name
    entname=tk.Entry(win,width=200,textvariable=var_Name)
    entpwd=tk.Entry(win,show="*",width=200,textvariable=var_Pwd)
    #设计三个按钮
    but_Ok=tk.Button(win,text="登录",command=login)
    but_Cancel=tk.Button(win,text="重置",command=cancel)
    but_quit=tk.Button(win,text="退出",command=_quit)

    #登录窗口各部件布局
    #部件的窗口布局
    labname.place(x=40,y=20,width=160,height=40)
    labpwd.place(x=40,y=80,width=160,height=40)
    entname.place(x=240,y=20,width=160,height=40)
    entpwd.place(x=240,y=80,width=160,height=40)
    but_Ok.place(x=60,y=160,width=100,height=40)
    but_Cancel.place(x=200,y=160,width=100,height=40)
    but_quit.place(x=340,y=160,width=100,height=40)

    #功能代码结束
    win.mainloop() #进入消息循环

if __name__ == "__main__":
    main()