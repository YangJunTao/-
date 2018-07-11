# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:37:38 2018

@author: PC-XXX
"""
import pandas as pd
import os
import matplotlib.pyplot as plt


for root, dirs, files in os.walk('E:\大数据学习群\POI\\'):
	L = ['E:\大数据学习群\POI\\'+file for file in files]

poi_name = [i.split('_')[0] for i in files]
poi_num = {'宝安区':[], '龙岗区':[], '福田区':[], '南山区':[], '罗湖区':[], '盐田区':[]}    #每个区各种POI分布 
counts = 0  #保存每个区POI总量
# =============================================================================
# for i in L:
#     POI = i.split('\\')[-1].split('_')[0]
#     data = pd.read_excel(i)
#     try:
#         data = data[data['city'] == '深圳市']   #筛选city为深圳市的行
#         #print(POI+'分类在深圳市地区分布为：\n%s'%data.district.value_counts())
#         for i in poi_num:
#             poi_num[i].append(data.district.value_counts()[i])
#         counts += data.district.value_counts()
#     except:
#         data = data[data['adname'] == '深圳市']
#         #print(POI+'分类在深圳市地区分布为：\n%s'%data.shopid.value_counts())
#         for i in poi_num:
#             poi_num[i].append(data.shopid.value_counts()[i])
#         counts += data.shopid.value_counts()
# 
# print('总分布为：\n%s'%counts)
# =============================================================================

def showBarChart(counts):   #生成柱状图
    counts = counts.reset_index()
    x = counts['index']
    y = counts['district']
    plt.figure(figsize=(10, 6), dpi=100)
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.bar(x, y)
    plt.xlabel('区域')
    plt.ylabel('数量')
    plt.title('深圳市POI数量分布柱状图')  
    for a,b in zip(x,y):
        plt.text(a, b, b, ha='center', va='bottom')
           
    plt.show()
    pass

def showPieChart(district): #生成饼状图
    count = []
    for i in range(11):
        n = 0
        for d in district:
            n+=district[d][i]
        count.append(n)
        
    plt.figure(figsize=(9, 9), dpi=100)
    plt.rcParams["font.sans-serif"]=['SimHei']  # 用于正常显示中文标签
    plt.style.use('ggplot')
    plt.axes(aspect= 'equal')
    plt.title('深圳市POI数量分布饼状图', fontsize = 20)  
    
    labels = poi_name
    plt.pie(x=count, labels=labels,textprops = {'fontsize':10, 'color':'k'}, autopct= '%.1f%%')
    plt.show()
    pass
