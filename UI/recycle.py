# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\recycle.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

import utils
import config


class Ui_recycle_Dialog(QtWidgets.QDialog):
    sel_signal = pyqtSignal(str)

    def __init__(self, parent, username):
        super().__init__(parent=parent)
        self.set_data(username)
        self.setupUi()
        self.show()

    def set_data(self, username):
        self.del_records = utils.get_records(config.LDB_FILENAME, username,
                                             is_del='1')

    def setupUi(self):
        self.setObjectName("recycle_Dialog")
        self.resize(config.TEXT_WIDTH,
                    config.BTN_HEIGHT * len(self.del_records) + 30)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(
                QtCore.QRect(10, 10, config.TEXT_WIDTH,
                             config.BTN_HEIGHT * len(self.del_records)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        for i in range(len(self.del_records)):
            self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
            self.checkBox.setObjectName("checkBox" + str(i))
            self.verticalLayout.addWidget(self.checkBox)
            self.checkBox.setText(self.del_records[i][1])

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "回收站"))
        self.pushButton_2.setText(_translate("Dialog", "还原"))
