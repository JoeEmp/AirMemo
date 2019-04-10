# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\recycle.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import operateSqlite
import config
<<<<<<< HEAD
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
=======
import utils
import logging


class Ui_recycle_Dialog(QtWidgets.QDialog):
    updateSignal = pyqtSignal(str)
    item_set = set()

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.set_data(parent.user_info['username'])
        self.parent = parent
        self.setupUi()
        self.show()

    def set_data(self, username):
        self.del_records = utils.get_records(config.LDB_FILENAME, username,
                                             is_del='1')

    def setupUi(self):
        self.setObjectName("recycle_Dialog")
        self.resize(config.TEXT_WIDTH,
                    config.BTN_HEIGHT * len(self.del_records) * 2 + 50)
        # self.setFixedSize(config.TEXT_WIDTH,
        #             config.BTN_HEIGHT * len(self.del_records) * 2 + 50)
        # 窗口总布局
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
>>>>>>> joe

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(
                QtCore.QRect(10, 10, config.TEXT_WIDTH,
                             config.BTN_HEIGHT * len(
                                     self.del_records) * 2 + 30))
        #打印 布局高度
        print(self.verticalLayoutWidget.height())

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.setObjectName("verticalLayout")
        for i in range(len(self.del_records)):
            self.message_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
            self.message_check.setObjectName(
                    "message_check" + str(self.del_records[i][0]))
            # 设置 msg
            self.message_check.setText(self.del_records[i][1])
            self.message_check.setChecked(False)
            self.message_check.clicked.connect(self.set_list)
            self.verticalLayout.addWidget(self.message_check)

            self.detail_sub_lab = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.detail_sub_lab.setObjectName(
                    "detail_sub_lab" + str(self.del_records[i][0]))
            # 设置 detail
            if not self.del_records[i][2]:
                self.detail_sub_lab.setText('无详细信息')
            elif len(self.del_records[i][2]) > config.TEXT_WIDTH:
                self.detail_sub_lab.setText(
                        self.del_records[i][2][:config.TEXT_WIDTH - 3] + '...')
            else:
                self.detail_sub_lab.setText(self.del_records[i][2])
            self.verticalLayout.addWidget(self.detail_sub_lab)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.restore_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.restore_btn.setObjectName("restore_btn")
        self.horizontalLayout.addWidget(self.restore_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.restore_btn.clicked.connect(self.restore_records)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "回收站"))
        self.restore_btn.setText(_translate("Dialog", "还原"))

    def reset(self):
        self.set_data(self.parent.user_info['username'])
        self.setupUi()
        self.show()

    def restore_records(self):
        table = 'Msg'
        value_dict = {'is_del': '0'}
        for i in self.item_set:
            filter_list = [
                ['id', '=', str(i)]
            ]
            sql = operateSqlite.be_sql().update_sql(table=table,
                                                    value_dict=value_dict,
                                                    filter_list=filter_list)
            operateSqlite.exec_sql(config.LDB_FILENAME, sql)
        self.reset()
        self.item_set.clear()

    def set_list(self):
        # print(self.sender().objectName())
        try:
            id = int(re.findall('\d+', self.sender().objectName())[0])
        except Exception as e:
            logging.info(e)
        if self.sender().isChecked():
            self.item_set.add(id)
        else:
            self.item_set.remove(id)
        # print(self.item_set)

    def closeEvent(self, QCloseEvent):
        self.updateSignal.emit(self.parent.user_info['username'])
        self.item_set.clear()
