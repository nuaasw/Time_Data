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
        self.orgPeople = {}
        self.setupUi(Dialog)
        # print('test')

    def setupUi(self, Dialog):
        """
        :type Dialog: object
        """
        # Dialog.setObjectName("Hello World!")
        Dialog.resize(800, 500)

        self.layout = QVBoxLayout(Dialog)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl.start_static_plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


        self.allButton = button("&Calculate",Dialog)

        self.allButton.setFont(font('黑体',10))
        self.allButton.setGeometry(QtCore.QRect(600,160,150,30))
        # dataays = ays('HelloTest')

        self.allButton.clicked.connect(self.testJob)


        self.closeButton = button("&Close",Dialog)
        self.closeButton.setFont(font('黑体',10))
        self.closeButton.setGeometry(QtCore.QRect(600,200,150,30))
        self.closeButton.clicked.connect(Dialog.close)

        self.showLabel = label(Dialog)
        self.showLabel.setText("Wait Operation!")
        self.showLabel.setGeometry(QtCore.QRect(10,20,300,30))
        self.showLabel.setFont(font('黑体',12))

        self.lineedit_1 = lineedit(Dialog)
        self.lineedit_1.setGeometry(QtCore.QRect(600,120,150,30))
        self.lineedit_1.setText('./test.csv')

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(self.printSuccess)
        # self.buttonBox.rejected.connect(Dialog.close)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    #   显示Qt界面
        Dialog.show()

    def textChanged(self,Dialog):
        self.showLabel.setText("Go!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def printSuccess(self):
        print('Success!')

    def testJob(self):
        dataays = ays(self.lineedit_1.text())
        self.dataResult = dataays.timeDataAys()
        self.orgPeople = dataays.calOrgData(self.dataResult[1])
        self.showLabel.setText('数据预处理成功！')
        dataays.getOrgImg(self.orgPeople)
        self.mpl.start_static_plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉

        # self.lineedit_1.setText(self.orgPeople.value(1))

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    Ui_Dialog(w)
    # w.show()
    sys.exit(app.exec_())