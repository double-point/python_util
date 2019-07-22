# encoding:utf-8
# FileName: pymatplotlib
# Author:   wzg
# email:    1010490079@qq.com
# Date:     2019/7/22 下午 08:52
# Description: Python matplotlib使用

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 获取当前文件夹的路径
dir_path = os.getcwd()

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as psl
from numpy import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

reload(sys)
sys.setdefaultencoding('utf-8')

def chart_line(data):
    # 折线图
    plt.xlabel("x label line chart")
    plt.ylabel("y label line chart")
    plt.title("this is line chart title")
    # 设置ｘ轴刻度数据: 最好根据数据的取值范围划分刻度
    plt.xticks(range(40))
    # 显示网格，注意网格线的参数和plt.plot画图时的参数
    plt.grid(True, linestyle="--", color="gray", linewidth=0.5, axis="both")
    # 设置刻度显示方向
    plt.tick_params(bottom='on', top='off', left='on', right='off')
    # 设置ｘ轴主次刻度，如下：主刻度为２的倍数，副刻度为５的倍数
    plt.subplot().xaxis.set_major_locator(MultipleLocator(2))
    plt.subplot().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.subplot().xaxis.set_minor_locator(MultipleLocator(5))
    plt.subplot().xaxis.set_minor_formatter(FormatStrFormatter('%.2f'))
    plt.subplot().xaxis.grid(True, which="both")
    # 关闭刻度值，都不显示
    # plt.axis("off")
    plt.plot(np.random.rand(20), marker='*', linestyle='--', color='red', alpha=0.8)
    # 设置某个点显示注解
    plt.text(5, 0.5, 'this is annotation data(5,0.5)', fontsize=10)
    # 保存图到本地图片
    plt.savefig('test.png', dpi=400, bbox_inches='tight', facecolor='orange', edgecolor='b')
    plt.show()


def chart_bar(data):
    # 柱状图
    plt.xlabel("x label bar chart")
    plt.ylabel("y label bar chart")
    plt.title("this is bar chart title")
    # 设置x，y轴数据
    data_x = np.arange(5)
    data_y = np.random.rand(5) * 10
    # 设置x轴柱子的类别
    plt.xticks(data_x, ('a', 'b', 'c', 'd', 'e'))
    # 设置柱状图的参数
    plt.bar(data_x, data_y, orientation='vertical', align='edge', edgecolor='white', facecolor='yellowgreen',
            yerr=data_y * 0.1)
    # 设置柱状图显示数值
    for i, j in zip(data_x, data_y):
        plt.text(i + 0.3, j - 0.5, '%.2f' % j, color='black')
    plt.show()


def chart_scatter(data):
    # 散点图
    plt.xlabel("x label scatter chart")
    plt.ylabel("y label scatter chart")
    plt.title("this is scatter chart title")
    # 设置x，y轴数据
    data_x = np.arange(20)
    data_y = np.random.rand(20)
    # 设置散点图的参数，其中c为色彩序列，为一个数组, cmap为颜色渐变(_r为反转)，结合c使用
    chart_scatter = plt.scatter(data_x, data_y, alpha=0.5, s=75, c=data_x*data_y, cmap=plt.cm.get_cmap('RdYlBu'))
    # 设置散点图颜色渐变的提示柱状图。
    plt.colorbar(chart_scatter)

    # 设置散点图显示数值
    for i, j in zip(data_x, data_y):
        plt.text(i, j, '(%.2f,%.2f)' %(i,j), color='black')

    plt.show()


def chart_area(data):
    # 面积图 注意生成图的方式不同于其他图
    fig, axes = plt.subplots(2,1)
    data_x = pd.DataFrame(np.random.rand(10,4), columns=['a', 'b', 'c', 'd'])
    # 设置面积图
    data_x.plot.area(colormap='Greens', alpha=0.5, ax = axes[0], stacked=False)
    plt.show()


