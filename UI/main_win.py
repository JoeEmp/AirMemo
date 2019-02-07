# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\demo.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

# 有注释部分基本为生成后的作者插入代码的注释

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication
from time import sleep
from module import get_records,getSize
import config
import customWidget

class Ui_MainWindow(QtWidgets.QMainWindow):
    _startPos = None
    _endPos = None
    _isTracking = False
    layoutWidth=0
    layoutHeight=0
    _records=None

    def __init__(self):
        super().__init__()
        self.setData()
        self.setupLayout()
        self.retranslateUi()
        # self.TrayIcon(MainWindow)

    # 初始化 窗口布局及控件
    def setupLayout(self):
        #窗口
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(self.layoutWidth, self.layoutHeight)
        self.setFixedSize(self.layoutWidth, self.layoutHeight)
        #窗口总布局
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.layoutWidth, self.layoutHeight))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        #总布局
        self.rootLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setObjectName("rootLayout")

        #标题栏布局
        self.titleLayout = QtWidgets.QHBoxLayout()
        self.titleLayout.setObjectName("titleLayout")
        #icon 标签
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.titleLayout.addWidget(self.label)
        self.label.setStyleSheet('border-image:url(./UI/app_icon.png);')
        #标题标签
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.titleLayout.addWidget(self.label_2)
        self.label_2.setText('AirMemo')
        #空白
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titleLayout.addItem(spacerItem)
        #关闭按钮
        self.close_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.close_btn.setText("")
        self.close_btn.setObjectName("closeButton")
        self.titleLayout.addWidget(self.close_btn)
        self.close_btn.setMaximumSize(config.BTN_WIDTH, config.BTN_HEIGHT)
        self.close_btn.clicked.connect(self.close)

        self.rootLayout.addLayout(self.titleLayout)

        #窗口内容布局
        self.winLayout = QtWidgets.QHBoxLayout()
        self.winLayout.setObjectName("winLayout")
        #隐藏按钮
        self.hideBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hideBtn.setObjectName("hideBtn")
        self.winLayout.addWidget(self.hideBtn)
        #使用 self.layoutHeight 直接占满
        self.hideBtn.setMaximumSize(config.HIDE_BTN_WIDTH,self.layoutHeight)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.note_le_list = []
        self.hide_detail_btn_list = []
        self.detail_tx_list = []
        self.detail_tx_state_list = []

        for i in range(len(self.records)):
            self.noteLayout = QtWidgets.QGridLayout()
            self.noteLayout.setObjectName("noteLayout" + str(i))

            #短消息编辑框
            self.note_le = customWidget.AirLineEdit(self.verticalLayoutWidget)
            self.noteLayout.addWidget(self.note_le, 0, 1, 1, 1)
            #将id写入objName里 bwrb 必须重构
            self.note_le.setObjectName("note_le" + str(self.records[i][0]))
            # 加入相应列表，禁用LineEdit
            self.note_le_list.append(self.note_le)
            self.note_le.setEnabled(False)
            # self.noteLineEdit.clicked.connect(self.swithEdit_state)

            #发送按钮
            self.send_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
            self.noteLayout.addWidget(self.send_btn, 0, 0, 1, 1)
            self.send_btn.setObjectName("send_btn" + str(i))
            self.send_btn.setText(str(i + 1))
            self.send_btn.setMaximumSize(config.BTN_WIDTH, config.BTN_HEIGHT)

            #收起/展开按钮
            self.hide_detail_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
            self.hide_detail_btn.setText("")
            self.noteLayout.addWidget(self.hide_detail_btn, 0, 2, 1, 1)
            self.hide_detail_btn.setObjectName("hide_detail_btn" + str(i))
            self.hide_detail_btn.setMaximumSize(config.BTN_WIDTH, config.BTN_HEIGHT)
            self.hide_detail_btn_list.append(self.hide_detail_btn)

            #详情编辑框
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
            self.send_btn.clicked.connect(self.sendEmail)
            QtCore.QMetaObject.connectSlotsByName(self)
            self.verticalLayout.addLayout(self.noteLayout)

        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName("add_btn")
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
        self.hideBtn.setText(_translate("MainWindow", "hide"))
        self.add_btn.setText(_translate("MainWindow", "add"))
        self.setStyleSheet('QMainWindow{background-color:rgba(169,169,169,0.74);}')
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框

    # 初始化数据
    def setData(self):
        self.records = get_records(config.LDB_FILENAME)
        if config.SIZEMODE == 'divide':
            divide = getSize(config.divide)
            self.layoutWidth = divide['width']
        else:
            self.layoutWidth = config.BASEWIDTH
        #20为标题宽度
        self.layoutHeight = (len(self.records) + 1) * config.BTN_HEIGHT + 20
        self.Text_isShow = False

    #系统托盘
    def TrayIcon(self, MainWindow):
        pass

    def ishide(self):
        index = self.hide_detail_btn_list.index(self.sender())
        # 隐藏  点击a后，再点击b，隐藏a
        if 1 in self.detail_tx_state_list and self.detail_tx_state_list.index(1) != index:
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
        else:
            self.detail_tx_list[index].hide()
            self.layoutHeight = self.layoutHeight - config.TEXT_HEIGHT
            self.setFixedSize(self.layoutWidth, self.layoutHeight)
            self.detail_tx_state_list[index] = 0

        # 调整大小
        self.resize(self.layoutWidth, self.layoutHeight)
        self.centralwidget.resize(self.layoutWidth, self.layoutHeight)
        self.verticalLayoutWidget.resize(self.layoutWidth, self.layoutHeight)

    def sendEmail(self):
        try:
            index = int(self.sender().text())
        except Exception as e:
            print('程序初始化出错')
        self.detail_tx_list[index].setText(str(index))
        pass

    def addNote(self):
        pass

    def switchEdit_state(self):
        index = self.note_le_list.index(self.sender())
        # if(self.note_le_list[index].isEnabled()):
        self.note_le_list[index].setEnable(True)

    # 重写移动事件
    def mouseMoveEvent(self, e: QMouseEvent):
        if not self.geometry().contains(self.pos()):
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton and not self.geometry().contains(self.pos()):
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton and not self.geometry().contains(self.pos()):
            width=QApplication.desktop().screenGeometry().width()
            if self.x() > width - config.BASEWIDTH:
                for i in range(width-self.x()-config.HIDE_BTN_WIDTH):
                    self.move(self.x()+1,self.y())
                    sleep(0.001)    # 0.001为微调结果
            self._isTracking = False
            self._startPos = None
            self._endPos = None
