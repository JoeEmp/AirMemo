<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sync.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from operateSqlite import exec_sql
import config
from module import get_cloud_notes, get_notes, server_error_msg


class Ui_Sync_Dialog(QtWidgets.QDialog):
    updateSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.user_info = parent.user_info
        self.set_data(username=self.user_info['username'])
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(252, 403)

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 234, 381))

        self.tabWidget.setObjectName("tabWidget")
        self.cloud_tab = QtWidgets.QWidget()
        self.cloud_tab.setObjectName("cloud_tab")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.cloud_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 231, 331))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.cloud_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.cloud_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cloud_gridLayout.setObjectName("cloud_gridLayout")

        # 云tab删除按钮
        self.cloud_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_del_btn.setObjectName("cloud_del_btn")
        self.cloud_gridLayout.addWidget(self.cloud_del_btn, 3, 2, 1, 1)

        # 云tab同步按钮
        self.cloud_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_sync_btn.setObjectName("cloud_sync_btn")
        self.cloud_gridLayout.addWidget(self.cloud_sync_btn, 3, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem1, 3, 0, 1, 1)

        # 云tab list
        self.cloud_list = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.cloud_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.cloud_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cloud_list.setObjectName("cloud_list")

        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.cloud_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cloud_list.addItem(item)
        self.cloud_gridLayout.addWidget(self.cloud_list, 1, 0, 1, 4)

        # 云tab 提示语
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setStyleSheet("color:rgb(85, 85, 255)")
        self.label_2.setObjectName("label_2")
        self.cloud_gridLayout.addWidget(self.label_2, 2, 0, 1, 3)

        # 本地tab
        self.tabWidget.addTab(self.cloud_tab, "")
        self.local_tab = QtWidgets.QWidget()
        self.local_tab.setObjectName("local_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.local_tab)

        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 231, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.local_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.local_gridLayout.setContentsMargins(1, 1, 2, 0)
        self.local_gridLayout.setObjectName("local_gridLayout")

        self.local_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.local_del_btn.setObjectName("local_del_btn")
        self.local_gridLayout.addWidget(self.local_del_btn, 3, 2, 1, 1)

        self.local_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.local_sync_btn.setObjectName("local_sync_btn")
        self.local_gridLayout.addWidget(self.local_sync_btn, 3, 1, 1, 1)

        # 空间
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem2, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem3, 3, 0, 1, 1)

        # 本地tab list
        self.local_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.local_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.local_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.local_list.setObjectName("local_list")

        # msg item
        item = QtWidgets.QListWidgetItem()
        self.local_list.addItem(item)
        self.local_gridLayout.addWidget(self.local_list, 1, 0, 1, 4)
        # 本地提示语
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color:rgb(0, 255, 0)")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.local_gridLayout.addWidget(self.label, 2, 1, 1, 3)
        self.tabWidget.addTab(self.local_tab, "")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "云"))
        self.cloud_del_btn.setText(_translate("Dialog", "删除"))
        self.cloud_sync_btn.setText(_translate("Dialog", "同步"))
        __sortingEnabled = self.cloud_list.isSortingEnabled()
        self.cloud_list.setSortingEnabled(False)
        item = self.cloud_list.item(0)
        item.setText(_translate("Dialog", "cloud have new"))
        item = self.cloud_list.item(1)
        item.setText(_translate("Dialog", "与本地一致"))
        self.cloud_list.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog", "蓝色为云端有更新的版本"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cloud_tab), _translate("Dialog", "云端"))
        self.local_del_btn.setText(_translate("Dialog", "删除"))
        self.local_sync_btn.setText(_translate("Dialog", "备份"))
        __sortingEnabled = self.local_list.isSortingEnabled()
        self.local_list.setSortingEnabled(False)
        item = self.local_list.item(0)
        item.setText(_translate("Dialog", "1"))
        self.local_list.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "绿色为云端已有消息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.local_tab), _translate("Dialog", "本地"))

    def set_data(self, username='visitor'):
        self.local_records = get_notes(config.LDB_FILENAME, username, is_del='all')
        try:
            self.cloud_records = get_cloud_notes(username, self.user_info['token'])
        except Exception as e:
            QMessageBox.information(self.parent, 'tip', "{}".format(server_error_msg()['errMsg']), QMessageBox.Ok)

    # 备份按钮槽函数
    def sync_upload_slot(self):
        self.local_list.selectedIndexes()
        pass

    # 同步按钮槽函数
    def sync_download_slot(self, type=1):
        pass

    def del_local_record(self):
        pass

