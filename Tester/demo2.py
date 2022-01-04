# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/4 15:29
@Author  : AI悦创
@FileName: demo2.py
@Software: PyCharm
@Blog    ：https://www.aiyc.top
@公众号   ：AI悦创
@description：
"""
import tkinter as tk

class MainWindow(object):
	def __init__(self):
		# 创建主窗口
		self.window = tk.Tk()
		self.window.minsize(300, 50)  # 设置窗口的最小值
		self.window.title("婷婷专享-站酷图片抓取|AI悦创&流沙团队")
		self.url = "https://www.aiyc.top"
		# 添加组件
		self.addComponents()

		# 进入消息循环
		self.window.mainloop()

	def addComponents(self):
		my_frame = tk.Frame(self.window)  # 就是要把组件放在哪个主窗口 my_frame 又是其他组件的父组件
		# 设置 my_frame 的布局方式，在最上面
		my_frame.pack(side=tk.TOP, anchor="w")
		# 创建按钮
		# tk.Button(父窗体, text="str")
		my_button = tk.Button(my_frame, text="执行", command=self.button_clicked)
		# my_button = tk.Button(my_frame, text="执行")
		my_button.pack(side=tk.RIGHT)
		# 创建单行文本
		name = tk.Label(my_frame, text="URL")
		name.pack(side=tk.LEFT)
		self.url = tk.Entry(my_frame, bd=5, width=50)
		self.url.pack(side=tk.RIGHT)

		# 添加用户输入
		my_frame2 = tk.Frame(self.window)
		my_frame2.pack(side=tk.BOTTOM, anchor="w")
		name_file = tk.Label(my_frame2, text="文件夹名称")
		name_file.pack(side=tk.LEFT)
		self.filename = tk.Entry(my_frame2, bd=5, width=30)
		self.filename.pack(side=tk.RIGHT)

if __name__ == '__main__':
	MainWindow()