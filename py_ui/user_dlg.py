# 此文件为用户对话框的窗口
# 包括 login_dlg register_dlg logout_dlg
import logging

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QLineEdit

import config
import operateSqlite
import module
import utils

# 登录窗口
class Ui_login_Dialog(QtWidgets.QDialog):
    login_signal = pyqtSignal(str)

    def __init__(self, parent):
        logging.info('__init__')
        super().__init__(parent=parent)
        self.setupUi()
        self.retranslateUi()
        logging.info('end init')

    def setupUi(self):
        self.setObjectName("login_Dialog")
        self.resize(293, 192)
        self.setSizeGripEnabled(False)
        # 非模模式
        self.setModal(False)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.password_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_le.setObjectName("password_le")
        self.password_le.setPlaceholderText('密码')
        self.gridLayout.addWidget(self.password_le, 3, 2, 1, 1)

        self.password_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_lab.setObjectName("password_lab")
        self.gridLayout.addWidget(self.password_lab, 3, 1, 1, 1)
        # 设置模式
        self.password_le.setEchoMode(QLineEdit.Password)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)

        self.username_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username_le.setObjectName("username_le")
        self.username_le.setPlaceholderText('邮箱')
        self.gridLayout.addWidget(self.username_le, 1, 2, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.login_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)

        self.register_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn)

        self.gridLayout.addLayout(self.horizontalLayout, 6, 2, 1, 1)

        self.username_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.username_lab.setObjectName("username_lab")
        self.gridLayout.addWidget(self.username_lab, 1, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.login_btn.clicked.connect(self.do_login)
        self.register_btn.clicked.connect(self.do_register)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "登录"))
        self.password_lab.setText(_translate("Dialog", "     密码："))
        self.login_btn.setText(_translate("Dialog", "登录"))
        self.register_btn.setText(_translate("Dialog", "注册"))
        self.username_lab.setText(_translate("Dialog", "     账号："))

    def do_login(self):
        if self.username_le.text() and self.password_le.text():
            result = module.login(username=self.username_le.text(), password=self.password_le.text())
            # assert result['token'], '本地无记录'
            try:
                if result['token']:
                    table = 'user'
                    if not utils.get_user_info(table, self.username_le.text()):
                        # 没有用户直接插入
                        dict = {'username': self.username_le.text(), 'token': result['token']}
                        sql = operateSqlite.be_sql().ins_sql(table, dict)
                        operateSqlite.exec_sql(config.LDB_FILENAME, sql)
                    # 已有用户更新数据
                    else:
                        value_dict = {'token': result['token']}
                        filter_list = [['username', '=', self.username_le.text()]]
                        sql = operateSqlite.be_sql().update_sql(table=table, value_dict=value_dict,
                                                                filter_list=filter_list)
                        operateSqlite.exec_sql(config.LDB_FILENAME, sql, is_update=1)
                    try:
                        self.login_signal.emit(self.username_le.text())  # 发射信号
                    except Exception as e:
                        logging.error(e)
                    self.close()
                else:
                    QMessageBox.information(self, '提示', "{}".format(result['errMsg']),
                                            QMessageBox.Yes)
            except Exception as e:
                logging.error(e)

        elif not self.username_le.text():
            QMessageBox.information(self, '提示', "{}".format('请输入账号'), QMessageBox.Yes)
        elif not self.password_le.text():
            QMessageBox.information(self, '提示', "{}".format('请输入密码'), QMessageBox.Yes)

    def do_register(self):
        ui = Ui_register_Dialog(self)
        ui.show()


