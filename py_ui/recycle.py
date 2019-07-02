# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui\recycle.ui'
#
# Created by: PyQt5 ui code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import logging
import re
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox

import config
import operateSqlite
import module


class Ui_recycle_Dialog(QtWidgets.QDialog):
    updateSignal = pyqtSignal(str)
    item_set = set()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.set_data(parent.user_info['username'])
        self.parent = parent
        self.setupUi()
        self.show()

    def set_data(self, username):
        '''
        根据用户名，获取已删除note
        :param username:
        :return:
        '''
        self.del_records = module.get_notes(config.LDB_FILENAME, username, is_del='1')
        self.records_len = len(self.del_records)

    def setupUi(self):
        self.setObjectName("recycle_Dialog")
        self.resize(300, 370)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 280, 350))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        for i in range(self.records_len):
            item = QListWidgetItem()
            item.setSizeHint(QSize(10, 40))
            self.listWidget.addItem(item)

            # 设置item布局
            itemWidget = QtWidgets.QWidget(self)
            itemWidget.setGeometry(QtCore.QRect(40, 190, 231, 51))
            item_verticalLayout = QtWidgets.QVBoxLayout(itemWidget)
            item_verticalLayout.setContentsMargins(0, 0, 0, 0)
            message_check = QtWidgets.QCheckBox(itemWidget)
            message_check.setText(self.del_records[i]['message'])
            item_verticalLayout.addWidget(message_check)
            message_check.setObjectName('message_check%s' % i)
            message_check.clicked.connect(self.set_list)
            detail_sub_lab = QtWidgets.QLabel(itemWidget)
            if self.del_records[i]['detail']:
                if len(self.del_records[i]['detail']) > 22:
                    detail_sub_lab.setText(self.del_records[i]['detail'][:20] + "……")
                else:
                    detail_sub_lab.setText(self.del_records[i]['detail'])
            else:
                detail_sub_lab.setText('无具体任务细节')
            item_verticalLayout.addWidget(detail_sub_lab)

            self.listWidget.setItemWidget(item, itemWidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.restore_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.restore_btn.setObjectName("restore_btn")
        self.restore_btn.clicked.connect(self.restore_records)
        self.horizontalLayout.addWidget(self.restore_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "回收站"))
        self.restore_btn.setText(_translate("Dialog", "还原"))

    def restore_records(self):
        '''
        根据item_set还原note,重置数据
        :return:
        '''
        if not self.listWidget.selectedItems():
            QMessageBox.information(self, 'tips', '请选择回收任务', QMessageBox.Ok)
        else:
            # print(self.item_set)
            for i in self.item_set:
                filter_list = [
                    ['id', '=', str(self.del_records[i]['id'])]
                ]
                module.restore_note(config.LDB_FILENAME, filter_list)
                self.listWidget.takeItem(i)
        self.reset()

    def reset(self):
        '''
        重设全部变量
        :return:
        '''
        self.set_data(self.parent.user_info['username'])
        self.item_set.clear()

    def set_list(self):
        '''
        添加选中项到 item_set
        :return:
        '''
        # print(self.sender().objectName())
        try:
            id = int(re.findall('\d+', self.sender().objectName())[0])
        except Exception as e:
            logging.info(e)
        if self.sender().isChecked():
            self.item_set.add(id)
            self.listWidget.setCurrentRow(id)
        else:
            self.item_set.remove(id)

    def closeEvent(self, QCloseEvent):
        self.updateSignal.emit(self.parent.user_info['username'])
        self.item_set.clear()
