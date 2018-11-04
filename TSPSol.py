#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-03 10:36:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import numpy as np
import ExtractData as ED

class tspDP:

	def __init__(self,disMat,numC):
		#注意，这里的 numC 已经包含了起始城市
		self.disMat = disMat
		self.numC = numC
		# 初始化动规矩阵
		#其长度为 2^n(number of set),宽度为 n (cities)
		self.inf = 999999

		#初始化dp数组
		self.dp = np.full((self.Convert(),numC),self.inf)

		for i in range(0,self.numC ):
			self.dp[0][i] = disMat[0][i]


	def Convert(self):
		# 进行集合的二进制转换
		# 所有状态的集合一共为 2^n
		return np.power(2,self.numC - 1)

	def Algo(self):
		#注意这里处理从第二个城市到最后一个城市这之间的距离
		#从第二个城市进行处理是因为第一个城市为城市 0 
		#因为 TSP 为一个环，所以最后还要处理从最后一个城市到 0

		for i in range(1,self.Convert()):
			#这里循环的是顶点的数目
			for j in range(1,self.numC):
				#这里循环的是所有 在 set 中的顶点数目
				for k in range(1,self.numC): # 在数据中，城市从 0 ~ N-1
					#首先判定当前顶点是否在 set 中
					tem = 1<<(k-1)
					if (tem & i):
						#表示当前搜寻的顶点存在于当前的集合i中
						self.dp[i][j] = min(self.dp[i][j],self.dp[i-tem][k] + self.disMat[k][j])
		# 处理 N-1 ~ 0 这段距离
		shortestPath = self.inf
		for i in range(1,self.numC):
			shortestPath = min(shortestPath,self.dp[self.Convert() - 1][i] + self.disMat[i][0])
		return shortestPath

corMat,disMat,numC = ED.PreData()

DP = tspDP(disMat,numC)
print(DP.Algo())