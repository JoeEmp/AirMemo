from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QMessageBox, QRadioButton, QWidget
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.Qt import QPushButton
from module.email_conf import add_email_conf, del_email_conf, update_email_conf, get_email_conf, get_user_email_conf, set_is_default_email_conf
from py_ui.toast import Toast
from comm.user_cache import mine
import logging


class Email_Tab_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_data()
        self.setupUi()

    def set_data(self):
        self.user_info = mine['user_info']
        self._email_records = get_user_email_conf(
            self.user_info['username'])['records']

    def setupUi(self):
        self.setObjectName("time_tab")
        # 提醒列表
        self.time_list = QListWidget(self)
        self.time_list.setGeometry(QtCore.QRect(10, 10, 231, 271))
        for record in self._reminder_records:
            item = QListWidgetItem(record['time'])
            item.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.time_list.addItem(item)
        self.time_list.setObjectName("time_list")

        self.creater_reminder_btn = QPushButton(self)
        self.creater_reminder_btn.setGeometry(QtCore.QRect(250, 10, 75, 23))
        self.creater_reminder_btn.clicked.connect(self._add_reminder_slot)
        self.creater_reminder_btn.setObjectName("creater_reminder_btn")

        self.del_reminder_btn = QPushButton(self)
        self.del_reminder_btn.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.del_reminder_btn.clicked.connect(self._del_reminder_slot)
        self.del_reminder_btn.setObjectName("del_reminder_btn")

        self.up_btn =QPushButton(self)
        self.up_btn.setGeometry(QtCore.QRect(250, 90, 75, 23))
        self.up_btn.clicked.connect(self.up_reminder)
        self.up_btn.setObjectName("up_btn")

        self.down_btn = QPushButton(self)
        self.down_btn.setGeometry(QtCore.QRect(250, 130, 71, 21))
        self.down_btn.clicked.connect(self.down_reminder)
        self.down_btn.setObjectName("down_btn")

        self.save_reminder_btn = QPushButton(self)
        self.save_reminder_btn.setGeometry(QtCore.QRect(250, 170, 75, 23))
        self.save_reminder_btn.clicked.connect(self._save_reminder_sequence)
        self.save_reminder_btn.setObjectName("save_reminder_btn")

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 210, 141, 31))
        self.label.setObjectName("label")

        self.tabWidget.addTab(self, "")


    # 提醒时间页的槽函数
    def _add_reminder_slot(self):
        '''

        :return:
        '''
        item = QListWidgetItem('00:00:00')
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.time_list.addItem(item)
        table = 'Reminder'
        value_dict = {'time': '00:00:00',
                      'username': self.user_info['username']}
        sql = be_sql().ins_sql(table, value_dict)
        exec_sql(sql)
        self.set_data()

    def _del_reminder_slot(self):
        index = self.time_list.currentRow()
        if index != -1:
            ret = QMessageBox.question(
                self, ' ', '是否删除此提醒时间', QMessageBox.Yes, QMessageBox.Cancel)
            try:
                if ret == QMessageBox.Yes:
                    self.time_list.takeItem(index)
                    self.clear_email_form()
                    table = 'reminder'
                    filter_list = [
                        ['id', '=', str(self._reminder_records[index]['id'])]
                    ]
                    sql = be_sql().del_sql(table, filter_list=filter_list)
                    exec_sql(sql)
                elif ret == QMessageBox.Cancel:
                    pass
            except Exception as e:
                print(e)
        else:
            ret = QMessageBox.information(self, 'tips', '没有选择删除项')

    def up_reminder(self):
        cur_row = self.time_list.currentRow()
        if cur_row > 0:
            # UI 调整
            per_item = self.time_list.item(cur_row - 1)
            cur_item = self.time_list.item(cur_row)
            # 这个操作考虑性能没有必要使用range
            self.time_list.takeItem(cur_row - 1)
            self.time_list.takeItem(cur_row - 1)

            self.time_list.insertItem(cur_row - 1, cur_item)
            self.time_list.insertItem(cur_row, per_item)

            # records调整
            per_record = self._reminder_records.pop(cur_row - 1)
            cur_record = self._reminder_records.pop(cur_row - 1)
            self._reminder_records.insert(cur_row - 1, cur_record)
            self._reminder_records.insert(cur_row, per_record)

            self.time_list.setCurrentRow(cur_row - 1)

        elif cur_row == 0:
            pass
        else:
            QMessageBox.information(self, ' ', '没有选中时间项')

    def down_reminder(self):
        cur_row = self.time_list.currentRow()
        if cur_row < self.time_list.count():
            # UI 调整
            last_item = self.time_list.item(cur_row + 1)
            cur_item = self.time_list.item(cur_row)
            for i in range(2):
                self.time_list.takeItem(cur_row)
            self.time_list.insertItem(cur_row, cur_item)
            self.time_list.insertItem(cur_row, last_item)
            self.time_list.setCurrentRow(cur_row + 1)

            # record调整
            cur_record = self._reminder_records.pop(cur_row)
            last_record = self._reminder_records.pop(cur_row)
            self._reminder_records.insert(cur_row, last_record)
            self._reminder_records.insert(cur_row + 1, cur_record)

        elif cur_row == self.time_list.count():
            pass
        else:
            QMessageBox.information(self, ' ', '没有选中时间项')

    def _save_reminder_sequence(self):
        table = 'reminder'
        value_dict = {'sequence': -1, 'time': '00:00:00'}
        filter_list = [
            ['username', '=', self.user_info['username']],
            ['id', '=', -1],
            ['time', '=', -1]
        ]
        ids = [record['id'] for record in self._reminder_records]
        times = [record['time'] for record in self._reminder_records]
        for i in range(len(ids)):
            value_dict['sequence'] = str(i)
            value_dict['time'] = self.time_list.item(i).text()
            filter_list[1][2] = str(ids[i])
            filter_list[2][2] = times[i]
            sql = be_sql().update_sql(table, value_dict, filter_list)
            exec_sql(sql)
        pass

