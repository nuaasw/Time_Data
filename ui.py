# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os,sys
from PyQt5 import  QtCore,QtWidgets,QtGui
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont

from base import TimeData as ays
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        """
        :type Dialog: object
        """
        Dialog.setObjectName("Hello World!")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.inputBox = QPushButton("&出差工时比",Dialog)
        self.inputBox.setFont(QFont('黑体',10))
        # self.inputBox.setEnabled(1)
        self.inputBox.setGeometry(QtCore.QRect(30,50,100,50))
        self.inputBox.clicked.connect(ays.timeDataAys)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.close)
        self.buttonBox.rejected.connect(self.printSuccess)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    #   显示Qt界面
        Dialog.show()

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