# 注销渲染
class Ui_logout_Dialog(QtWidgets.QDialog):
    logout_signal = pyqtSignal(str)

    def __init__(self, parent, username=''):
        super().__init__(parent=parent)
        self.username = username
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        self.setObjectName("logout_Dialog")
        self.resize(293, 210)
        self.setStyleSheet('background-color:rgba(255,255,255,1);')
        self.setSizeGripEnabled(False)
        self.setModal(True)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 189))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)

        self.logout_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.logout_btn.setObjectName("logout_btn")

        self.gridLayout.addWidget(self.logout_btn, 1, 1, 1, 1)
        self.wel_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.wel_lab.setObjectName("wel_lab")

        self.gridLayout.addWidget(self.wel_lab, 0, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        #
        self.logout_btn.clicked.connect(self.do_logout)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Welcome"))
        self.logout_btn.setText(_translate("Dialog", "注销"))
        self.wel_lab.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; font-weight:96; color:#5f6266; background-color:#ffffff;\">Thank you support!!!</span></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; color:#5f6266; background-color:#ffffff;\">We will then keep you up to date</span><br/></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; font-weight:600; color:#5f6266; background-color:#ffffff;\">%s</span></p></body></html>") % (
                                 self.username))

    def do_logout(self):
        # 请求登出
        state = module.logout(self.username)
        if state['state'] == 1:
            table = 'user'
            value_dict = {'token': 'NULL'}
            filter_list = [
                ['username', '=', self.username]
            ]
            sql = operateSqlite.be_sql().update_sql(table, value_dict, filter_list)
            # print(sql)
            operateSqlite.exec_sql(config.LDB_FILENAME, sql, is_update=1)
            self.close()
            self.logout_signal.emit('visitor')
        else:
            QMessageBox.information(self, '提示', "{}".format('请检查数据库文件和网络状态'), QMessageBox.Yes)


# 注册渲染
class Ui_register_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        self.setObjectName("register_Dialog")
        self.resize(293, 192)
        self.setSizeGripEnabled(False)
        self.setModal(False)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        self.password_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_le.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.password_le, 3, 2, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)

        self.username_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username_le.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.username_le, 1, 2, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 2, 1, 1)

        self.password_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_lab.setObjectName("password_lab")
        self.gridLayout.addWidget(self.password_lab, 5, 1, 1, 1)

        self.again_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.again_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.again_le, 5, 2, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)

        self.username_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.username_lab.setObjectName("username_lab")
        self.gridLayout.addWidget(self.username_lab, 1, 1, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.register_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.register_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.register_btn)

        self.close_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.close_btn)

        self.gridLayout.addLayout(self.horizontalLayout, 8, 2, 1, 1)

        self.register_btn.clicked.connect(self.do_register)
        self.close_btn.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "注册"))
        self.label.setText(_translate("Dialog", "     密码："))
        self.password_lab.setText(_translate("Dialog", " 再次确认："))
        self.username_lab.setText(_translate("Dialog", "     账号："))
        self.register_btn.setText(_translate("Dialog", "注册"))
        self.close_btn.setText(_translate("Dialog", "返回"))

    def do_register(self):
        if self.username_le.text() and self.password_le.text() and self.again_le.text() and (
                    self.password_le.text() == self.again_le.text()):
            result = utils.register(username=self.username_le.text(), password=self.again_le.text())
            if result:
                if result['state'] == 1:
                    self.close()
                else:
                    QMessageBox.information(self, '提示', "{}".format(result['errMsg']),
                                            QMessageBox.Yes)
            else:
                QMessageBox.information(self, '提示', "{}".format(result['errMsg']), QMessageBox.Yes)
        elif not self.username_le.text():
            QMessageBox.information(self, '提示', "{}".format('请输入账号'), QMessageBox.Yes)
        elif not self.password_le.text():
            QMessageBox.information(self, '提示', "{}".format('请输入密码'), QMessageBox.Yes)
        elif not self.again_le.text():
            QMessageBox.information(self, '提示', "{}".format('请再次确认密码'), QMessageBox.Yes)
        elif self.password_le.text() != self.again_le.text():
            QMessageBox.information(self, '提示', "{}".format('两次密码不正确'), QMessageBox.Yes)
