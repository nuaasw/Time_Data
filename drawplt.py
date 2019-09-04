import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # /用来正常显示负号
        # plt.show()
        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        self.fig.suptitle('工时数据分析')

        # self.axes.hold(False)  # 每次绘图的时候不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        # FigureCanvas.setSizePolicy(self,
                                   # QSizePolicy.Expanding,
                                   # QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)


    '''绘制静态图，可以在这里定义自己的绘图逻辑'''

    def start_static_plot(self,datas={}):
        self.fig.suptitle('工时数据分析')
        t = list(datas.keys())
        s = list(datas.values())
        self.axes.plot(t,s)
        self.axes.set_ylabel('静态图：Y轴')
        self.axes.set_xlabel('静态图：X轴')
        self.axes.grid(True)
        self.draw()

    def start_static_plot(self,keys=[],values=[]):
        plt.show()
        t = keys[:]
        s = values[:]
        # plt.bar(t,s)
        # plt.show()
        self.axes.set_xticks(range(len(t)),t)
        self.axes.plot(s)
        self.axes.set_ylabel('静态图：Y轴')
        self.axes.set_xlabel('静态图：X轴')
        self.axes.grid(True)
        self.draw()

