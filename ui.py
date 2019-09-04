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
        self.orgPeople = {}
        self.mpl = MyMplCanvas(self, width=5.5, height=4, dpi=150)
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


        self.allButton = button("总工时数据",Dialog)
        self.allButton.setFont(font('黑体',10))
        self.allButton.setGeometry(QtCore.QRect(900,80,150,40))
        self.allButton.clicked.connect(self.allDataJob)

        self.overButton = button("加班工时",Dialog)
        self.overButton.setEnabled(False)
        self.overButton.setFont(font('黑体', 10))
        self.overButton.setGeometry(QtCore.QRect(900, 140, 150, 40))
        self.overButton.clicked.connect(self.overDataJob)

        self.outButton = button("出差工时",Dialog)
        self.outButton.setEnabled(False)
        self.outButton.setFont(font('黑体', 10))
        self.outButton.setGeometry(QtCore.QRect(900, 200, 150, 40))
        self.outButton.clicked.connect(self.outDataJob)


        self.kpiButton = button("KPI100H",Dialog)
        self.kpiButton.setEnabled(False)
        self.kpiButton.setFont(font('黑体', 10))
        self.kpiButton.setGeometry(QtCore.QRect(900, 260, 150, 40))
        self.kpiButton.clicked.connect(self.kpiDataJob)


        self.closeButton = button("&关闭",Dialog)
        self.closeButton.setFont(font('黑体',10))
        self.closeButton.setGeometry(QtCore.QRect(900,320,150,40))
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
        print('test')

    def overDataJob(self):
        self.mpl.start_static_plots(list(self.dataResult[0]), self.dataResult[2],self.dataResult[4], '员工加班工时数据', '员工编号', '加班工时')

    def outDataJob(self):
        self.mpl.start_static_plots(list(self.dataResult[0]), self.dataResult[2],self.dataResult[5], '员工出差工时数据', '员工编号', '出差工时')

    def kpiDataJob(self):
        self.mpl.start_static_plots(list(self.dataResult[0]), self.dataResult[2],self.dataResult[4]+self.dataResult[5], '员工出差加班工时数据', '员工编号', '出差加班工时')

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    Ui_Dialog(w)
    w.setWindowTitle('ASD工时分析软件')
    # w.show()
    sys.exit(app.exec_())