#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-29 18:07:50
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import numpy as np
import math

def PreData(method):
#此函数将获取一个文件名，文件名为 TSP 数据 ----  此项尚未完成
#并将读取数据最终输出城市坐标以及城市数目
		with open('D:/Study/Jean Monnet/Advanced Algoirthm/Project/Data/gr666.tsp') as f:
			num = 0 #统计城市数目
			find_num = False # 标记找到的下一行即为真实城市数据
			temMat = []
			data = f.readlines()
			numJudge = 0

			for line in data:

				stringJudge = []
				line = line.rstrip('\n') # 读取文件时逐行读取的话，在每一行的末尾会录入一个 \n 换行符
				stringJudge = line.split()

				# print(stringJudge)
				if stringJudge[0] == 'DIMENSION:':	
					#取得一共多少维矩阵
					numJudge = np.int(stringJudge[1])

				if find_num:	
					#将数据按照空格分开
					if numJudge:
						string_data = line.split()
						temMat.append(string_data)
						numJudge = numJudge - 1
						
					else:
						break

					num = num + 1		#统计城市数目
				
				if stringJudge[0] == "NODE_COORD_SECTION":
					# 在 NODE_COORD_SECTION 的下一行即为真实数据
					find_num = True

		# 读取到的文件最后一行有 EOF 标识
			# temMat = temMat[0:num-1]
		#将 List 数据转化为 array 数据

			# corMat = map(float,temMat)
			corMat = np.array(temMat)
			corMat = corMat.astype(np.float64)
			corMat = corMat[:,1:3]

			# 以下计算城市距离矩阵
			disMat = np.zeros((num,num),dtype = np.float64) #初始化距离矩阵
##########################################################################
			#EU_2D
			if method == "eu":
				for i in range(num):
					for j in range(num):
						#计算两个城市之间的欧式距离
						if i != j:
							xd = corMat[i][0]-corMat[j][0]
							yd = corMat[i][1]-corMat[j][1]

							# temDis = (int)(np.sqrt(np.float((xd*xd + yd*yd) ) ) + 0.5)
							temDis = (int)(math.sqrt((xd*xd + yd*yd) ) + 0.5)

							disMat[i][j] = disMat[j][i] = temDis

##############################################################################

##############################################################################
			#GEO Distance
			if method == "geo":
				# Latitude is geoMat[:][0]
				# longitude is geoMat[:][1]


				geoMat = np.zeros((num,2),dtype = np.float64)
				PI = np.float64(3.141592)
				RRR = np.float64(6378.388)

				for i in range(num):
					x = corMat[i][0]
					deg = (int)(x)
					min = np.float(x - deg)
					geoMat[i][0] = np.float(PI * (deg + 5.0 * min / 3.0) / 180.0 )

					y = corMat[i][1]
					deg = (int)(y)
					min = np.float(y - deg)
					geoMat[i][1] = np.float(PI * (deg + 5.0 * min / 3.0) / 180.0 )

				for i in range(num):
					for j in range(num):
						if i != j:
							q1 = np.float( np.cos(geoMat[i][1] - geoMat[j][1]) )
							q2 = np.float( np.cos(geoMat[i][0] - geoMat[j][0]) )
							q3 = np.float( np.cos(geoMat[i][0] + geoMat[j][0]) )
							disMat[i][j] = (np.int64)( RRR * np.arccos( 0.5 * ((1.0 + q1) * q2 
								- (1.0 - q1) * q3) ) + 1.0 ) 

##############################################################################

			#距离矩阵保留两位小数
			# disMat = np.around(disMat,decimals = 6)

		# 其中 corMat 即为城市坐标矩阵，disMat 为城市距离矩阵，num-1 则为城市数目
			return corMat,disMat,num;