# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os,sys
from PyQt5 import  QtCore,QtWidgets,QtGui
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtWidgets import QPushButton as button
from PyQt5.QtWidgets import QLabel as label
from PyQt5.QtWidgets import QLineEdit as lineedit
from PyQt5.QtWidgets import QVBoxLayout,QWidget
from PyQt5.QtGui import QFont as font
from drawplt import MyMplCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from base import TimeData as ays

class Ui_Dialog(QWidget):
    def __init__(self,Dialog,name= ' ',parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.name = name
        self.dataResult = []
        self.overData = []
        self.partData = []
        self.orgPeople = {}
        self.mpl = MyMplCanvas(self, width=5.5, height=4, dpi=160)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        self.setupUi(Dialog)
        # print('test')

    def setupUi(self, Dialog):
        """
        :type Dialog: object
        """
        Dialog.resize(1100, 800)

        self.layout = QVBoxLayout(Dialog)
        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)
        # 提示Label
        self.showLabel = label(Dialog)
        self.showLabel.setText("Wait Operation!")
        self.showLabel.setGeometry(QtCore.QRect(10, 20, 300, 30))
        self.showLabel.setFont(font('黑体', 12))

        # 数据路径,暂时指定路径
        # self.lineedit_1 = lineedit(Dialog)
        # self.lineedit_1.setGeometry(QtCore.QRect(900, 100, 150, 30))
        # self.lineedit_1.setText('./test.csv')
        x=60

        self.allButton = button("总工时数据",Dialog)
        self.allButton.setFont(font('黑体',10))
        self.allButton.setGeometry(QtCore.QRect(900,80-x,150,40))
        self.allButton.clicked.connect(self.allDataJob)

        self.overButton = button("员工加班工时",Dialog)
        self.overButton.setEnabled(False)
        self.overButton.setFont(font('黑体', 10))
        self.overButton.setGeometry(QtCore.QRect(900, 140-x, 150, 40))
        self.overButton.clicked.connect(self.overDataJob)

        self.outButton = button("员工出差工时",Dialog)
        self.outButton.setEnabled(False)
        self.outButton.setFont(font('黑体', 10))
        self.outButton.setGeometry(QtCore.QRect(900, 200-x, 150, 40))
        self.outButton.clicked.connect(self.outDataJob)


        self.kpiButton = button("员工KPI100H",Dialog)
        self.kpiButton.setEnabled(False)
        self.kpiButton.setFont(font('黑体', 10))
        self.kpiButton.setGeometry(QtCore.QRect(900, 260-x, 150, 40))
        self.kpiButton.clicked.connect(self.kpiDataJob)

        self.avgPartAllButton = button("部门人均总工时",Dialog)
        # self.avgPartAllButton.setEnabled(False)
        self.avgPartAllButton.setFont(font('黑体',10))
        self.avgPartAllButton.setGeometry(QtCore.QRect(900, 320-x, 150, 40))
        self.avgPartAllButton.clicked.connect(self.partAllData)

        self.avgPartOverButton = button("部门人均加班工时", Dialog)
        # self.avgPartOverButton.setEnabled(False)
        self.avgPartOverButton.setFont(font('黑体', 10))
        self.avgPartOverButton.setGeometry(QtCore.QRect(900, 380-x, 150, 40))
        self.avgPartOverButton.clicked.connect(self.partOverData)

        self.avgPartOutButton = button("部门人均出差工时", Dialog)
        # self.avgPartOutButton.setEnabled(False)
        self.avgPartOutButton.setFont(font('黑体', 10))
        self.avgPartOutButton.setGeometry(QtCore.QRect(900, 440-x, 150, 40))
        self.avgPartOutButton.clicked.connect(self.partOutData)

        self.avgPartKpiButton = button("部门KPI100h工时", Dialog)
        # self.avgPartKpiButton.setEnabled(False)
        self.avgPartKpiButton.setFont(font('黑体', 10))
        self.avgPartKpiButton.setGeometry(QtCore.QRect(900, 500-x, 150, 40))
        self.avgPartKpiButton.clicked.connect(self.partKpiData)

        self.projectAllButton = button("项目总工时",Dialog)
        self.projectAllButton.setEnabled(False)
        self.projectAllButton.setFont(font('黑体',10))
        self.projectAllButton.setGeometry(QtCore.QRect(900, 560-x, 150, 40))

        self.projectOverButton = button("项目总工时", Dialog)
        self.projectOverButton.setEnabled(False)
        self.projectOverButton.setFont(font('黑体', 10))
        self.projectOverButton.setGeometry(QtCore.QRect(900, 620-x, 150, 40))

        self.projectOutButton = button("项目出差工时", Dialog)
        self.projectOutButton.setEnabled(False)
        self.projectOutButton.setFont(font('黑体', 10))
        self.projectOutButton.setGeometry(QtCore.QRect(900, 680-x, 150, 40))

        self.closeButton = button("&关闭",Dialog)
        self.closeButton.setFont(font('黑体',10))
        self.closeButton.setGeometry(QtCore.QRect(900,740-x,150,40))
        self.closeButton.clicked.connect(Dialog.close)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.show()

    # def textChanged(self,Dialog):
    #     self.showLabel.setText("Go!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def printSuccess(self):
        print('Success!')

    def allDataJob(self):
        # dataays = ays(self.lineedit_1.text())
        dataays = ays('./test.csv')
        self.dataResult = dataays.timeDataAys()
        self.orgPeople = dataays.calOrgData(self.dataResult[1])
        self.showLabel.setText('员工总工时数据计算成功！')
        self.overButton.setEnabled(True)
        self.outButton.setEnabled(True)
        self.kpiButton.setEnabled(True)
        self.mpl.start_static_plot(list(self.dataResult[0]),self.dataResult[2],'员工总工时数据','员工编号','总工时')
        # test
        self.partData = dataays.calTimeDate(self.orgPeople,self.dataResult)
        print('test')

    def overDataJob(self):
        self.mpl.start_static_plots(list(self.dataResult[0]), self.dataResult[2],self.dataResult[4], '员工加班工时数据', '员工编号', '加班工时')

    def outDataJob(self):
        self.mpl.start_static_plots(list(self.dataResult[0]), self.dataResult[2],self.dataResult[5], '员工出差工时数据', '员工编号', '出差工时')

    def kpiDataJob(self):
        self.mpl.start_static_plots(list(self.dataResult[0]), self.dataResult[2],self.dataResult[4]+self.dataResult[5], '员工KPI工时数据', '员工编号', 'KPI工时')

    def partAllData(self):
        self.mpl.start_static_plot(list(self.partData[0]),self.partData[1],'部门总工时数据','部门编号','总工时',1)

    def partOverData(self):
        # print(self.partData[0])
        self.mpl.start_static_plots(self.partData[0],self.partData[1],self.partData[2],'部门加班工时数据','部门编号','加班工时',1)

    def partOutData(self):
        self.mpl.start_static_plots(self.partData[0],self.partData[1],self.partData[3],'部门出差工时数据','部门编号','出差工时',1)

    def partKpiData(self):
        # print(self.partData[0])
        self.mpl.start_static_plots(self.partData[0],self.partData[1],self.partData[3]+self.partData[4],'部门KPI工时数据','部门编号','KPI工时',1)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    Ui_Dialog(w)
    w.setWindowTitle('ASD工时分析软件')
    # w.show()
    sys.exit(app.exec_())