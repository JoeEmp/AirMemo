# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/email.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import logging

from PyQt5.QtWidgets import QMessageBox

from utils import mail
from operateSqlite import *
import config


class Ui_Email_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None, info=None):
        logging.info('begin')
        super().__init__(parent=parent)
        self.user_info =parent.user_info
        self.info = info
        self.set_data()
        self.setupUi()

    def set_data(self):
        sql = "select * from email_settings where username = '%s'" % 'joe'
        self.settings = exec_sql(config.LDB_FILENAME, sql)
        print(self.settings)

    def setupUi(self):
        self.setObjectName("email_Dialog")
        self.resize(503, 184)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.sender_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sender_lab.setObjectName("sender_lab")
        self.gridLayout.addWidget(self.sender_lab, 0, 1, 1, 1)
        self.sender_comb = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.sender_comb.setObjectName("comboBox")
        for i in range(len(self.settings)):
            self.sender_comb.addItem('')
        self.gridLayout.addWidget(self.sender_comb, 0, 2, 1, 2)

        # 内容标签
        self.content_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.content_lab.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.content_lab.setObjectName("content_lab")
        self.gridLayout.addWidget(self.content_lab, 4, 1, 1, 1)

        # 主题标签
        self.msg_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.msg_lab.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.msg_lab.setObjectName("Msg_lab")
        self.gridLayout.addWidget(self.msg_lab, 3, 1, 1, 1)

        # 抄送标签
        self.copy_to_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.copy_to_lab.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.copy_to_lab.setObjectName("copy_to_lab")
        self.gridLayout.addWidget(self.copy_to_lab, 2, 1, 1, 1)

        # 发送标签
        self.send_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.send_btn.setObjectName("send_btn")
        self.gridLayout.addWidget(self.send_btn, 5, 3, 1, 1)

        # 内容编辑框
        self.content_tx = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.content_tx.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.content_tx, 4, 2, 1, 2)

        # 抄送编辑框
        self.copy_tx = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.copy_tx.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.copy_tx.setObjectName("copy_tb")
        self.gridLayout.addWidget(self.copy_tx, 2, 2, 1, 2)

        # 收件人便签
        self.recipients_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.recipients_lab.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.recipients_lab.setObjectName("recipients_lab")
        self.gridLayout.addWidget(self.recipients_lab, 1, 1, 1, 1)

        # 主题编辑框
        self.Msg_tx = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Msg_tx.setObjectName("textEdit")
        self.gridLayout.addWidget(self.Msg_tx, 3, 2, 1, 2)

        # 收件人编辑框
        self.recipients_tx = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.recipients_tx.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.recipients_tx, 1, 2, 1, 2)

        self.retranslateUi(self.info)

        self.send_btn.clicked.connect(self.send_email)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, info=None):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Email"))
        self.content_lab.setText(_translate("Dialog", "内容:"))
        self.msg_lab.setText(_translate("Dialog", "主题:"))
        self.copy_to_lab.setText(_translate("Dialog", "抄送:"))
        self.send_btn.setText(_translate("Dialog", "发送"))
        self.recipients_lab.setText(_translate("Dialog", "收件人:"))
        self.sender_lab.setText(_translate("Dialog", "发送人:"))
        for i in range(len(self.settings)):
            self.sender_comb.setItemText(i,self.settings[i]['addr'])
        if info:
            self.Msg_tx.setText(info['msg'])
            self.content_tx.setText(info['detail'])


    def send_email(self):
        self.send_btn.setDisabled(True)
        info = {'username': self.user_info['username'], 'addr': self.sender_comb.currentText()}
        result = mail(info, self.Msg_tx.toPlainText(),
                      self.recipients_tx.toPlainText(), self.content_tx.toPlainText())
        self.send_btn.setEnabled(True)
        if result['state'] == 1:
            self.close()
        elif result['state'] == -1:
            QMessageBox.information(self, '提示', "{}".format(result['errMsg']), QMessageBox.Ok)
