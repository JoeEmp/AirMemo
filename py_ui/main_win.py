import logging
import re
from time import sleep
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication, QMessageBox
import config
from comm import customWidget
from comm.operateSqlite import be_sql,sqlite_db
from py_ui.email import Ui_Email_Dialog
from py_ui.recycle import Ui_recycle_Dialog
from py_ui.demo import Ui_Sync_Dialog
from py_ui.user_dlg import Ui_login_Dialog, Ui_logout_Dialog
from module.login import get_login_status
from comm.utils import getSize, cryptograph_text
import sip
import platform
from comm.user_cache import mine
from module.note import get_notes


class Ui_MainWindow(QtWidgets.QMainWindow):
    _startPos = None
    _endPos = None
    _isTracking = False
    layoutWidth = 0
    layoutHeight = 0
    _records = None
    user_info = {}

    def __init__(self, parent=None):
        super().__init__()
        logging.info("mainwindow init")
        self.parent = parent
        self.user_info = mine.get_value('user_info')
        self.setData(username=self.user_info['username'])
        self.setupLayout()
        self.retranslateUi()

    # 初始化 窗口布局及控件
    def setupLayout(self):
        # 窗口
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(self.layoutWidth, self.layoutHeight)
        self.setFixedSize(self.layoutWidth, self.layoutHeight)
        # 置顶
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
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
        self.icon_lab.setStyleSheet('border-image:url(./ui/title.ico);')
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
        self.login_btn.setMaximumSize(
            config.COM_MICRO_BTN_WIDTH, config.COM_MICRO_BTN_HEIGHT)
        self.login_btn.setStyleSheet(
            'border-image:url(%s);' % config.LOGIN_ICON)
        # 请求登录
        self.login_btn.clicked.connect(self.show_user_dlg_slot)
        self.titleLayout.addWidget(self.login_btn)
        # 同步按钮
        self.Sync_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Sync_btn.setText("")
        self.Sync_btn.setObjectName("homology_btn")
        self.Sync_btn.setMaximumSize(
            config.COM_MICRO_BTN_WIDTH, config.COM_MICRO_BTN_HEIGHT)
        self.Sync_btn.setStyleSheet('border-image:url(%s);' % config.SYNC_ICON)
        self.Sync_btn.clicked.connect(self.show_sync_dlg_slot)
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
        self.recycle_bin_btn.setMaximumSize(config.COM_MICRO_BTN_WIDTH,
                                            config.COM_MICRO_BTN_HEIGHT)
        self.recycle_bin_btn.setStyleSheet(
            'border-image:url(%s);' % config.HOMO_ICON)
        self.recycle_bin_btn.clicked.connect(self.show_recycle_dlg_slot)

        self.titleLayout.addWidget(self.recycle_bin_btn)
        # 关闭按钮
        self.close_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.close_btn.setText("")
        self.close_btn.setObjectName("closeButton")
        self.titleLayout.addWidget(self.close_btn)
        self.close_btn.setMaximumSize(
            config.COM_MICRO_BTN_WIDTH, config.COM_MICRO_BTN_HEIGHT)
        self.close_btn.setStyleSheet(
            'border-image:url(%s);' % config.CLOSE_ICON)
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
        self.welt_btn.setMaximumSize(
            config.MAIN_WELT_BTN_WIDTH, self.layoutHeight)
        self.welt_btn.clicked.connect(self.welt_slot)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.note_le_list = list()
        self.detail_tx_list = list()
        self.detail_tx_status_list = list()
        self.hide_detail_btn_list = list()

        for i in range(len(self.records)):
            self.noteLayout = QtWidgets.QGridLayout()
            self.noteLayout.setObjectName("noteLayout" + str(i))
            # self.noteLayout

            # 短消息编辑框
            self.note_le = customWidget.AirLineEdit(main_win=self,
                                                    parent=self.verticalLayoutWidget,
                                                    info=self.user_info,
                                                    color=self.records[i]['color'])
            self.noteLayout.addWidget(self.note_le, 0, 1, 1, 1)
            # 将id写入objName里 bwrb 必须重构
            self.note_le.setObjectName("note_le" + str(self.records[i]['id']))
            # 加入相应列表，禁用LineEdit
            self.note_le_list.append(self.note_le)
            self.note_le.setMaxLength(30)
            self.note_le.setStyleSheet(
                'background-color:#%s' % self.records[i]['color'])
            # self.note_le.editingFinished.connect(self.update_item_value)
            self.note_le.update_id_Signal.connect(self.update_tx_id)

            # 发送按钮
            self.send_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
            self.noteLayout.addWidget(self.send_btn, 0, 0, 1, 1)
            self.send_btn.setObjectName(
                "send_btn" + str(self.records[i]['id']))
            self.send_btn.setText(str(i + 1))
            self.send_btn.setMaximumSize(
                config.COM_BTN_WIDTH, config.COM_BTN_HEIGHT)
            self.send_btn.setStyleSheet('border-image:url(%s);' % '')
            self.send_btn.setStyleSheet(
                'background-color:rgba(196,255,255,1);')

            # 收起/展开按钮
            self.hide_detail_btn = QtWidgets.QPushButton(
                self.verticalLayoutWidget)
            self.hide_detail_btn.setText("")
            self.noteLayout.addWidget(self.hide_detail_btn, 0, 2, 1, 1)
            self.hide_detail_btn.setObjectName("hide_detail_btn" + str(i))
            # -5为微调结果
            self.hide_detail_btn.setMaximumSize(
                config.COM_MICRO_BTN_WIDTH, config.COM_MICRO_BTN_HEIGHT - 5)
            self.hide_detail_btn.setStyleSheet(
                'border-image:url(%s);' % config.LEFT_ICON)
            self.hide_detail_btn_list.append(self.hide_detail_btn)

            # 详情编辑框
            self.detail_tx = customWidget.AirTextEdit(main_win=self,
                                                      parent=self.verticalLayoutWidget, color=self.records[i]['color'])
            self.noteLayout.addWidget(self.detail_tx, 1, 0, 1, 3)
            self.detail_tx.setObjectName(
                "detail_tx" + str(self.records[i]['id']))
            # 隐藏文本框 初始化文本框状态数组
            self.detail_tx.hide()
            self.detail_tx_status_list.append(0)
            self.detail_tx_list.append(self.detail_tx)
            # 绑定槽
            self.hide_detail_btn.clicked.connect(self.ishide)
            self.send_btn.clicked.connect(self.send_Email_slot)
            QtCore.QMetaObject.connectSlotsByName(self)
            self.verticalLayout.addLayout(self.noteLayout)

        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setStyleSheet('border-image:url(%s);' % config.ADD_ICON)
        self.add_btn.clicked.connect(self.addNote_slot)
        self.verticalLayout.addWidget(self.add_btn)

        self.winLayout.addLayout(self.verticalLayout)
        self.rootLayout.addLayout(self.winLayout)
        self.setCentralWidget(self.centralwidget)

    # 初始化相应文本
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "AirMemo"))
        for i in range(len(self.records)):
            self.note_le_list[i].setText(self.records[i]['message'])
            self.detail_tx_list[i].setText(self.records[i]['detail'])
        self.welt_btn.setText(_translate("MainWindow", "welt"))
        self.add_btn.setText(_translate("MainWindow", "add"))
        self.setStyleSheet(
            'QMainWindow{background-color:rgba(196,255,255,1);}')
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        # self.setStyleSheet('QMainWindow{border-top-left-radius:15px;border-top-right-radius:15px;}')

    def setData(self, username=None):
        '''
        根据用户初始化数据
        :param username: 用户名
        :return:
        '''
        username = username if username else 'visitor'
        ret = get_notes(username)
        if not ret['status']:
            logging.error(ret['msg'])
        self.records = ret['records'] if 'records' in ret.keys() else list()

        # 尺寸模式
        if config.SIZEMODE == 'divide':
            divide = getSize(config.divide)
            self.layoutWidth = divide['width']
        else:
            self.layoutWidth = config.MAIN_BASEWIDTH
        # 20为标题高度
        self.layoutHeight = (len(self.records) + 1) * \
            config.COM_BTN_HEIGHT + 20
        try:
            if 1 in self.detail_tx_status_list:
                self.layoutHeight += config.COM_TE_HEIGHT
        except Exception as e:
            logging.warning(e)
        self.Text_isShow = False
        logging.info('set data')

    def ishide(self):
        '''
        详情编辑框的展开和收起
        :return:
        '''
        index = self.hide_detail_btn_list.index(self.sender())
        # 隐藏  点击a后，再点击b，隐藏a
        if 1 in self.detail_tx_status_list and self.detail_tx_status_list.index(
                1) != index:
            self.detail_tx_list[self.detail_tx_status_list.index(1)].hide()
            self.hide_detail_btn_list[self.detail_tx_status_list.index(1)].setStyleSheet(
                'border-image:url(%s);' % config.LEFT_ICON)
            self.layoutHeight = self.layoutHeight - config.COM_TE_HEIGHT
            self.setFixedSize(self.layoutWidth, self.layoutHeight)
            self.detail_tx_status_list[self.detail_tx_status_list.index(1)] = 0

        # 展开或隐藏
        if self.detail_tx_list[index].isHidden():
            self.detail_tx_list[index].show()
            self.layoutHeight = self.layoutHeight + config.COM_TE_HEIGHT
            self.setFixedSize(self.layoutWidth, self.layoutHeight)
            self.detail_tx_status_list[index] = 1
            self.sender().setStyleSheet('border-image:url(%s);' % config.DOWN_ICON)
        else:
            self.detail_tx_list[index].hide()
            self.layoutHeight = self.layoutHeight - config.COM_TE_HEIGHT
            self.setFixedSize(self.layoutWidth, self.layoutHeight)
            self.detail_tx_status_list[index] = 0
            self.sender().setStyleSheet('border-image:url(%s);' % config.LEFT_ICON)

        # 调整大小
        self.resize(self.layoutWidth, self.layoutHeight)
        self.centralwidget.resize(self.layoutWidth, self.layoutHeight)
        self.verticalLayoutWidget.resize(self.layoutWidth, self.layoutHeight)
        self.welt_btn.setMaximumSize(
            config.MAIN_WELT_BTN_WIDTH, self.layoutHeight)

    def send_Email_slot(self):
        '''
        获取序号对应的数据，打开窗口
        :return:
        '''
        msg_id = re.findall('\d+', self.sender().objectName())[0]
        sql = 'select message,detail from Msg where id = %s' % msg_id
        ret = sqlite_db.select(sql)
        if not ret['status']:
            logging.error(ret['msg'])
        info = ret['records'][0] if 'records' in ret.keys() else {'message':'untitle','detail':'input text'}
        # info={'message':'test','detail':'123456'} #debug 使用
        email_dlg = Ui_Email_Dialog(self, info)
        email_dlg.show()

    def switchEdit_status(self):
        '''
        textEdit的状态切换
        :return:
        '''
        index = self.note_le_list.index(self.sender())
        self.note_le_list[index].setEnable(True)

    def welt_slot(self):
        '''
        便利贴贴边
        速度和CPU有关 开放给用户自己调节
        :return:
        '''
        width = QApplication.desktop().availableGeometry().width()
        platform_name = platform.system()

        if self.x() <= width - config.MAIN_BASEWIDTH:
            if 'Windows' == platform_name:
                for i in range(width - self.x() - config.MAIN_WELT_BTN_WIDTH):
                    self.move(self.x() + 1, self.y())
                    sleep(config.SPEED)
                    print(self.x(), self.y())

            elif 'Darwin' == platform_name or 'Linux' == platform_name:
                self.move(width - config.MAIN_WELT_BTN_WIDTH, self.y())
            # 变更贴图
            # self.sender().setStyleSheet('border-image:url(%s);' % config.SHOW_ICON)
        else:
            if 'Windows' == platform_name:
                for i in range(config.MAIN_BASEWIDTH - config.MAIN_WELT_BTN_WIDTH):
                    self.move(self.x() - 1, self.y())
                    sleep(config.SPEED)
            elif 'Darwin' == platform_name or 'Linux' == platform_name:
                self.move(width - config.MAIN_BASEWIDTH, self.y())
            # 变更贴图
            # self.sender().setStyleSheet('border-image:url(%s);' % config.WELT_ICON)

    def addNote_slot(self):
        '''
        增加memo
        :return:
        '''
        # 限高设置
        if QApplication.desktop().screenGeometry().height() < self.layoutHeight + config.COM_BTN_HEIGHT:
            QMessageBox.information(
                self, 'tips', '请清除一些任务后再添加', QMessageBox.Ok)
            return None
        if self.note_le.text():
            self.setData(username=self.user_info['username'])
            new_record = {'id': -1, 'detail': '',
                          'message': '', 'color': 'c4ffff'}
            self.records.append(new_record)
            self.changeLayout()
            self.retranslateUi()
            self.show()
        else:
            QMessageBox.information(self, 'tips', '请补充短消息框内容', QMessageBox.Ok)

    def changeLayout(self):
        '''
        仅用于add_note_slot 先删除add_btn,再插入 AirLineEdit 和 add_btn
        :return:
        '''
        record = self.records[-1]
        length = len(self.records)

        self.verticalLayout.removeWidget(self.add_btn)
        sip.delete(self.add_btn)

        self.noteLayout = QtWidgets.QGridLayout()
        self.noteLayout.setObjectName("noteLayout" + str(-1))
        # 短消息编辑框
        self.note_le = customWidget.AirLineEdit(main_win=self,
                                                parent=self.verticalLayoutWidget,
                                                info=self.user_info,
                                                color=record['color'])
        self.noteLayout.addWidget(self.note_le, 0, 1, 1, 1)
        # 将id写入objName里 bwrb 必须重构
        self.note_le.setObjectName("note_le" + str(record['id']))
        # 加入相应列表，禁用LineEdit
        self.note_le_list.append(self.note_le)
        self.note_le.setMaxLength(30)
        self.note_le.setStyleSheet('background-color:#%s' % record['color'])
        # self.note_le.editingFinished.connect(self.update_item_value)
        self.note_le.update_id_Signal.connect(self.update_tx_id)

        # 发送按钮
        self.send_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.noteLayout.addWidget(self.send_btn, 0, 0, 1, 1)
        self.send_btn.setObjectName("send_btn" + str(record['id']))
        self.send_btn.setText(str(length))
        self.send_btn.setMaximumSize(
            config.COM_BTN_WIDTH, config.COM_BTN_HEIGHT)
        self.send_btn.setStyleSheet('border-image:url(%s);' % '')
        self.send_btn.setStyleSheet('background-color:rgba(196,255,255,1);')

        # 收起/展开按钮
        self.hide_detail_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hide_detail_btn.setText("")
        self.noteLayout.addWidget(self.hide_detail_btn, 0, 2, 1, 1)
        self.hide_detail_btn.setObjectName("hide_detail_btn" + str(-1))
        self.hide_detail_btn.setMaximumSize(
            config.COM_BTN_WIDTH, config.COM_BTN_HEIGHT)
        self.hide_detail_btn.setStyleSheet(
            'border-image:url(%s);' % config.LEFT_ICON)
        self.hide_detail_btn_list.append(self.hide_detail_btn)

        # 详情编辑框
        self.detail_tx = customWidget.AirTextEdit(
            main_win=self, parent=self.verticalLayoutWidget)
        self.noteLayout.addWidget(self.detail_tx, 1, 0, 1, 3)
        self.detail_tx.setObjectName("detail_tx" + str(record['id']))
        # 隐藏文本框 初始化文本框状态数组
        self.detail_tx.hide()
        self.detail_tx_status_list.append(0)
        self.detail_tx_list.append(self.detail_tx)
        # 绑定槽
        self.hide_detail_btn.clicked.connect(self.ishide)
        self.send_btn.clicked.connect(self.send_Email_slot)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.verticalLayout.addLayout(self.noteLayout)

        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.addNote_slot)
        self.verticalLayout.addWidget(self.add_btn)

        # 调整窗口和布局高度
        self.layoutHeight += config.COM_BTN_HEIGHT

        self.setFixedSize(self.layoutWidth, self.layoutHeight)
        self.resize(self.layoutWidth, self.layoutHeight)
        self.centralwidget.resize(self.layoutWidth, self.layoutHeight)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(0, 0, self.layoutWidth, self.layoutHeight))

    def show_user_dlg_slot(self):
        '''
        用户窗口
        检测登录状态，已登录状态下创建注销窗口
                    未登录状态下创建登录窗口
        :return:
        '''
        # 检测登录状态
        result = get_login_status()
        # result['status'] = 1
        ui = None
        if result['status'] == 1:
            ui = Ui_login_Dialog(self)
        elif result['status'] == 0:
            try:
                ui = Ui_logout_Dialog(self, self.user_info['username'])
            except Exception as e:
                logging.error(e)
        else:
            QMessageBox.information(self, '提示', "{}".format(
                result['msg']), QMessageBox.Yes)
            return -1
        if ui:
            ui.show()

    def get_update_Signal(self, username, is_welcome=0):
        '''
        根据当前登录用户名，去更新数据memo
        :param username:
        :param is_welcome:
        :return:
        '''
        if is_welcome == 1:
            return True
        if username:
            self.reset(username)
            return True
        else:
            QMessageBox.information(
                self, '提示', "{}".format('登录信息错误'), QMessageBox.Yes)
            return False

    def reset(self, username):
        '''
        根据username名，更新整个窗口的data
        :param username:
        :return:
        '''
        self.check()
        self.setData(username)
        self.setupLayout()
        self.retranslateUi()
        self.show()

    def check(self):
        '''
        用于检测用户的登录状态
        :return:
        '''
        self.user_info = mine.get_value('user_info')
        logging.warning(self.user_info)
        ret = get_notes(self.user_info['username'])
        if not ret['status']:
            logging.error(ret['msg'])
        records = ret['records'] if 'records' in ret.keys() else list()
        if not records:
            table = 'Msg'
            dict = {'message': 'Welcome',
                    'detail': 'Thanks\ you\ support',
                    'username': self.user_info['username']}
            dict['message'] = cryptograph_text(
                dict['message'], 'message', user_name=self.user_info['username'])
            dict['detail'] = cryptograph_text(
                dict['detail'], 'detail', user_name=self.user_info['username'])
            sql = be_sql().ins_sql(table, dict)
            sqlite_db.transaction(sql)
        return self.user_info['username']

    def update_tx_id(self, id):
        self.detail_tx_list[-1].setObjectName('detail_tx' + str(id))

    def show_recycle_dlg_slot(self):
        '''
        创建回收站
        :return:
        '''
        dlg = Ui_recycle_Dialog(parent=self)
        dlg.updateSignal.connect(self.get_update_Signal)

    def show_sync_dlg_slot(self):
        result = get_login_status()
        # result['status'] = 0
        if result['status'] == 0:
            try:
                dlg = Ui_Sync_Dialog(parent=self)
            except Exception as e:
                logging.warning(e)
                QMessageBox.information(
                    self, 'tips', "无法连接服务器", QMessageBox.Ok)
        else:
            QMessageBox.information(
                self, 'tips', result['msg'], QMessageBox.Ok)

    # 重写类方法
    def show(self):
        super().show()
        # 添加置顶
        self.raise_()

    # 重写移动事件
    def mouseMoveEvent(self, e: QMouseEvent):
        # if not self.geometry().contains(self.pos()):
        if self._startPos:
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
            platform_name = platform.system()
            # x轴判断
            if self.x() > width - config.MAIN_WELT_BTN_WIDTH:
                if 'Windows' == platform_name:
                    for i in range(width - self.x() - config.MAIN_WELT_BTN_WIDTH):
                        self.move(self.x() + 1, self.y())
                        sleep(config.SPEED)
                        print(self.x(), self.y())

                elif 'Darwin' == platform_name or 'Linux' == platform_name:
                    self.move(width - config.MAIN_WELT_BTN_WIDTH, self.y())
                # 变更贴图
                # self.sender().setStyleSheet('border-image:url(%s);' % config.SHOW_ICON)
            elif self.x() > width - config.MAIN_BASEWIDTH:
                if 'Windows' == platform_name:
                    for i in range(width - self.x() - config.MAIN_WELT_BTN_WIDTH):
                        self.move(self.x() + 1, self.y())
                        sleep(config.SPEED)  # 0.001为微调结果
                elif 'Darwin' == platform_name or 'Linux' == platform_name:
                    self.move(width - config.MAIN_BASEWIDTH, self.y())
                # 变更贴图
                # self.sender().setStyleSheet('border-image:url(%s);' % config.WELT_ICON)
            self._isTracking = False
            self._startPos = None
            self._endPos = None
        # print(self.x(), self.y())
