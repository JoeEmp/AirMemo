# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\demo.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu

from module import get_records
import config
from customWidget import AirLineEdit

class Ui_MainWindow(object):

    def setUi(self,MainWindow):
        self.setData(MainWindow)
        self.setupLaylout(MainWindow)
        self.retranslateUi(MainWindow)
        # self.TrayIcon(MainWindow)

    #初始化数据
    def setData(self,MainWindow):
        self.records=get_records(config.LDB_FILENAME)
        self.layoutWidth=config.BASEWIDTH
        self.layoutHeight=(len(self.records)+1)*config.BTN_HEIGHT

        self.Text_isShow=False
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.WindowTitleHint)
        # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # MainWindow.setWindowFlags(QtCore.Qt.WindowTitleHint)

        pass

    def setupLaylout(self, MainWindow):
        #窗口
        records=get_records(config.LDB_FILENAME)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.layoutWidth,self.layoutHeight)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.layoutWidth,self.layoutHeight)

        #窗口总布局
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        #窗口大小
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, config.BASEWIDTH, (len(records) + 1) * config.BTN_HEIGHT))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        #Memo总布局
        self.rootLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setObjectName("rootLayout")
        self.rootLayout.setGeometry(QtCore.QRect(0, 0,560,550))
        #收起按钮
        self.hideBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hideBtn.setObjectName("hideBtn")
        #尺寸限制
        self.hideBtn.setMaximumSize(config.HIDE_BTN_WIDTH, 20)
        self.rootLayout.addWidget(self.hideBtn)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.noteLineEditList=[]
        self.hide_detailBtnList=[]
        self.detailTextEditList=[]
        self.detailTextEdit_state_List=[]

        for i in range(len(get_records(config.LDB_FILENAME))):
            self.noteLayout = QtWidgets.QGridLayout()
            self.noteLayout.setObjectName("noteLayout"+str(i))

            #收起/展开按钮
            self.hide_detailBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.hide_detailBtn.setObjectName("hide_detailBtn"+str(i))
            self.noteLayout.addWidget(self.hide_detailBtn, 0, 2, 1, 1)
            #加入相应列表
            self.hide_detailBtnList.append(self.hide_detailBtn)

            #发送按钮
            self.sendBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.sendBtn.setObjectName("sendBtn"+str(i))
            self.sendBtn.setText(str(i+1))
            self.noteLayout.addWidget(self.sendBtn, 0, 0, 1, 1)

            self.noteLE = AirLineEdit(self.horizontalLayoutWidget)
            self.noteLE.setObjectName("noteLE")
            self.noteLayout.addWidget(self.noteLE, 0, 1, 1, 1)

            self.detailTE = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
            self.detailTE.setObjectName("detailTE")
            self.noteLayout.addWidget(self.detailTE, 1, 0, 1, 3)

            self.verticalLayout.addLayout(self.noteLayout)

        self.addBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        self.rootLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "test"))
        self.hideBtn.setText(_translate("MainWindow", "hide"))
        self.hide_detailBtn.setText(_translate("MainWindow", "hide_detail"))
        self.sendBtn.setText(_translate("MainWindow", "send"))
        self.addBtn.setText(_translate("MainWindow", "add"))

