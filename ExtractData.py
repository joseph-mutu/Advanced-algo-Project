#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-29 18:07:50
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import numpy as np

def PreData():
#此函数将获取一个文件名，文件名为 TSP 数据 ----  此项尚未完成
#并将读取数据最终输出城市坐标以及城市数目
		with open('D:/Study/Jean Monnet/Advanced Algoirthm/Project/Data/a280.tsp') as f:
			num = 0 #统计城市数目
			find_num = False # 标记找到的下一行即为真实城市数据
			temMat = []
			data = f.readlines()

			for line in data:
				line = line.rstrip('\n') # 读取文件时逐行读取的话，在每一行的末尾会录入一个 \n 换行符
				
				if find_num:	

					#将数据按照空格分开
					string_data = line.split()
					temMat.append(string_data)

					num = num + 1		#统计城市数目
				
				if line == "NODE_COORD_SECTION":
					# 在 NODE_COORD_SECTION 的下一行即为真实数据
					find_num = True

		# 读取到的文件最后一行有 EOF 标识
			temMat = temMat[0:num-1]
		#将 List 数据转化为 array 数据
			corMat = np.array(temMat)
			corMat = corMat.astype(np.float64)

			# 以下计算城市距离矩阵
			disMat = np.zeros((num-1,num-1),dtype = np.float64) #初始化距离矩阵
			for i in range(num-1):
				for j in range(num-1):
					#计算两个城市之间的欧式距离
					if i != j:

						temDis = np.sqrt( np.square(corMat[i][1]-corMat[j][1]) 
							+ np.square(corMat[i][2]-corMat[j][2]) )

						disMat[i][j] = disMat[j][i] = temDis
					else:
						disMat[i][j] = 0

		# 其中 corMat 即为城市坐标矩阵，disMat 为城市距离矩阵，num-1 则为城市数目
			return corMat,disMat,num-1;

	# CorMat, num_cities = PreData()