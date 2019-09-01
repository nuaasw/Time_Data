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
from PyQt5.QtGui import QFont as font

from base import TimeData as ays

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        """
        :type Dialog: object
        """
        Dialog.setObjectName("Hello World!")
        Dialog.resize(600, 400)

        self.allButton = button("&出差工时比",Dialog)

        self.allButton.setFont(font('黑体',10))
        self.allButton.setGeometry(QtCore.QRect(400,180,150,30))
        # dataays = ays('Hello')
        self.allButton.clicked.connect(ays.timeDataAys)

        self.closeButton = button("&Close",Dialog)
        self.closeButton.setFont(font('黑体',10))
        self.closeButton.setGeometry(QtCore.QRect(400,220,150,30))
        self.closeButton.clicked.connect(Dialog.close)

        self.showLabel = label(Dialog)
        self.showLabel.setText("Hello")
        self.showLabel.setGeometry(QtCore.QRect(10,10,400,400))


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

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(w)
    sys.exit(app.exec_())