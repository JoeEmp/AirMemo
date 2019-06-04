# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui\recycle.ui'
#
# Created by: PyQt5 ui code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import logging
import re
import sip

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
import config
import operateSqlite
import utils


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
        self.del_records = utils.get_records(config.LDB_FILENAME, username, is_del='1')
        self.records_len = len(self.del_records)

    def setupUi(self):
        self.setObjectName("recycle_Dialog")
        self.resize(config.COM_TE_WIDTH,
                    config.COM_BTN_HEIGHT * self.records_len * 2 + 50)
        # self.setFixedSize(config.TEXT_WIDTH,
        #             config.BTN_HEIGHT * len(self.del_records) * 2 + 50)
        # 窗口总布局
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setGeometry(
        #         QtCore.QRect(0, 0, config.TEXT_WIDTH + 20,
        #                      config.BTN_HEIGHT * len(
        #                              self.del_records) * 2 + 30) + 20)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(
                QtCore.QRect(10, 10, config.COM_TE_WIDTH,
                             config.COM_BTN_HEIGHT * self.records_len * 2 + 30))
        # 打印 布局高度
        logging.warning(self.verticalLayoutWidget.height())

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.setObjectName("verticalLayout")
        for i in range(len(self.del_records)):
            self.message_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
            self.message_check.setObjectName(
                    "message_check" + str(self.del_records[i]['id']))
            # 设置 msg
            self.message_check.setText(self.del_records[i]['message'])
            self.message_check.setChecked(False)
            self.message_check.clicked.connect(self.set_list)
            self.verticalLayout.addWidget(self.message_check)

            self.detail_sub_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.detail_sub_lab.setObjectName(
                    "detail_sub_lab" + str(self.del_records[i]['id']))
            # 设置 detail
            if not self.del_records[i]['detail']:
                self.detail_sub_lab.setText('无详细信息')
            elif len(self.del_records[i]['detail']) > config.COM_TE_WIDTH:
                self.detail_sub_lab.setText(
                        self.del_records[i]['detail'][:config.COM_TE_WIDTH - 3] + '...')
            else:
                self.detail_sub_lab.setText(self.del_records[i]['detail'])
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

    def restore_records(self):
        self.restore_btn.clicked.connect(self.restore_records)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "回收站"))
        self.restore_btn.setText(_translate("Dialog", "还原"))

    def reset(self):
        self.verticalLayout.removeWidget(self.detail_sub_lab)
        sip.delete(self.detail_sub_lab)
        self.repaint()
        self.set_data(self.parent.user_info['username'])
        self.setupUi()
        self.show()
        table = 'Msg'
        value_dict = {'is_del': '0'}
        for i in self.item_set:
            filter_list = [
                ['id', '=', str(i)]
            ]
            sql = operateSqlite.be_sql().update_sql(table=table,
                                                    value_dict=value_dict,
                                                    filter_list=filter_list)
            operateSqlite.exec_sql(config.LDB_FILENAME, sql)
        self.reset()
        self.item_set.clear()

    def set_list(self):
        # print(self.sender().objectName())
        try:
            id = int(re.findall('\d+', self.sender().objectName())[0])
        except Exception as e:
            logging.info(e)
        if self.sender().isChecked():
            self.item_set.add(id)
        else:
            self.item_set.remove(id)
            # print(self.item_set)

    def closeEvent(self, QCloseEvent):
        self.updateSignal.emit(self.parent.user_info['username'])
        self.item_set.clear()
