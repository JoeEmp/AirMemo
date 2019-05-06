# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sync.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

import config
import utils


class Ui_Sync_Dialog(QtWidgets.QDialog):
    updateSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.set_data(parent.user_info['username'])
        self.parent = parent
        self.user_info = parent.user_info
        self.setupUi()
        self.show()

    def set_data(self, username):
        self.local_records = utils.get_records(config.LDB_FILENAME, username, is_del='all')
        self.records_len = len(self.local_records)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(252, 403)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 231, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.cloud_tab = QtWidgets.QWidget()
        self.cloud_tab.setObjectName("cloud_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.cloud_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 231, 331))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.cloud_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.cloud_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cloud_gridLayout.setObjectName("cloud_gridLayout")
        self.cloud_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_del_btn.setObjectName("cloud_del_btn")
        self.cloud_gridLayout.addWidget(self.cloud_del_btn, 3, 2, 1, 1)
        self.cloud_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_sync_btn.setObjectName("cloud_sync_btn")
        self.cloud_gridLayout.addWidget(self.cloud_sync_btn, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.cloud_list = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.cloud_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.cloud_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cloud_list.setObjectName("cloud_list")
        item = QtWidgets.QListWidgetItem()
        self.cloud_list.addItem(item)
        self.cloud_gridLayout.addWidget(self.cloud_list, 1, 0, 1, 4)

        self.tabWidget.addTab(self.cloud_tab, "")
        self.local_tab = QtWidgets.QWidget()
        self.local_tab.setObjectName("local_tab")

        self.gridLayoutWidget = QtWidgets.QWidget(self.local_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 231, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.local_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.local_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.local_gridLayout.setObjectName("local_gridLayout")

        self.local_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.local_del_btn.setObjectName("local_del_btn")
        self.local_gridLayout.addWidget(self.local_del_btn, 3, 2, 1, 1)

        # 备份信息
        self.local_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.local_sync_btn.setObjectName("local_sync_btn")
        self.local_sync_btn.clicked.connect(self.local_sync_slot)
        self.local_gridLayout.addWidget(self.local_sync_btn, 3, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem2, 3, 3, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem3, 3, 0, 1, 1)

        self.local_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.local_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.local_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.local_list.setObjectName("local_list")

        for local in self.local_records:
            item = QtWidgets.QListWidgetItem(local[2])
            if local[6] == 1:
                item.setText(local[2] + '(已删除)')
            if local[5]:
                brush = QtGui.QBrush(QtGui.QColor(1, 203, 31))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
            self.local_list.addItem(item)
        self.local_gridLayout.addWidget(self.local_list, 1, 0, 1, 4)

        self.local_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.local_lab.setObjectName("label")
        self.local_lab.setText('绿色为云端已有消息')
        self.local_lab.setStyleSheet('color:rgb(1,203,31)')
        # self.local_lab.setAlignment(
            # QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.local_gridLayout.addWidget(self.local_lab, 2, 0, 1, 2)

        self.tabWidget.addTab(self.local_tab, "")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "云"))
        self.cloud_del_btn.setText(_translate("Dialog", "删除"))
        self.cloud_sync_btn.setText(_translate("Dialog", "同步"))
        __sortingEnabled = self.cloud_list.isSortingEnabled()
        self.cloud_list.setSortingEnabled(False)
        item = self.cloud_list.item(0)
        item.setText(_translate("Dialog", "2"))
        self.cloud_list.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cloud_tab),
                                  _translate("Dialog", "云端"))
        self.local_del_btn.setText(_translate("Dialog", "删除"))
        self.local_sync_btn.setText(_translate("Dialog", "备份"))
        __sortingEnabled = self.local_list.isSortingEnabled()
        self.local_list.setSortingEnabled(False)
        self.local_list.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.local_tab),
                                  _translate("Dialog", "本地"))

    def local_sync_slot(self):
        if self.local_list.selectedIndexes():
            # 请求
            # 对新数据接口newkey,newkey写入到记录里
            pass
        else:
            QMessageBox.information(self, ' ', '请选择需要上传的消息', QMessageBox.Ok)
