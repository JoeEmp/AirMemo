# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\logout_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 210)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 189))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.logout_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.logout_btn.setObjectName("logout_btn")
        self.gridLayout.addWidget(self.logout_btn, 1, 1, 1, 1)
        self.wel_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.wel_lab.setObjectName("wel_lab")
        self.gridLayout.addWidget(self.wel_lab, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.logout_btn.setText(_translate("Dialog", "logout"))
        self.wel_lab.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; font-weight:96; color:#5f6266; background-color:#f9fbfc;\">Thank you support!!!</span></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; color:#5f6266; background-color:#f9fbfc;\">We will then keep you up to date</span><br/></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; font-weight:600; color:#5f6266; background-color:#f9fbfc;\">%s</span></p></body></html>"))

