# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/4 16:53
@Author  : AI悦创
@FileName: os_tester.py
@Software: PyCharm
@Blog    ：https://www.aiyc.top
@公众号   ：AI悦创
@description：
"""
# import os
#
# r = os.path.exists("Default")
# print(r)
# from uuid import uuid4
# print(uuid4())
#
# user_input = input("Please enter sex:").upper()
# if user_input == "M":
# 	print("M")
# elif user_input == "W":
# 	print("W")
# # else:
# # 	print("error!")

user_answer_correct = False

while not user_answer_correct:
	user_gender = input("请输入您的性别(F/M):")
	if user_gender == "F":
		print("你是萌妹纸学生！")
		user_answer_correct = True
	elif user_gender == "M":
		print("你是糙汉子！")
		user_answer_correct = True
	else:
		print("输入不正确，请输入 F/M")
