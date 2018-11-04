#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-03 10:36:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import numpy as np
import ExtractData as ED


class TSPsolve:

	def __init__(self,disMat,start_node,num):

		#初始化距离矩阵以及开始点
		self.disMat = disMat
		self.start_node = start_node
		self.num = num
		#创立一个回溯矩阵，矩阵大小为距离矩阵列维度大小的 2^n，初始化全为0
		# num 为传入的城市数目
		self.Traceback = [[0]*(2**num) for i in range(num)]


	def TSP_ini(self):

		cities_set = list(range(self.num))
		pass_set = [self.start_node]

		# 初始化剩下的节点列表，在初始化中也就是除去开始节点
		cities_set.pop(cities_set.index(self.start_node))
		node = self.start_node

		return self.solve(node,cities_set)

	def TSP_Convert(self,sets):

		#将集合转化为2进制进行计算
		set_Bin = 0
		for i in sets:
			set_Bin = set_Bin + np.power(2,i)
		return set_Bin

	def solve(self,node,future_sets):

		if len(future_sets) == 0:
			#如果集合中没有任何元素，则返回当前顶点与初始顶点之间的距离
			#也是我们最初掌握的数据
			return self.disMat[self.start_node][node]

		d = 999999 #初始化 d
		#定义距离矩阵，注意在 DP 的时候，每一层向上返回值的时候，都要进行比较
		distance = [] #这个矩阵在每一层比较的时候都会被重新更新为 0 

		for i in range(len(future_sets)):

			#选出当前的节点，并作为下一层的起点
			Current_node = future_sets[i] 

			#将全部节点复制，从总节点中删除当前节点，并传入下一层
			rest_sets = future_sets[:]
			rest_sets.pop(i)

			#算出其全部子集，再加上子集顶点到当前顶点的距离，
			distance.append(self.disMat[node][Current_node] + self.solve(Current_node,rest_sets))

		d = min(distance) #选取子集中距离最小的那个

		#将数据录入 TraceBack 矩阵
		Next_node = future_sets[distance.index(d)]
		#将未走过的集合转化为二进制，从而进行回溯
		Bin_set = self.TSP_Convert(future_sets)
		self.Traceback[node][Bin_set] = Next_node

		return d


D = [[-1,10,20,30,40,50],[12,-1,18,30,25,21],[23,19,-1,5,10,15],[34,32,4,-1,8,16],[45,27,11,10,-1,18],[56,22,16,20,12,-1]]

S = TSPsolve(D,0,len(D))
print(S.TSP_ini())










		


