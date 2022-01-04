# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/4 14:43
@Author  : AI悦创
@FileName: demo.py
@Software: PyCharm
@Blog    ：https://www.aiyc.top
@公众号   ：AI悦创
@description：
"""

try:
    from tkinter import *  # Python 3.x
except ImportError:
    from Tkinter import *  # Python 2.x

root = Tk()
e = Entry(root)
e.insert(END, 'default text')
# e.insert(END)
e.pack()
root.mainloop()
