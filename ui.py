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
from PyQt5.QtGui import QFont as font

from base import TimeData as ays

class Ui_Dialog(object):
    def __init__(self,name= ' '):
        self.name = name

    def setupUi(self, Dialog):
        """
        :type Dialog: object
        """
        Dialog.setObjectName("Hello World!")
        Dialog.resize(600, 400)

        self.allButton = button("&出差工时比",Dialog)

        self.allButton.setFont(font('黑体',10))
        self.allButton.setGeometry(QtCore.QRect(400,180,150,30))
        # dataays = ays('HelloTest')

        self.allButton.clicked.connect(self.testJob)


        self.closeButton = button("&Close",Dialog)
        self.closeButton.setFont(font('黑体',10))
        self.closeButton.setGeometry(QtCore.QRect(400,220,150,30))
        self.closeButton.clicked.connect(Dialog.close)

        self.showLabel = label(Dialog)
        self.showLabel.setText("Hello")
        self.showLabel.setGeometry(QtCore.QRect(10,10,400,400))

        self.lineedit_1 = lineedit(Dialog)
        self.lineedit_1.setGeometry(QtCore.QRect(400,120,150,30))
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
        print(self.lineedit_1.text())
        dataays = ays(self.lineedit_1.text())
        print(dataays.getFilename())
        dataays.timeDataAys()
        # self.lineedit_1.setText(self.name)
        # print(self.name)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(w)
    sys.exit(app.exec_())