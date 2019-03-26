# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\recycle.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

import config
import utils


class Ui_recycle_Dialog(QtWidgets.QDialog):
    updateSignal = pyqtSignal(str)
    item_set = set()

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.set_data(parent.user_info['username'])
        self.parent = parent
        self.setupUi()
        self.show()

    def set_data(self, username):
        self.del_records = utils.get_records(config.LDB_FILENAME, username,
                                             is_del='1')

    def setupUi(self):
        self.setObjectName("recycle_Dialog")
        self.resize(config.TEXT_WIDTH,
                    config.BTN_HEIGHT * len(self.del_records) * 2 + 50)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(
                QtCore.QRect(10, 10, config.TEXT_WIDTH,
                             config.BTN_HEIGHT * len(
                                 self.del_records) * 2 + 30))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        for i in range(len(self.del_records)):
            self.message_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
            self.message_check.setObjectName("message_check" + str(self.del_records[i][0]))
            # 设置 msg
            self.message_check.setText(self.del_records[i][1])
            self.message_check.clicked.connect(self.set_list)
            self.verticalLayout.addWidget(self.message_check)

            self.detail_sub_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.detail_sub_lab.setObjectName("detail_sub_lab" + str(self.del_records[i][0]))
            # 设置 detail
            if not self.del_records[i][2]:
                self.detail_sub_lab.setText('无详细信息')
            elif len(self.del_records[i][2]) > config.TEXT_WIDTH:
                self.detail_sub_lab.setText(
                    self.del_records[i][2][:config.TEXT_WIDTH - 3] + '...')
            else:
                self.detail_sub_lab.setText(self.del_records[i][2])
            self.verticalLayout.addWidget(self.detail_sub_lab)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.restore_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.restore_btn.setObjectName("restore_btn")
        self.horizontalLayout.addWidget(self.restore_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.restore_btn.clicked.connect(self.reset)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "回收站"))
        self.restore_btn.setText(_translate("Dialog", "还原"))

    def reset(self):
        self.set_data(self.parent.user_info['username'])
        self.setupUi()
        self.show()

    def restore_records(self):

        pass

    def set_list(self):
        print(self.sender().objectName())
        try:
            id = int(re.findall('\d+',self.sender().objectName())[0])
        except Exception as e:
            print(e)
        if self.sender().isChecked():
            self.item_set.add(id)
        else:
            self.item_set.remove(id)
        print(self.item_set)

    def closeEvent(self, QCloseEvent):
        self.updateSignal.emit(self.parent.user_info['username'])
        self.item_set.clear()