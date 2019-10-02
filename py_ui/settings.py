# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox
from comm.operateSqlite import *
from comm.user_cache import mine


class Ui_Settings(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        logging.info('init begin')
        self.parent = parent        # 冗余
        self.user_info = mine.get_value('user_info')
        self.set_data()
        self.setupUi()

    def set_data(self):
        '''
        初始化数据 获取 email_settings 和 reminder 表的数据
        :return:
        '''
        # 获取email_settings表数据
        table = 'email_settings'
        filter_list = [
            ['username', '=', self.user_info['username']]
        ]
        sql = be_sql().sel_sql(table=table, filter_list=filter_list)
        self._email_records = exec_sql(sql)
        # 获取Reminder表数据
        sql = sql.replace(table, 'Reminder') + 'order by sequence'
        self._reminder_records = exec_sql(sql)
        # print(self._reminder_records)
        logging.info('data init end')

    def setupUi(self):
        self.setObjectName("Settings")
        self.resize(493, 333)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 471, 311))
        self.tabWidget.setObjectName("tabWidget")

        self.email_tab = QtWidgets.QWidget()
        self.email_tab.setObjectName("email_tab")

        self.gridLayoutWidget = QtWidgets.QWidget(self.email_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # 邮箱设置页保存按钮
        self.save_email_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_email_btn.setObjectName("save_email_btn")
        self.save_email_btn.clicked.connect(self._save_email_config)
        self.gridLayout.addWidget(self.save_email_btn, 5, 6, 1, 1)

        # 邮箱设置页删除按钮
        self.del_email_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.del_email_btn.setObjectName("del_email_btn")
        self.del_email_btn.clicked.connect(self._del_item_slot)
        self.gridLayout.addWidget(self.del_email_btn, 5, 3, 1, 1)

        # 邮箱设置页 邮箱编辑框
        self.email_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_le.setObjectName("email_le")
        self.gridLayout.addWidget(self.email_le, 1, 5, 1, 2)

        # 邮箱设置页添加按钮
        self.add_email_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_email_btn.setObjectName("add_email_btn")
        self.add_email_btn.clicked.connect(self._add_email_item_slot)
        self.gridLayout.addWidget(self.add_email_btn, 5, 1, 1, 1)

        # 邮箱设置页 ssl 单选按钮
        self.ssl_rbtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.ssl_rbtn.setText("")
        self.ssl_rbtn.setObjectName("ssl_rbtn")
        self.ssl_rbtn.clicked.connect(self.chcek_radio_slot)
        self.gridLayout.addWidget(self.ssl_rbtn, 3, 5, 1, 1)

        # 发信名称标签
        self.sender_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sender_lab.setObjectName("sender_lab")
        self.gridLayout.addWidget(self.sender_lab, 4, 4, 1, 1)

        # 密码标签
        self.password_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_lab.setObjectName("password_lab")
        self.gridLayout.addWidget(self.password_lab, 2, 4, 1, 1)

        # ssl 标签
        self.ssl_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ssl_lab.setObjectName("ssl_lab")
        self.gridLayout.addWidget(self.ssl_lab, 3, 4, 1, 1)

        # 邮箱标签
        self.email_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.email_lab.setObjectName("email_lab")
        self.gridLayout.addWidget(self.email_lab, 1, 4, 1, 1)

        # 编辑框
        self.password_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.password_le, 2, 5, 1, 2)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)

        # 发信名称编辑框
        self.sender_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sender_le.setObjectName("sender_le")
        self.gridLayout.addWidget(self.sender_le, 4, 5, 1, 2)

        # ssl编辑框
        self.ssl_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ssl_le.setObjectName("ssl_le")
        self.gridLayout.addWidget(self.ssl_le, 3, 6, 1, 1)

        # 默认使用按钮
        self.default_email_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.default_email_btn.setObjectName("default_email_btn")
        self.default_email_btn.clicked.connect(self._selectDefualt)
        self.gridLayout.addWidget(self.default_email_btn, 5, 0, 1, 1)

        # 邮箱列表
        self.email_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.email_list.setObjectName("email_list")
        for record in self._email_records:
            item = QListWidgetItem(record['addr'])
            if record['is_default'] == 1:
                brush = QtGui.QBrush(QtGui.QColor(1, 203, 31))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
            # item.setFlags(
            #         QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.email_list.addItem(item)
        # self.email_list.setStyleSheet('background-color:#c4ffff')
        self.email_list.itemClicked.connect(self._set_config_slot)
        self.gridLayout.addWidget(self.email_list, 1, 0, 4, 4)

        # 提示标签
        self.tips_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.tips_lab.setMaximumSize(QtCore.QSize(130, 15))
        self.tips_lab.setObjectName("tips_lab")
        self.gridLayout.addWidget(self.tips_lab, 0, 0, 1, 1)

        # 提醒时间标签页
        self.tabWidget.addTab(self.email_tab, "")
        self.time_tab = QtWidgets.QWidget()
        self.time_tab.setObjectName("time_tab")

        # 提醒列表
        self.time_list = QtWidgets.QListWidget(self.time_tab)
        self.time_list.setGeometry(QtCore.QRect(10, 10, 231, 271))
        for record in self._reminder_records:
            item = QListWidgetItem(record['time'])
            item.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.time_list.addItem(item)
        self.time_list.setObjectName("time_list")

        self.creater_reminder_btn = QtWidgets.QPushButton(self.time_tab)
        self.creater_reminder_btn.setGeometry(QtCore.QRect(250, 10, 75, 23))
        self.creater_reminder_btn.clicked.connect(self._add_reminder_slot)
        self.creater_reminder_btn.setObjectName("creater_reminder_btn")

        self.del_reminder_btn = QtWidgets.QPushButton(self.time_tab)
        self.del_reminder_btn.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.del_reminder_btn.clicked.connect(self._del_reminder_slot)
        self.del_reminder_btn.setObjectName("del_reminder_btn")

        self.up_btn = QtWidgets.QPushButton(self.time_tab)
        self.up_btn.setGeometry(QtCore.QRect(250, 90, 75, 23))
        self.up_btn.clicked.connect(self.up_reminder)
        self.up_btn.setObjectName("up_btn")

        self.down_btn = QtWidgets.QPushButton(self.time_tab)
        self.down_btn.setGeometry(QtCore.QRect(250, 130, 71, 21))
        self.down_btn.clicked.connect(self.down_reminder)
        self.down_btn.setObjectName("down_btn")

        self.save_reminder_btn = QtWidgets.QPushButton(self.time_tab)
        self.save_reminder_btn.setGeometry(QtCore.QRect(250, 170, 75, 23))
        self.save_reminder_btn.clicked.connect(self._save_reminder_sequence)
        self.save_reminder_btn.setObjectName("save_reminder_btn")

        self.label = QtWidgets.QLabel(self.time_tab)
        self.label.setGeometry(QtCore.QRect(250, 210, 141, 31))
        self.label.setObjectName("label")

        self.tabWidget.addTab(self.time_tab, "")
        # 优先级选择颜色框
        self.color_tab = QtWidgets.QWidget()
        self.color_tab.setObjectName("color_tab")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.color_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 361, 281))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.color_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.color_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.color_gridLayout.setObjectName("color_gridLayout")
        # green 颜色条
        self.green_Slider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.green_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_Slider.setObjectName("green_Slider")
        self.color_gridLayout.addWidget(self.green_Slider, 2, 2, 1, 1)
        # red 颜色条
        self.red_Slider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.red_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_Slider.setObjectName("red_Slider")
        self.color_gridLayout.addWidget(self.red_Slider, 1, 2, 1, 1)
        # bule 颜色条
        self.bule_Slider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.bule_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.bule_Slider.setObjectName("bule_Slider")
        self.color_gridLayout.addWidget(self.bule_Slider, 3, 2, 1, 1)
        # 优先级设置框
        self.priority_listWidget = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.priority_listWidget.setMinimumSize(QtCore.QSize(0, 180))
        self.priority_listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.priority_listWidget.setObjectName("priority_listWidget")
        self.color_gridLayout.addWidget(self.priority_listWidget, 1, 0, 3, 2)

        # rgb标签
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.color_gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        # rgb输入框
        self.rgb_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.rgb_le.setObjectName("rgb_le")
        self.color_gridLayout.addWidget(self.rgb_le, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.color_gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        # r值输入框
        self.red_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.red_le.setMaximumSize(QtCore.QSize(50, 16777215))
        self.red_le.setObjectName("red_le")
        self.color_gridLayout.addWidget(self.red_le, 1, 3, 1, 1)
        # g值输入框
        self.green_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.green_le.setMaximumSize(QtCore.QSize(50, 16777215))
        self.green_le.setObjectName("green_le")
        self.color_gridLayout.addWidget(self.green_le, 2, 3, 1, 1)
        # b值输入框
        self.bule_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.bule_le.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bule_le.setObjectName("bule_le")
        self.color_gridLayout.addWidget(self.bule_le, 3, 3, 1, 1)
        # 优先级设置保存按钮
        self.priority_save_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.priority_save_btn.setMinimumSize(QtCore.QSize(15, 0))
        self.priority_save_btn.setMaximumSize(QtCore.QSize(65, 16777215))
        self.priority_save_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.priority_save_btn.setObjectName("priority_save_btn")
        self.color_gridLayout.addWidget(self.priority_save_btn, 5, 3, 1, 1)
        self.tabWidget.addTab(self.color_tab, "")

        self.color_gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.color_Slider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.color_Slider.setOrientation(QtCore.Qt.Vertical)
        self.color_Slider.setObjectName("color_Slider")
        self.color_gridLayout.addWidget(self.color_Slider, 1, 4, 3, 1)

        self.setCentralWidget(self.centralwidget)

        self.set_color()

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Settings", "Settings"))
        self.save_email_btn.setText(_translate("Settings", "保存"))
        self.del_email_btn.setText(_translate("Settings", "删除"))
        self.add_email_btn.setText(_translate("Settings", "添加"))
        self.sender_lab.setText(_translate("Settings", "发信名称"))
        self.password_lab.setText(_translate("Settings", "密码"))
        self.ssl_lab.setText(_translate("Settings", "ssl端口"))
        self.email_lab.setText(_translate("Settings", "Email地址"))
        self.default_email_btn.setText(_translate("Settings", "默认使用"))
        self.tips_lab.setText(_translate("Settings", "暂仅支持stmp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.email_tab),
                                  _translate("Settings", "邮箱设置"))
        self.creater_reminder_btn.setText(_translate("Settings", "新建"))
        self.del_reminder_btn.setText(_translate("Settings", "删除"))
        self.up_btn.setText(_translate("Settings", "上移"))
        self.down_btn.setText(_translate("Settings", "下降"))
        self.save_reminder_btn.setText(_translate("Settings", "保存"))
        self.label.setText(_translate("Settings", "前三个时间会\n"
                                                  "在主窗口的右键菜单显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.time_tab),
                                  _translate("Settings", "提醒时间"))
        self.label_3.setText(_translate("Settings", "rgb:"))
        self.priority_save_btn.setText(_translate("Settings", "保存"))
        self.label_2.setText(_translate("Settings", "颜色设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.color_tab), _translate("Settings", "优先级颜色配置"))

    # email页的槽函数
    # 选中时配置
    def _set_config_slot(self):
        self._clear_config()

        index = self.email_list.currentRow()
        self.email_le.setText(self._email_records[index]['addr'])
        self.password_le.setText(self._email_records[index]['password'])
        self.sender_le.setText(self._email_records[index]['sender_name'])
        if self._email_records[index]['ssl_port']:
            self.ssl_le.setText(str(self._email_records[index]['ssl_port']))
        if self._email_records[index]['user_ssl'] == 1:
            self.ssl_le.setEnabled(True)
            self.ssl_rbtn.setChecked(True)
        else:
            self.ssl_le.setEnabled(False)
            self.ssl_rbtn.setChecked(False)

    # 添加
    def _add_email_item_slot(self):
        '''
        添加邮箱配置的槽函数
        :return:
        '''
        self._email_records.append({'id': -1, 'username': '', 'password': '', 'sender_name': '',
                                    'addr': 'new addr', 'ssl_port': None, 'user_ssl': 0,
                                    'is_default': 0})
        new_item = QListWidgetItem('new addr(请编辑Email地址后退出)')
        # new_item.setFlags(
        #         QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.email_list.insertItem(len(self._email_records), new_item)
        table = 'Email_settings'
        dict = {'username': self.user_info['username'], 'addr': 'new addr'}
        sql = be_sql().ins_sql(table, dict)
        exec_sql( sql)
        self.set_data()
        pass

    # 删除按钮
    def _del_item_slot(self):
        index = self.email_list.currentRow()
        if index != -1:
            ret = QMessageBox.question(self, ' ', '是否删除本条配置', QMessageBox.Yes, QMessageBox.Cancel)
            try:
                if ret == QMessageBox.Yes:
                    self.email_list.takeItem(index)
                    self._clear_config()
                    table = 'Email_settings'
                    filter_list = [
                        ['id', '=', str(self._email_records[index]['id'])]
                    ]
                    sql = be_sql().del_sql(table, filter_list=filter_list)
                    exec_sql( sql)
                elif ret == QMessageBox.Cancel:
                    pass
            except Exception as e:
                print(e)
        else:
            ret = QMessageBox.information(self, 'tips', '没有选择删除项')

    # ssl按钮
    def chcek_radio_slot(self):
        '''
        变更按钮状态时，更改对应ssl编辑框
        :return:
        '''
        if self.ssl_rbtn.isChecked():
            self.ssl_le.setEnabled(True)
        else:
            self.ssl_le.setEnabled(False)
            self.ssl_le.clear()

    # 清空邮箱设置表单
    def _clear_config(self):
        self.email_le.setText('')
        self.password_le.setText('')
        self.sender_le.setText('')
        self.ssl_le.setText('')
        self.ssl_rbtn.setChecked(False)

    # 保存设置
    def _save_email_config(self):
        if self.email_list.currentRow() == -1:
            return QMessageBox.information(self, 'tips', '没有选择配置邮箱')
        if self.email_le.text() == 'new addr':
            QMessageBox.warning(self, ' ', '请修改邮箱地址', QMessageBox.Ok)
            return 0
        if self.email_le.text():
            try:
                if self.password_le.text():
                    ssl_port = self.ssl_le.text()
                    if not ssl_port:
                        ssl_port = 'NULL'
                        user_ssl = str(0)  # 0代表不使用
                    else:
                        user_ssl = str(1)
                    if not self.sender_le.text():
                        sender_name = self.email_le.text()
                    else:
                        sender_name = self.sender_le.text()
                    # 更新设置到数据库
                    table = 'Email_settings'
                    value_dict = {'addr': self.email_le.text(), 'password': self.password_le.text(),
                                  'user_ssl': user_ssl, 'ssl_port': ssl_port,
                                  'sender_name': sender_name}
                    filter_list = [
                        ['id', '=', str(self.email_list.currentRow() + 1)],
                        ['username', '=',self.user_info['username']]
                    ]
                    sql = be_sql().update_sql(table, value_dict=value_dict, filter_list=filter_list)
                    ret = exec_sql( sql,is_update=1)
                    # 更新失败，直接插入数据
                    if ret <= 0:
                        value_dict['username']=self.user_info['username']
                        sql = be_sql().ins_sql(table,value_dict)
                        exec_sql( sql)
                    self.email_list.currentItem().setText(self.email_le.text())
                    #清除无效配置数据
                    sql = "delete from Email_settings where password is NULL;"
                    exec_sql( sql)
                    self.set_data()
                else:
                    QMessageBox.warning(self, ' ', '请输入密码', QMessageBox.Ok)
            except Exception as e:
                print(e)
        else:
            QMessageBox.warning(self, ' ', '请输入邮箱地址', QMessageBox.Ok)

    def _selectDefualt(self):
        '''
        # 默认使用按钮
        :return:
        '''
        if self.email_list.currentRow() != -1:
            for i in range(self.email_list.count()):
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                self.email_list.item(i).setForeground(brush)
            brush = QtGui.QBrush(QtGui.QColor(1, 203, 31))
            brush.setStyle(QtCore.Qt.NoBrush)
            self.email_list.currentItem().setForeground(brush)

            table = 'Email_settings'
            value_dict = {'is_default': '1'}
            filter_list = [
                ['id', '=', str(self._email_records[self.email_list.currentRow()]['id'])]
            ]
            sql = be_sql().update_sql(table, value_dict, filter_list)
            exec_sql( sql)

            value_dict['is_default'] = '0'
            filter_list[0][1] = '!='
            sql = be_sql().update_sql(table, value_dict, filter_list)
            exec_sql( sql)
        else:
            QMessageBox.information(self, ' ', '请选择优先使用的邮箱', QMessageBox.Ok)

    def _reset(self):
        self.set_data()
        # 重置email_list
        self.email_list.clear()
        for record in self._email_records:
            item = QListWidgetItem(record['addr'])
            if record['is_default'] == 1:
                brush = QtGui.QBrush(QtGui.QColor(1, 203, 31))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
            # item.setFlags(
            #         QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.email_list.addItem(item)
        # 重置 time_list
        self.time_list.clear()
        for record in self._reminder_records:
            item = QListWidgetItem(record['time'])
            item.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.time_list.addItem(item)

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
        value_dict = {'time': '00:00:00', 'username': self.user_info['username']}
        sql = be_sql().ins_sql(table, value_dict)
        exec_sql( sql)
        self.set_data()

    def _del_reminder_slot(self):
        index = self.time_list.currentRow()
        if index != -1:
            ret = QMessageBox.question(self, ' ', '是否删除此提醒时间', QMessageBox.Yes, QMessageBox.Cancel)
            try:
                if ret == QMessageBox.Yes:
                    self.time_list.takeItem(index)
                    self._clear_config()
                    table = 'reminder'
                    filter_list = [
                        ['id', '=', str(self._reminder_records[index]['id'])]
                    ]
                    sql = be_sql().del_sql(table, filter_list=filter_list)
                    exec_sql( sql)
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
            exec_sql( sql)
        pass

    # 优先级页的函数
    def set_color(self):
        self.red_Slider.setStyleSheet(
            'color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\ngridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));')

    # 窗口函数
    def closeEvent(self, *args, **kwargs):
        # tab_name = self.tabWidget.currentWidget().objectName()
        # if tab_name == 'email_tab':
        # 去除无效email配置
        sql = "delete from Email_settings where password is NULL;"
        exec_sql( sql)
        self._reset()
        # 保存当前顺序

    def show(self):
        super().show()
        # 添加置顶
        self.raise_()
