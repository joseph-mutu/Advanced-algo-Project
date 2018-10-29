#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-29 18:07:50
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

# 以下将尝试打开 tsp 文件，将文件保存在元组中
import numpy as np

with open('D:/Study/Jean Monnet/Advanced Algoirthm/Project/Data/a280.tsp') as f:
	
	num = 0 #统计城市数目
	find_num = False # 标记找到的下一行即为真实城市数据
	# corMat = np.array()
	temMat = []
	# corMat = [] #空列表，保存城市的坐标
	data = f.readlines()

	for line in data:
		line = line.rstrip('\n') # 读取文件时逐行读取的话，在每一行的末尾会录入一个 \n 换行符
		
		if find_num:
			string_data = line.split()
			temMat.append(string_data)
			# tem = np.array(string_data)
			# real_data = map(float, string_data)
			# print(real_data)
			# corMat[num][0:2] = real_data
			num = num + 1		
		
		if line == "NODE_COORD_SECTION":
			find_num = True

	temMat = temMat[0:num-1]

	corMat = np.array(temMat)
	corMat = corMat.astype(np.float64)
print(corMat[0][2])