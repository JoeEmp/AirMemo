# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/sync.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from comm.operateSqlite import sqlite_db
import config
from module.note import get_cloud_notes, get_notes


class Ui_Sync_Dialog(QtWidgets.QDialog):
    updateSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.user_info = parent.user_info
        self.set_data(
            username=self.user_info['username'], token=self.user_info['token'])
        self.setupUi()
        self.updateSignal.connect(parent.get_update_Signal)
        self.show()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(258, 402)

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 241, 391))
        self.tabWidget.setObjectName("tabWidget")
        # 云端tab
        self.cloud_tab = QtWidgets.QWidget()
        self.cloud_tab.setObjectName("cloud_tab")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.cloud_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.cloud_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.cloud_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cloud_gridLayout.setObjectName("cloud_gridLayout")

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        # 云端tab的提示语
        self.cloud_lab = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.cloud_lab.setStyleSheet("color:rgb(0, 68, 221)")
        self.cloud_lab.setObjectName("cloud_lab")
        self.cloud_gridLayout.addWidget(self.cloud_lab, 2, 0, 1, 3)
        # 云端tab的列表
        self.cloud_list = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.cloud_list.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection)
        self.cloud_list.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.cloud_list.setObjectName("cloud_list")

        brush = QtGui.QBrush(QtGui.QColor(0, 68, 221))
        brush.setStyle(QtCore.Qt.NoBrush)
        local_ids = [r['cloud_id'] for r in self.local_records]
        for cloud_record in self.cloud_records:
            item = QtWidgets.QListWidgetItem()
            item.setText(cloud_record['msg'])
            if cloud_record['cloud_id'] in local_ids:
                item.setForeground(brush)
            self.cloud_list.addItem(item)

        # 云端tab的删除按钮
        self.cloud_gridLayout.addWidget(self.cloud_list, 1, 0, 1, 4)
        self.cloud_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_del_btn.setObjectName("cloud_del_btn")
        self.cloud_gridLayout.addWidget(self.cloud_del_btn, 3, 2, 1, 1)
        # 云端tab的同步按钮
        self.cloud_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cloud_sync_btn.setObjectName("cloud_sync_btn")
        self.cloud_gridLayout.addWidget(self.cloud_sync_btn, 3, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cloud_gridLayout.addItem(spacerItem1, 3, 3, 1, 1)

        self.tabWidget.addTab(self.cloud_tab, "")

        # 本地页面
        self.local_tab = QtWidgets.QWidget()
        self.local_tab.setObjectName("local_tab")

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.local_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.local_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.local_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.local_gridLayout.setObjectName("local_gridLayout")

        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        # 本地tab的提示语
        self.local_lab = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.local_lab.setStyleSheet("color:rgb(0, 204, 34)")
        self.local_lab.setObjectName("local_lab")
        self.local_gridLayout.addWidget(self.local_lab, 2, 0, 1, 3)
        # 本地tab的列表
        self.local_list = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.local_list.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection)
        self.local_list.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.local_list.setObjectName("local_list")

        # record插入
        brush = QtGui.QBrush(QtGui.QColor(0, 204, 34))
        brush.setStyle(QtCore.Qt.NoBrush)
        cloud_ids = [r['cloud_id'] for r in self.cloud_records]
        for local_record in self.local_records:
            item = QtWidgets.QListWidgetItem()
            item.setText(local_record['message'])
            if 1 == local_record['is_del']:
                item.setText(item.text() + '(已删除)')
            if local_record['cloud_id'] in cloud_ids:
                item.setForeground(brush)
            self.local_list.addItem(item)

        self.local_gridLayout.addWidget(self.local_list, 1, 0, 1, 4)
        # 本地tab的删除按钮
        self.local_del_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.local_del_btn.setObjectName("local_del_btn")
        self.local_gridLayout.addWidget(self.local_del_btn, 3, 2, 1, 1)
        # 本地tab的同步按钮
        self.local_sync_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.local_sync_btn.setObjectName("local_sync_btn")
        self.local_gridLayout.addWidget(self.local_sync_btn, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.local_gridLayout.addItem(spacerItem3, 3, 3, 1, 1)

        self.tabWidget.addTab(self.local_tab, "")

        # 绑定槽
        self.local_del_btn.clicked.connect(self.del_local_record)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "云"))
        self.cloud_lab.setText(_translate("Dialog", "蓝色为云端有更新的版本"))
        __sortingEnabled = self.cloud_list.isSortingEnabled()
        self.cloud_list.setSortingEnabled(False)
        self.cloud_list.setSortingEnabled(__sortingEnabled)
        self.cloud_del_btn.setText(_translate("Dialog", "删除"))
        self.cloud_sync_btn.setText(_translate("Dialog", "同步"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.cloud_tab), _translate("Dialog", "云端"))
        self.local_lab.setText(_translate("Dialog", "绿色为已在云端，但未必一致"))
        __sortingEnabled = self.local_list.isSortingEnabled()
        self.local_list.setSortingEnabled(False)
        self.local_list.setSortingEnabled(__sortingEnabled)
        self.local_del_btn.setText(_translate("Dialog", "删除"))
        self.local_sync_btn.setText(_translate("Dialog", "备份"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.local_tab), _translate("Dialog", "本地"))

    def set_data(self, username='visitor', token=None):
        self.local_records = get_notes(username, is_del='all')
        try:
            self.cloud_records = get_cloud_notes(username, token)['list']
            print(self.cloud_records)
        except Exception as e:
            QMessageBox.information(self.parent, 'tip', "{}".format(
                server_error_msg(-1)['msg']), QMessageBox.Ok)

    # 备份按钮槽函数
    def sync_upload_slot(self):
        self.local_list.selectedIndexes()
        pass

    # 同步按钮槽函数
    def sync_download_slot(self, type=1):
        pass

    def del_local_record(self):
        ids = self.local_list.selectedIndexes()
        for id in ids:
            sql = "delete from msg where username = '%s' and id = %d" % (
                self.user_info['username'], self.local_records[id.row()]['id'])
            sqlite_db.transaction(sql)
            self.local_list.takeItem(id.row())

# if __name__ == "__main__":
#     cloud_records = get_cloud_records('coco')
#     for cloud in cloud_records:
#         print()
