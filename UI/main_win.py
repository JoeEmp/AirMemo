# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\demo.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

# 有注释部分基本为生成后的作者插入代码的注释

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication, QMessageBox
from time import sleep
from module import get_records, getSize, login_state, check_login_state, \
    add_records
import config
import customWidget
from UI.user_dlg import Ui_login_Dialog, Ui_logout_Dialog, Ui_register_Dialog
import logging

from utils import be_sql, exec_sql


class Ui_MainWindow(QtWidgets.QMainWindow):
    _startPos = None
    _endPos = None
    _isTracking = False
    layoutWidth = 0
    layoutHeight = 0
    _records = None

    def __init__(self):
        super().__init__()
        logging.info("mainwindow init")
        username = self.check()
        self.setData(username=username)
        self.setupLayout()
        self.retranslateUi()
        self.TrayIcon()

    # 初始化 窗口布局及控件
    def setupLayout(self):
        # 窗口
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(self.layoutWidth, self.layoutHeight)
        self.setFixedSize(self.layoutWidth, self.layoutHeight)
        # 窗口总布局
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(0, 0, self.layoutWidth, self.layoutHeight))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # 总布局
        self.rootLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setObjectName("rootLayout")

        # 标题栏布局
        self.titleLayout = QtWidgets.QHBoxLayout()
        self.titleLayout.setObjectName("titleLayout")

        # icon 标签
        self.icon_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.icon_lab.setObjectName("icon")
        self.icon_lab.setBaseSize(32, 27)
        self.titleLayout.addWidget(self.icon_lab)
        self.icon_lab.setStyleSheet('border-image:url(./UI/title.ico);')
        self.icon_lab.setText('    ')
        # 标题标签
        self.title_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title_lab.setObjectName("title")
        self.titleLayout.addWidget(self.title_lab)
        self.title_lab.setText('AirMemo')
        # 登录按钮
        self.login_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.login_btn.setText("")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setMaximumSize(config.MICRO_BTN_WIDTH,
                                      config.MICRO_BTN_HEIGHT)
        self.login_btn.setStyleSheet(
            'border-image:url(%s);' % config.login_icon)
        # 请求登录
        self.login_btn.clicked.connect(self.show_user_dlg)
        self.titleLayout.addWidget(self.login_btn)
        # 同步按钮
        self.Sync_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Sync_btn.setText("")
        self.Sync_btn.setObjectName("homology_btn")
        self.Sync_btn.setMaximumSize(config.MICRO_BTN_WIDTH,
                                     config.MICRO_BTN_HEIGHT)
        self.Sync_btn.setStyleSheet('border-image:url(%s);' % config.Sync_icon)
        self.titleLayout.addWidget(self.Sync_btn)
        # 空白
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.titleLayout.addItem(spacerItem)
        # 回收按钮
        self.recycle_bin_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.recycle_bin_btn.setText("")
        self.recycle_bin_btn.setObjectName("recycle_bin_btn")
        self.recycle_bin_btn.setMaximumSize(config.MICRO_BTN_WIDTH,
                                            config.MICRO_BTN_HEIGHT)
        self.recycle_bin_btn.setStyleSheet(
            'border-image:url(%s);' % config.homo_icon)
        self.titleLayout.addWidget(self.recycle_bin_btn)
        # 关闭按钮
        self.close_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.close_btn.setText("")
        self.close_btn.setObjectName("closeButton")
        self.titleLayout.addWidget(self.close_btn)
        self.close_btn.setMaximumSize(config.BTN_WIDTH, config.BTN_HEIGHT)
        self.close_btn.setStyleSheet(
            'border-image:url(%s);' % config.close_icon)
        self.close_btn.clicked.connect(self.close)

        self.rootLayout.addLayout(self.titleLayout)

        # 窗口内容布局
        self.winLayout = QtWidgets.QHBoxLayout()
        self.winLayout.setObjectName("winLayout")
        # 隐藏按钮
        self.welt_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.welt_btn.setObjectName("welt_btn")
        self.winLayout.addWidget(self.welt_btn)
        # 使用 self.layoutHeight 直接占满
        self.welt_btn.setMaximumSize(config.WELT_BTN_WIDTH, self.layoutHeight)
        self.welt_btn.clicked.connect(self.welt)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.note_le_list = []
        self.hide_detail_btn_list = []
        self.detail_tx_list = []
        self.detail_tx_state_list = []

        for i in range(len(self.records)):
            self.noteLayout = QtWidgets.QGridLayout()
            self.noteLayout.setObjectName("noteLayout" + str(i))
            # self.noteLayout

            # 短消息编辑框
            self.note_le = customWidget.AirLineEdit(self.verticalLayoutWidget)
            self.noteLayout.addWidget(self.note_le, 0, 1, 1, 1)
            # 将id写入objName里 bwrb 必须重构
            self.note_le.setObjectName("note_le" + str(self.records[i][0]))
            # 加入相应列表，禁用LineEdit
            self.note_le_list.append(self.note_le)
            self.note_le.setEnabled(False)
            self.note_le.setMaxLength(30)
            self.note_le.setStyleSheet('background-color:rgba(196,255,255,1);')
            # self.note_le.editingFinished.connect(self.update_item_value)

            # 发送按钮
            self.send_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
            self.noteLayout.addWidget(self.send_btn, 0, 0, 1, 1)
            self.send_btn.setObjectName("send_btn" + str(i))
            self.send_btn.setText(str(i + 1))
            self.send_btn.setMaximumSize(config.BTN_WIDTH, config.BTN_HEIGHT)
            self.send_btn.setStyleSheet('border-image:url(%s);' % '')
            self.send_btn.setStyleSheet('background-color:rgba(196,255,255,1);')

            # 收起/展开按钮
            self.hide_detail_btn = QtWidgets.QPushButton(
                self.verticalLayoutWidget)
            self.hide_detail_btn.setText("")
            self.noteLayout.addWidget(self.hide_detail_btn, 0, 2, 1, 1)
            self.hide_detail_btn.setObjectName("hide_detail_btn" + str(i))
            self.hide_detail_btn.setMaximumSize(config.BTN_WIDTH,
                                                config.BTN_HEIGHT)
            self.hide_detail_btn.setStyleSheet(
                'border-image:url(%s);' % config.hide_icon)
            self.hide_detail_btn_list.append(self.hide_detail_btn)

            # 详情编辑框
            self.detail_tx = customWidget.AirTextEdit(self.verticalLayoutWidget)
            self.noteLayout.addWidget(self.detail_tx, 1, 0, 1, 3)
            self.detail_tx.setObjectName("detail_tx" + str(self.records[i][0]))
            # 隐藏文本框 初始化文本框状态数组
            self.detail_tx.hide()
            self.detail_tx.setEnabled(False)
            self.detail_tx_state_list.append(0)
            self.detail_tx_list.append(self.detail_tx)
            # 绑定槽
            self.hide_detail_btn.clicked.connect(self.ishide)
            self.send_btn.clicked.connect(self.send_Email)
            QtCore.QMetaObject.connectSlotsByName(self)
            self.verticalLayout.addLayout(self.noteLayout)

        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.addNote)
        self.verticalLayout.addWidget(self.add_btn)

        self.winLayout.addLayout(self.verticalLayout)
        self.rootLayout.addLayout(self.winLayout)
        self.setCentralWidget(self.centralwidget)

    # 初始化相应文本
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "AirMemo"))
        for i in range(len(self.records)):
            # 根据表结构写死了两个索引值，后面再改 wrb
            self.note_le_list[i].setText(self.records[i][1])
            self.detail_tx_list[i].setText(self.records[i][2])
        self.welt_btn.setText(_translate("MainWindow", "welt"))
        self.add_btn.setText(_translate("MainWindow", "add"))
        self.setStyleSheet('QMainWindow{background-color:rgba(196,255,255,1);}')
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框

    # 初始化数据
    def setData(self, username=None):
        # 判断用户
        if username:
            self.records = get_records(config.LDB_FILENAME, username)
        else:
            self.records = get_records(config.LDB_FILENAME)

        # 尺寸模式
        if config.SIZEMODE == 'divide':
            divide = getSize(config.divide)
            self.layoutWidth = divide['width']
        else:
            self.layoutWidth = config.BASEWIDTH
        # 20为标题宽度
        self.layoutHeight = (len(self.records) + 1) * config.BTN_HEIGHT + 20
        self.Text_isShow = False
        logging.info('set data')

    # 系统托盘
    def TrayIcon(self):
        tray = customWidget.AirTray(self)

    # 笔记详情的展开和收起
    def ishide(self):
        index = self.hide_detail_btn_list.index(self.sender())
        # 隐藏  点击a后，再点击b，隐藏a
        if 1 in self.detail_tx_state_list and self.detail_tx_state_list.index(
                1) != index:
            self.detail_tx_list[self.detail_tx_state_list.index(1)].hide()
            self.layoutHeight = self.layoutHeight - config.TEXT_HEIGHT
            self.setFixedSize(self.layoutWidth, self.layoutHeight)
            self.detail_tx_state_list[self.detail_tx_state_list.index(1)] = 0

        # 展开或隐藏
        if self.detail_tx_list[index].isHidden():
            self.detail_tx_list[index].show()
            self.layoutHeight = self.layoutHeight + config.TEXT_HEIGHT
            self.setFixedSize(self.layoutWidth, self.layoutHeight)
            self.detail_tx_state_list[index] = 1
            self.sender().setStyleSheet(
                'border-image:url(%s);' % config.show_icon)
        else:
            self.detail_tx_list[index].hide()
            self.layoutHeight = self.layoutHeight - config.TEXT_HEIGHT
            self.setFixedSize(self.layoutWidth, self.layoutHeight)
            self.detail_tx_state_list[index] = 0
            self.sender().setStyleSheet(
                'border-image:url(%s);' % config.hide_icon)

        # 调整大小
        self.resize(self.layoutWidth, self.layoutHeight)
        self.centralwidget.resize(self.layoutWidth, self.layoutHeight)
        self.verticalLayoutWidget.resize(self.layoutWidth, self.layoutHeight)
        self.welt_btn.setMaximumSize(config.WELT_BTN_WIDTH, self.layoutHeight)

    # 发送邮件 未实现
    def send_Email(self):
        try:
            index = int(self.sender().text())
        except Exception as e:
            print('程序初始化出错')
        self.detail_tx_list[index].setText(str(index))
        pass

    # bwrb 关闭窗口后重新渲染了GUI交互不友好，希望找到方法动态插入
    def addNote(self):
        self.setData()
        new_record = [-1, '', '', '', 0, '']
        self.layoutHeight += config.MICRO_BTN_HEIGHT
        self.records.append(new_record)
        self.setupLayout()
        self.retranslateUi()
        self.show()

    def switchEdit_state(self):
        index = self.note_le_list.index(self.sender())
        # if(self.note_le_list[index].isEnabled()):
        self.note_le_list[index].setEnable(True)

    def welt(self):
        width = QApplication.desktop().screenGeometry().width()
        if self.x() <= width - config.BASEWIDTH:
            for i in range(width - self.x() - config.WELT_BTN_WIDTH):
                self.move(self.x() + 1, self.y())
                sleep(0.001)
                # self.sender().setSytleSheet('')
        else:
            for i in range(config.BASEWIDTH - config.WELT_BTN_WIDTH):
                self.move(self.x() - 1, self.y())
                sleep(0.001)
                # self.sender().setSytleSheet('')

    def show_user_dlg(self):
        # login_dlg = QtWidgets.QDialog(self)
        # 检测登录状态
        result = login_state()
        # result['state'] = 1
        ui = None
        if result['state'] == 1:
            ui = Ui_login_Dialog(self)
            ui.login_signal.connect(self.getDialogSignal)
        elif result['state'] == 2:
            try:
                ui = Ui_logout_Dialog(self,result['username'])
                ui.logout_signal.connect(self.getDialogSignal)
            except Exception as e:
                logging.error(e)
        else:
            QMessageBox.information(self, '提示', "{}".format(result['errMsg']),
                                    QMessageBox.Yes)
            return -1
        if ui:
            ui.show()

    """
    实现槽函数
    """

    def getDialogSignal(self, username):
        if username:
            self.reset(username)
        else:
            QMessageBox.information(self, '提示', "{}".format('登录错误'),
                                    QMessageBox.Yes)

    def reset(self, username):
        self.check()
        self.setData(username)
        self.setupLayout()
        self.retranslateUi()
        self.show()

    def check(self):
        result = check_login_state()
        if not result:
            return 'visitor'
        else:
            # wrb
            result = result[0]
            records = get_records(config.LDB_FILENAME, result[0])
            if not records:
                table = 'Msg'
                col_list = ['message', 'detail', 'username']
                value_list = ['Welcome', 'Thanks you support', result[0]]
                sql = be_sql().ins_sql(table, col_list, value_list)
                exec_sql(config.LDB_FILENAME, sql)
            return result[0]

    # 重写移动事件
    def mouseMoveEvent(self, e: QMouseEvent):
        # if not self.geometry().contains(self.pos()):
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:  # and not self.geometry().contains(self.pos()):
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    # 释放鼠标时做出判断保证正常贴边 bug：y轴没做限制
    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:  # and not self.geometry().contains(self.pos()):
            width = QApplication.desktop().screenGeometry().width()

            # x轴判断
            if self.x() > width - config.WELT_BTN_WIDTH:
                for i in range(self.x() - (width - config.WELT_BTN_WIDTH)):
                    self.move(self.x() - 1, self.y())
                    sleep(0.001)
            elif self.x() > width - config.BASEWIDTH:
                for i in range(width - self.x() - config.WELT_BTN_WIDTH):
                    self.move(self.x() + 1, self.y())
                    sleep(0.001)  # 0.001为微调结果
            self._isTracking = False
            self._startPos = None
            self._endPos = None