# if __name__ == "__main__":
#     cloud_records = get_cloud_records('coco')
#     for cloud in cloud_records:
#         print()
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/sync.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(258, 402)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 241, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.cloud_tab = QtWidgets.QWidget()
        self.cloud_tab.setObjectName("cloud_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.cloud_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.cloud_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.cloud_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cloud_gridLayout.setObjectName("cloud_gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setStyleSheet("color:rgb(0, 68, 221)")
        self.label_2.setObjectName("label_2")
        self.cloud_gridLayout.addWidget(self.label_2, 2, 0, 1, 3)
        self.cloud_list = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.cloud_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.cloud_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cloud_list.setObjectName("cloud_list")
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 68, 221))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.cloud_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cloud_list.addItem(item)
        self.cloud_gridLayout.addWidget(self.cloud_list, 1, 0, 1, 4)
        self.cloud_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_del_btn.setObjectName("cloud_del_btn")
        self.cloud_gridLayout.addWidget(self.cloud_del_btn, 3, 2, 1, 1)
        self.cloud_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_sync_btn.setObjectName("cloud_sync_btn")
        self.cloud_gridLayout.addWidget(self.cloud_sync_btn, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        self.tabWidget.addTab(self.cloud_tab, "")
        self.local_tab = QtWidgets.QWidget()
        self.local_tab.setObjectName("local_tab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.local_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.local_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.local_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.local_gridLayout.setObjectName("local_gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.local_lab = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.local_lab.setStyleSheet("color:rgb(0, 204, 34)")
        self.local_lab.setObjectName("local_lab")
        self.local_gridLayout.addWidget(self.local_lab, 2, 0, 1, 3)
        self.local_list = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.local_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.local_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.local_list.setObjectName("local_list")
        item = QtWidgets.QListWidgetItem()
        self.local_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 204, 34))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.local_list.addItem(item)
        self.local_gridLayout.addWidget(self.local_list, 1, 0, 1, 4)
        self.local_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.local_del_btn.setObjectName("local_del_btn")
        self.local_gridLayout.addWidget(self.local_del_btn, 3, 2, 1, 1)
        self.local_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.local_sync_btn.setObjectName("local_sync_btn")
        self.local_gridLayout.addWidget(self.local_sync_btn, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        self.tabWidget.addTab(self.local_tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "云"))
        self.label_2.setText(_translate("Dialog", "蓝色为云端有更新的版本"))
        __sortingEnabled = self.cloud_list.isSortingEnabled()
        self.cloud_list.setSortingEnabled(False)
        item = self.cloud_list.item(0)
        item.setText(_translate("Dialog", "cloud have new"))
        item = self.cloud_list.item(1)
        item.setText(_translate("Dialog", "与本地一致"))
        self.cloud_list.setSortingEnabled(__sortingEnabled)
        self.cloud_del_btn.setText(_translate("Dialog", "删除"))
        self.cloud_sync_btn.setText(_translate("Dialog", "同步"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cloud_tab), _translate("Dialog", "云端"))
        self.local_lab.setText(_translate("Dialog", "绿色为已在云端"))
        __sortingEnabled = self.local_list.isSortingEnabled()
        self.local_list.setSortingEnabled(False)
        item = self.local_list.item(0)
        item.setText(_translate("Dialog", "123"))
        item = self.local_list.item(1)
        item.setText(_translate("Dialog", "sss已删除"))
        self.local_list.setSortingEnabled(__sortingEnabled)
        self.local_del_btn.setText(_translate("Dialog", "删除"))
        self.local_sync_btn.setText(_translate("Dialog", "备份"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.local_tab), _translate("Dialog", "本地"))


>>>>>>> joe
