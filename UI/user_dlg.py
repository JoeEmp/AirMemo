# 此文件为用户对话框的渲染
# 包括 login_dlg register_dlg logout_dlg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import module
import utils
import config
import logging


# 登录渲染
class Ui_login_Dialog(QtWidgets.QDialog):
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
        self.setModal(True)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.password_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.password_le, 3, 2, 1, 1)
        self.password_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_lab.setObjectName("password_lab")
        self.gridLayout.addWidget(self.password_lab, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.username_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username_le.setObjectName("username_le")
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.login_btn.clicked.connect(self.do_login)

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
            if result['token']:
                value_dict = {'token': result['token']}
                filter_list = [['username', '=', self.username_le.text()]]
                sql = utils.be_sql().update_sql(table='user', value_dict=value_dict, filter_list=filter_list)
                utils.exec_sql(config.LDB_FILENAME,sql)
                self.close()
            else:
                QMessageBox.information(self, '提示', "{}".format(result['errMsg']), QMessageBox.Yes)
        elif not self.username_le.text():
            QMessageBox.information(self, '提示', "{}".format('请输入账号'), QMessageBox.Yes)
        elif not self.password_le.text():
            QMessageBox.information(self, '提示', "{}".format('请输入密码'), QMessageBox.Yes)

    def do_register(self):
        pass


# 注销渲染
class Ui_logout_Dialog(object):
    def __init__(self, parent, username):
        super().__init__(parent=parent)
        self.username = username

    def setupUi(self, Dialog, username):
        self.username = username

        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 210)
        Dialog.setStyleSheet('background-color:rgba(255,255,255,1);')
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 189))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.logout_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.logout_btn.setObjectName("logout_btn")
        self.gridLayout.addWidget(self.logout_btn, 1, 1, 1, 1)
        self.wel_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.wel_lab.setObjectName("wel_lab")
        self.gridLayout.addWidget(self.wel_lab, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Welcome"))
        self.logout_btn.setText(_translate("Dialog", "注销"))
        self.wel_lab.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; font-weight:96; color:#5f6266; background-color:#ffffff;\">Thank you support!!!</span></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; color:#5f6266; background-color:#ffffff;\">We will then keep you up to date</span><br/></p><p align=\"center\"><span style=\" font-family:\'Arial,Microsoft YaHei,微软雅黑,宋体,Malgun Gothic,Meiryo,sans-serif\'; font-size:13px; font-weight:600; color:#5f6266; background-color:#ffffff;\">%s</span></p></body></html>") % (
                                 self.username))


# 注册渲染
class Ui_register_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 192)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 2, 1, 1)
        self.password_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_lab.setObjectName("password_lab")
        self.gridLayout.addWidget(self.password_lab, 5, 1, 1, 1)
        self.password_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.password_le, 5, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        self.username_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.username_lab.setObjectName("username_lab")
        self.gridLayout.addWidget(self.username_lab, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        self.register_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "     密码："))
        self.password_lab.setText(_translate("Dialog", " 再次确认："))
        self.username_lab.setText(_translate("Dialog", "     账号："))
        self.login_btn.setText(_translate("Dialog", "注册"))
        self.register_btn.setText(_translate("Dialog", "返回"))
