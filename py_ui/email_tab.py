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
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 350))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.tips_lab = QLabel(self.gridLayoutWidget)
        self.tips_lab.setMaximumSize(QtCore.QSize(130, 15))
        self.tips_lab.setText('暂不支持stmp')
        self.tips_lab.setObjectName("tips_lab")
        self.gridLayout.addWidget(self.tips_lab, 0, 0, 1, 1)

        self.email_list = QListWidget(self.gridLayoutWidget)
        for record in self._email_records:
            item = QListWidgetItem(record['addr'])
            if record['is_default'] == 1:
                brush = QtGui.QBrush(QtGui.QColor(1, 203, 31))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
            item.data = record
            self.email_list.addItem(item)
        self.email_list.itemClicked.connect(self.set_email_config_form)
        self.gridLayout.addWidget(self.email_list, 1, 0, 4, 4)

        self.default_email_btn = QPushButton(self.gridLayoutWidget)
        self.default_email_btn.setText('设置默认')
        self.default_email_btn.clicked.connect(self._selectDefualt)
        self.gridLayout.addWidget(self.default_email_btn, 5, 0, 1, 1)

        self.del_email_btn = QPushButton(self.gridLayoutWidget)
        self.del_email_btn.setText('删除')
        self.del_email_btn.clicked.connect(self.del_email_config)
        self.gridLayout.addWidget(self.del_email_btn, 5, 3, 1, 1)

        self.add_email_btn = QPushButton(self.gridLayoutWidget)
        self.add_email_btn.setText('添加邮箱')
        self.add_email_btn.clicked.connect(self.set_email_config_form)
        self.gridLayout.addWidget(self.add_email_btn, 5, 1, 1, 1)

        self.email_lab = QLabel(self.gridLayoutWidget)
        self.email_lab.setText('邮箱地址')
        self.gridLayout.addWidget(self.email_lab, 1, 4, 1, 1)

        self.email_le = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.email_le, 1, 5, 1, 2)

        self.password_lab = QLabel(self.gridLayoutWidget)
        self.password_lab.setText('密码')
        self.gridLayout.addWidget(self.password_lab, 2, 4, 1, 1)

        self.password_le = QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.password_le, 2, 5, 1, 2)
        self.password_le.setEchoMode(QLineEdit.Password)

        self.ssl_lab = QLabel(self.gridLayoutWidget)
        self.ssl_lab.setText('ssl端口')
        self.gridLayout.addWidget(self.ssl_lab, 3, 4, 1, 1)

        self.ssl_rbtn = QRadioButton(self.gridLayoutWidget)
        self.ssl_rbtn.setText("")
        self.ssl_rbtn.setObjectName("ssl_rbtn")
        self.ssl_rbtn.clicked.connect(self.chcek_radio_slot)
        self.gridLayout.addWidget(self.ssl_rbtn, 3, 5, 1, 1)

        self.ssl_port_le = QLineEdit(self.gridLayoutWidget)
        self.ssl_port_le.setObjectName("ssl_le")
        self.gridLayout.addWidget(self.ssl_port_le, 3, 6, 1, 1)

        self.sender_le = QLineEdit(self.gridLayoutWidget)
        self.sender_le.setObjectName("sender_le")
        self.gridLayout.addWidget(self.sender_le, 4, 5, 1, 2)

        self.sender_lab = QLabel(self.gridLayoutWidget)
        self.sender_lab.setText('发信名称')
        self.gridLayout.addWidget(self.sender_lab, 4, 4, 1, 1)

        self.save_email_btn = QPushButton(self.gridLayoutWidget)
        self.save_email_btn.setText('保存')
        self.save_email_btn.clicked.connect(self.save_email_config)
        self.gridLayout.addWidget(self.save_email_btn, 5, 6, 1, 1)

    def save_email_config(self):
        if not self.email_le.text():
            return Toast(self).show_toast('请输入邮箱地址', height=0.15)
        if not self.password_le.text():
            return Toast(self).show_toast('请输入邮箱第三方设置密码', time=1500, height=0.15)
        else:
            ssl_port = self.ssl_port_le.text()
            if not ssl_port:
                ssl_port = None
                user_ssl = 0
            else:
                user_ssl = 1
            sender_name = self.email_le.text() or self.sender_le.text()
            args = [
                self.user_info['username'],
                self.email_le.text(),
                self.password_le.text(),
                sender_name,
                ssl_port,
                user_ssl
            ]
            if -1 != self.email_list.currentIndex:
                add_email_conf(*args)
                self.set_email_config_form()
                Toast(self).show_toast("添加成功", height=0.1)
            else:
                update_email_conf(*args)
            self.refresh_widget()

    def _selectDefualt(self):
        if self.email_list.currentRow() != -1:
            id = self.email_list.currentItem().data['id']
            set_is_default_email_conf(id, self.user_info['username'])
            self.refresh_email_tab()
        else:
            Toast(self).show_toast('请选择优先使用的邮箱', height=0.15)

    def refresh_widget(self):
        self.email_list.clear()
        self.set_email_config_form()
        for record in get_user_email_conf(self.user_info['username']).get('records', []):
            item = QListWidgetItem(record['addr'])
            if record['is_default'] == 1:
                brush = QtGui.QBrush(QtGui.QColor(1, 203, 31))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
            item.data = record
            self.email_list.addItem(item)

    def set_email_config_form(self, item=None):
        if item:
            data = item.data
        else:
            data = {
                "addr": '',
                "password": "",
                "sender_name": "",
                "ssl_port": '',
                "user_ssl": 0
            }
        self.email_le.setText(data['addr'])
        self.password_le.setText(data['password'])
        self.sender_le.setText(data['sender_name'])
        if data['ssl_port']:
            self.ssl_port_le.setText(str(data['ssl_port']))
        if data['user_ssl'] == 1:
            self.ssl_port_le.setEnabled(True)
            self.ssl_rbtn.setChecked(True)
        else:
            self.ssl_port_le.setEnabled(False)
            self.ssl_rbtn.setChecked(False)

    def del_email_config(self):
        index = self.email_list.currentRow()
        item = self.email_list.currentItem()
        if item:
            ret = QMessageBox.question(self, ' ', '是否删除本条配置',
                                       QMessageBox.Yes, QMessageBox.Cancel)
            try:
                if ret == QMessageBox.Yes:
                    del_email_conf(item.data['id'])
                    self.email_list.takeItem(index)
                    self.clear_email_form()
            except Exception as e:
                logging.error(e)
        else:
            Toast(self).show_toast('没有选择删除项')

    def chcek_radio_slot(self):
        if self.ssl_rbtn.isChecked():
            self.ssl_port_le.setEnabled(True)
        else:
            self.ssl_port_le.setEnabled(False)
            self.ssl_port_le.clear()
