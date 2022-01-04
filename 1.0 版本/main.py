# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/3 11:32
@Author  : AI悦创
@FileName: main.py
@Software: PyCharm
@Blog    ：https://www.aiyc.top
@公众号   ：AI悦创
@description：站酷图片抓取+GUI
"""
import os
import tkinter as tk
import re, requests, json
# from pprint import pprint

from requests.exceptions import RequestException


# from urllib.parse import urljoin


class MainWindow(object):
	def __init__(self):
		# 创建主窗口
		self.window = tk.Tk()
		self.window.minsize(300, 50)  # 设置窗口的最小值
		self.window.title("婷婷专享-站酷图片抓取|AI悦创&流沙团队")
		self.url = "https://www.aiyc.top"
		# self.img = "https://www.aiyc.top"
		# 添加组件
		self.addComponents()

		# 进入消息循环
		self.window.mainloop()

	def addComponents(self):
		my_frame = tk.Frame(self.window)  # 就是要把组件放在哪个主窗口 my_frame 又是其他组件的父组件
		# 设置 my_frame 的布局方式，在最上面
		my_frame.pack(side=tk.TOP)
		# 创建按钮
		# tk.Button(父窗体, text="str")
		# my_button = tk.Button(my_frame, text="执行", command=self.button_clicked)
		my_button = tk.Button(my_frame, text="执行", command=self.parse)
		my_button.pack(side=tk.RIGHT)
		# 创建单行文本
		name = tk.Label(my_frame, text="URL")
		name.pack(side=tk.LEFT)
		self.url = tk.Entry(my_frame, bd=5, width=50)
		self.url.pack(side=tk.RIGHT)

	# my_message = tk.Message(text="Aaaa")
	# my_message.pack(tk.)

	# def button_clicked(self):
	# 	print("啊哦，按钮被点击了！")
	# 	print(self.url.get())

	def parse(self):
		html = self.request_html(self.url.get())
		pattern = re.compile(r'<input.*?type.*?dataInput.*?data-objid="(.*?)".*?>', re.S | re.I)
		data_objid = re.search(pattern, html)
		data_objid = data_objid.group(1)
		url = f"https://www.zcool.com.cn/work/content/show?p=1&objectId={data_objid}"
		# url = urljoin(BASE_URL, data_objid)
		# print(url)
		html = self.request_html(url=url)
		# print(html)
		json_data = json.loads(html)
		try:
			data = json_data["data"]
			img_url_list = data["allImageList"]
			description = data["product"]["description"]
			os.mkdir(description)
			for index, img_url in enumerate(img_url_list):
				url = img_url.get("url", "https://gitee.com/huangjiabaoaiyc/image/raw/master/202201040033058.png")
				# print(url)
				postfix = re.search("http.*?img\.zcool\.cn.*?(\.\w+)", url).group(1)
				html = self.request_html(url=url, charset=False)
				# print(postfix)

				with open(f"{description}/{description}{index}.jpg", "wb")as f:
					f.write(html)
		except KeyError as e:
			# print(e)
			pass
	# print(html)
	# pattern = re.compile('<img.*?src="(https://img.zcool.cn.*?.jpg)".*?>')
	# result = re.findall(pattern, html)
	# print(result)

	def request_html(self, url, charset=True):
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
		}
		try:
			response = requests.get(url, headers=headers)
			if response.status_code == 200:
				if charset:
					return response.content.decode("UTF-8")
				else:
					return response.content
		except RequestException as e:
			# print(e)
			pass

if __name__ == '__main__':
	MainWindow()