def chart_fill(data):
    # 填图
    fig, axes = plt.subplots(2, 1, figsize=(8, 6))
    # 默认为最后一个图优先
    plt.xlabel("x label fill chart")
    plt.ylabel("y label fill chart")
    plt.title("this is fill chart title")
    # 设置x，y轴数据
    data_x = np.linspace(0, 1, 500)
    data_y1 = np.sin(4 * np.pi * data_x) * np.exp(-5 * data_x)
    data_y2 = -np.sin(4 * np.pi * data_x) * np.exp(-5 * data_x)
    # plt.fill(data_x, data_y1, 'red', data_x, data_y2, 'green', alpha=0.50)
    # 同上使用方法，每个函数与x轴相交部分
    axes[1].fill(data_x, data_y1, 'red', data_x, data_y2, 'green', alpha=0.50)
    # 两个函数的相交部分
    axes[0].fill_between(data_x, data_y1, data_y2, color='blue', alpha=0.5)

    plt.show()


def chart_stack(data):
    # 堆积图
    # plt.xlabel("this is stack chart xlabel")
    # plt.ylabel("this is stack chart ylabel")
    # plt.title("this is stack chart title")
    # 注意堆积图的数据为dataframe,且参数stack设置为true
    df_data = pd.DataFrame(np.random.rand(10,4), columns=['a', 'b', 'c', 'd'])
    df_data.plot(kind="bar", stacked="True", cmap=plt.cm.get_cmap("Blues_r"))
    plt.show()

def chart_pie(data):
    # 饼图
    plt.xlabel("this is pie chart label")
    plt.title("this is pie chart title")
    # 设置xy数据
    data = pd.Series(np.random.rand(5)*10, )
    # 设置饼图数据
    plt.pie(data, explode=[0.05,0.05,0.05,0.05,0.1], labels=['a','b','c','d','e'], colors=['red','blue','yellow','c','green'],
            autopct='%.2f %%', shadow=True, startangle=90, counterclock=False)
    plt.show()


def chart_hist(data):
    # 直方图
    plt.xlabel("this is hist chart xlabel")
    plt.ylabel("this is hist chart ylabel")
    plt.title("this is hist chart title ")
    # 生成直方图数据x
    data = pd.Series(np.random.rand(100)*100).astype(int)
    # print data
    # 设置直方图数据
    plt.hist(data, bins=50, histtype='bar', orientation="vertical", )
    plt.show()


def chart_polar1(data):
    # 极坐标图
    ax1 = plt.subplot(121, polar=True)
    data_x = np.arange(9)
    data_y = np.random.rand(9)*10
    ax1.plot(data_x, data_y,)
    # 设置坐标轴方向，-1为顺时针，默认为逆时针
    ax1.set_theta_direction(-1)
    # 设置网格线0-360 45为一度
    ax1.set_thetagrids(np.arange(0.0,360.0,45.0),['a','b','c','d','e','f','g','h'])
    plt.show()


def chart_polar2(data):
    # 雷达图
    angles = np.linspace(0, 2*np.pi, 7, endpoint=False)
    data = np.random.randint(0, 10, 7)
    # 数据进行首尾合并，形成闭区间
    angles = np.concatenate((angles, [angles[0]]))
    data = np.concatenate((data, [data[0]]))
    plt.polar(angles, data, )
    plt.fill(angles, data, )
    plt.show()


def chart_box(data):
    # 箱型图
    # plt.xlabel("this is box chart xlabel")
    # plt.title("this is box chart title")
    # 设置数据
    data = pd.DataFrame()
    data[u"数学"] = [11,55,99,66,2,24,55,77,445,45,25,221]
    data[u"英语"] = [76,90,97,71,70,93,86,83,78,85,81,11]
    # 设置箱型图
    color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
    # sym:异常点形状  vert:是否垂直  meanline:显示均值线  whis:IQR ,默认1.5
    data.plot.box(grid=True, color=color, sym='o', showmeans=True)
    plt.show()


if __name__ == '__main__':
    read_filepath = os.path.join(dir_path, u"source_data\\train.csv")
    df_data = pd.read_csv(read_filepath)
    # df_data = pd.isnull
    # 数据的字段和缺失情况统计
    print df_data.columns
    print df_data.info()

    # 折线图
    # chart_line(df_data)
    # 柱状图
    # chart_bar(df_data)
    # 堆积图
    # chart_stack(df_data)
    # 面积图
    # chart_area(df_data)
    # 填图
    # chart_fill(df_data)
    # 饼图
    # chart_pie(df_data)
    # 直方图：区别柱状图
    chart_hist(df_data)
    # 散点图
    # chart_scatter(df_data)
    # 极坐标图
    # chart_polar1(df_data)
    # 雷达图
    # chart_polar2(df_data)
    # 箱型图
    # chart_box(df_data)