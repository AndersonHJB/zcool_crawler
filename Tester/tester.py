# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/4 14:24
@Author  : AI悦创
@FileName: tester.py
@Software: PyCharm
@Blog    ：https://www.aiyc.top
@公众号   ：AI悦创
@description：
"""
import tkinter as tk
from tkinter import END

windows = tk.Tk()
windows.minsize(400, 400)
windows.title("AI悦创·Teseter")

my_frame = tk.Frame(windows)
my_frame.pack(side=tk.TOP)
name = tk.Label(my_frame, text=" ")
name.pack(side=tk.LEFT)

filename = tk.Entry(my_frame, text="请输入：", bd=5)
filename.insert(END, "Default")
filename.pack(side=tk.LEFT)
button = tk.Button(my_frame, text="点击", command=lambda: print(filename.get()))
button.pack(side=tk.LEFT)
windows.mainloop()