# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\demo.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

# 有注释部分基本为生成后的作者插入代码的注释

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu

from module import get_records, getSize
import config
from customWidget import AirLineEdit


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setUi(self, MainWindow):
        self.setData(MainWindow)
        self.setupLaylout(MainWindow)
        self.retranslateUi(MainWindow)
        self.TrayIcon(MainWindow)

    # 初始化 窗口布局及控件
    def setupLaylout(self, MainWindow):
        # 窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.layoutWidth, self.layoutHeight)

        # 窗口总布局
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # 窗口大小
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.layoutWidth, self.layoutHeight))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # Memo总布局
        self.rootLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setObjectName("rootLayout")
        self.rootLayout.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        # 收起按钮
        self.hideBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hideBtn.setObjectName("hideBtn")
        # 尺寸限制
        self.hideBtn.setMaximumSize(config.hideButtonWidth, 20)
        self.rootLayout.addWidget(self.hideBtn)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.noteLineEditList = []
        self.hide_detailBtnList = []
        self.detailTextEditList = []
        self.detailTextEdit_state_List = []

        for i in range(len(self.records)):
            self.noteLayout = QtWidgets.QGridLayout()
            self.noteLayout.setObjectName("noteLayout" + str(i))

            # 收起/展开按钮
            self.hide_detailBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.hide_detailBtn.setObjectName("hide_detailBtn" + str(i))
            self.hide_detailBtn.setMaximumSize(config.buttonWidth, config.buttonHeight)
            self.noteLayout.addWidget(self.hide_detailBtn, 0, 2, 1, 1)
            # 加入相应列表
            self.hide_detailBtnList.append(self.hide_detailBtn)

            self.verticalLayout.addLayout(self.noteLayout)

            # 发送按钮
            self.sendBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.sendBtn.setObjectName("sendBtn" + str(i))
            self.sendBtn.setText(str(i + 1))
            # 限制最大尺寸
            self.sendBtn.setMaximumSize(config.buttonWidth, config.buttonHeight)
            self.noteLayout.addWidget(self.sendBtn, 0, 0, 1, 1)

            # 短消息编辑框
            self.noteLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
            self.noteLineEdit.setObjectName("noteLineEdit" + str(i))
            self.noteLayout.addWidget(self.noteLineEdit, 0, 1, 1, 1)

            # 加入相应列表，禁用LineEdit
            self.noteLineEditList.append(self.noteLineEdit)
            self.noteLineEdit.setEnabled(False)
            # self.noteLineEdit.clicked.connect(self.swithEdit_state)

            # 详情编辑框
            self.detailTextEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
            self.detailTextEdit.setObjectName("detailTextEdit" + str(i))
            self.noteLayout.addWidget(self.detailTextEdit, 1, 0, 1, 3)
            # 隐藏文本框 初始化文本框状态数组
            self.detailTextEdit.hide()
            self.detailTextEdit_state_List.append(0)
            self.detailTextEditList.append(self.detailTextEdit)
            # 绑定槽
            self.hide_detailBtn.clicked.connect(lambda: self.ishide(MainWindow))
            self.sendBtn.clicked.connect(self.sendEmail)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        self.addBtn.clicked.connect(self.addNote)

        self.rootLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

    # 初始化相应文本
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AirMemo"))
        # MainWindow.setWindowIcon(QIcon('./ui/IconV2.png'))
        for i in range(len(self.records)):
            # 根据表结构写死了两个索引值，后面再改 wrb
            self.noteLineEditList[i].setText(self.records[i][1])
            self.detailTextEditList[i].setText(self.records[i][2])

        # for i in range(3):
        #     self.sendBtn.setText(_translate("MainWindow",str(i)))
        self.hideBtn.setText(_translate("MainWindow", "hide"))
        # self.hide_detailBtn.setText(_translate("MainWindow", "hide_detail"))
        self.addBtn.setText(_translate("MainWindow", "add"))

    # 初始化数据
    def setData(self, MainWindow):
        self.records = get_records(config.filename)
        if config.SIZEMODE == 'divide':
            divide = getSize(config.divide)
            self.layoutWidth = divide['width']
        else:
            self.layoutWidth = config.baseWidth
        self.layoutHeight = (len(self.records) + 1) * config.buttonHeight

        self.Text_isShow = False
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTitleHint)
        # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # MainWindow.setWindowFlags(QtCore.Qt.WindowTitleHint)

        pass

    def TrayIcon(self, MainWindow):

        pass

    def ishide(self, MainWindow):
        index = self.hide_detailBtnList.index(self.sender())
        # 隐藏  点击a后，再点击b，隐藏a
        if 1 in self.detailTextEdit_state_List and self.detailTextEdit_state_List.index(1) != index:
            self.detailTextEditList[self.detailTextEdit_state_List.index(1)].hide()
            self.layoutHeight = self.layoutHeight - config.textHeight
            self.detailTextEdit_state_List[self.detailTextEdit_state_List.index(1)] = 0

        # 展开或隐藏
        if self.detailTextEditList[index].isHidden():
            self.detailTextEditList[index].show()
            self.layoutHeight = self.layoutHeight + config.textHeight
            self.detailTextEdit_state_List[index] = 1
        else:
            self.detailTextEditList[index].hide()
            self.layoutHeight = self.layoutHeight - config.textHeight
            self.detailTextEdit_state_List[index] = 0

        # 调整大小
        MainWindow.resize(self.layoutWidth, self.layoutHeight)
        self.centralwidget.resize(self.layoutWidth, self.layoutHeight)
        self.horizontalLayoutWidget.resize(self.layoutWidth, self.layoutHeight)

    def sendEmail(self):
        try:
            index = int(self.sender().text())
        except Exception as e:
            print('程序初始化出错')
        self.detailTextEditList[index].setText(str(index))
        pass

    def addNote(self):
        pass

    def swithEdit_state(self):
        index = self.noteLineEditList.index(self.sender())
        # if(self.noteLineEditList[index].isEnabled()):
        self.noteLineEditList[index].setEnable(True)
