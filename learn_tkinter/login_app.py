#
# Created by wsnzg6 on 2026/7/10.
# Copyright(c) 2026 ZGTeam233.
#

import tkinter as tk
import tkinter.messagebox as messagebox

class LoginApp(tk.Tk):
    """用户登录窗口类，继承自 tk.Tk"""

    def __init__(self):
        # 初始化父类 tk.Tk
        super().__init__()

        # 1. 窗口基础设置
        self.title("用户登录")
        self.geometry('500x260')

        # 2. 初始化状态变量（将全局变量转为实例属性）
        self.var_name = tk.StringVar()
        self.var_pwd = tk.StringVar()

        # 3. 创建并布局 UI 组件
        self._create_widgets()

    def _create_widgets(self):
        """负责创建和布局所有 UI 组件，保持 __init__ 简洁"""
        # 标签 (去除了原代码中多余的 width 参数，因为 place 会控制像素宽度)
        self.lab_name = tk.Label(self, text="账号")
        self.lab_pwd = tk.Label(self, text="密码")

        # 输入框
        self.ent_name = tk.Entry(self, textvariable=self.var_name)
        self.ent_pwd = tk.Entry(self, show="*", textvariable=self.var_pwd)

        # 按钮 (command 绑定到实例方法)
        self.btn_ok = tk.Button(self, text="登录", command=self.login)
        self.btn_cancel = tk.Button(self, text="重置", command=self.reset)
        self.btn_quit = tk.Button(self, text="退出", command=self.quit_app)

        # 布局 (使用 place 绝对定位)
        self.lab_name.place(x=40, y=20, width=160, height=40)
        self.lab_pwd.place(x=40, y=80, width=160, height=40)
        self.ent_name.place(x=240, y=20, width=160, height=40)
        self.ent_pwd.place(x=240, y=80, width=160, height=40)
        self.btn_ok.place(x=60, y=160, width=100, height=40)
        self.btn_cancel.place(x=200, y=160, width=100, height=40)
        self.btn_quit.place(x=340, y=160, width=100, height=40)

    # ================= 事件处理函数 =================

    def login(self):
        """处理登录逻辑"""
        name = self.var_name.get()
        pwd = self.var_pwd.get()

        if name == "admin" and pwd == "python@16":
            messagebox.showinfo(title="用户登录", message="成功！")
        else:
            messagebox.showinfo(title="用户登录", message="失败！")

    def reset(self):
        """重置输入框"""
        self.var_name.set("")
        self.var_pwd.set("")

    def quit_app(self):
        """退出程序"""
        self.destroy()