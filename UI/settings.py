# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\settings.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(771, 422)
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 761, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.email_tab = QtWidgets.QWidget()
        self.email_tab.setObjectName("email_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.email_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.email_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.email_lab.setObjectName("email_lab")
        self.gridLayout.addWidget(self.email_lab, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 4, 1)
        self.sender_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sender_lab.setObjectName("sender_lab")
        self.gridLayout.addWidget(self.sender_lab, 3, 1, 1, 1)
        self.password_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_lab.setObjectName("password_lab")
        self.gridLayout.addWidget(self.password_lab, 1, 1, 1, 1)
        self.ssl_lab = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ssl_lab.setObjectName("ssl_lab")
        self.gridLayout.addWidget(self.ssl_lab, 2, 1, 1, 1)
        self.ssl_rbtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.ssl_rbtn.setText("")
        self.ssl_rbtn.setObjectName("ssl_rbtn")
        self.gridLayout.addWidget(self.ssl_rbtn, 2, 2, 1, 1)
        self.password_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.password_le, 1, 2, 1, 2)
        self.ssl_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ssl_le.setObjectName("ssl_le")
        self.gridLayout.addWidget(self.ssl_le, 2, 3, 1, 1)
        self.email_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_le.setObjectName("email_le")
        self.gridLayout.addWidget(self.email_le, 0, 2, 1, 2)
        self.save1_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save1_btn.setObjectName("save1_btn")
        self.gridLayout.addWidget(self.save1_btn, 4, 3, 1, 1)
        self.sender_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sender_le.setObjectName("sender_le")
        self.gridLayout.addWidget(self.sender_le, 3, 2, 1, 2)
        self.tabWidget.addTab(self.email_tab, "")
        self.color_tab = QtWidgets.QWidget()
        self.color_tab.setObjectName("color_tab")
        self.tabWidget.addTab(self.color_tab, "")
        self.time_tab = QtWidgets.QWidget()
        self.time_tab.setObjectName("time_tab")
        self.tabWidget.addTab(self.time_tab, "")
        self.color_tab1 = QtWidgets.QWidget()
        self.color_tab1.setObjectName("color_tab1")
        self.mainWgt = QtWidgets.QWidget(self.color_tab1)
        self.mainWgt.setGeometry(QtCore.QRect(10, 0, 741, 391))
        self.mainWgt.setObjectName("mainWgt")
        self.basicGroup = QtWidgets.QGroupBox(self.mainWgt)
        self.basicGroup.setGeometry(QtCore.QRect(100, 10, 228, 216))
        self.basicGroup.setObjectName("basicGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.basicGroup)
        self.horizontalLayout.setContentsMargins(5, 10, 5, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.basicColorWgt = BasicColorArea(self.basicGroup)
        self.basicColorWgt.setMinimumSize(QtCore.QSize(214, 191))
        self.basicColorWgt.setMaximumSize(QtCore.QSize(214, 191))
        self.basicColorWgt.setObjectName("basicColorWgt")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.basicColorWgt)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-240, -70, 741, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout.addWidget(self.basicColorWgt)
        self.customGroup = QtWidgets.QGroupBox(self.mainWgt)
        self.customGroup.setGeometry(QtCore.QRect(100, 230, 228, 81))
        self.customGroup.setObjectName("customGroup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.customGroup)
        self.horizontalLayout_2.setContentsMargins(5, 10, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.customColorWgt = CustomColorArea(self.customGroup)
        self.customColorWgt.setMinimumSize(QtCore.QSize(214, 52))
        self.customColorWgt.setMaximumSize(QtCore.QSize(214, 52))
        self.customColorWgt.setObjectName("customColorWgt")
        self.horizontalLayout_2.addWidget(self.customColorWgt)
        self.layoutWidget = QtWidgets.QWidget(self.mainWgt)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 230, 220, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(12, 26))
        self.label.setMaximumSize(QtCore.QSize(12, 26))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.colorEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.colorEdit.setMinimumSize(QtCore.QSize(72, 26))
        self.colorEdit.setMaximumSize(QtCore.QSize(72, 26))
        self.colorEdit.setObjectName("colorEdit")
        self.horizontalLayout_3.addWidget(self.colorEdit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.addCustomColorBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.addCustomColorBtn.setMinimumSize(QtCore.QSize(0, 26))
        self.addCustomColorBtn.setMaximumSize(QtCore.QSize(16777215, 26))
        self.addCustomColorBtn.setObjectName("addCustomColorBtn")
        self.horizontalLayout_4.addWidget(self.addCustomColorBtn)
        self.layoutWidget1 = QtWidgets.QWidget(self.mainWgt)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 20, 301, 272))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.svColorWgt = SVColorArea(self.layoutWidget1)
        self.svColorWgt.setMinimumSize(QtCore.QSize(256, 256))
        self.svColorWgt.setMaximumSize(QtCore.QSize(256, 256))
        self.svColorWgt.setObjectName("svColorWgt")
        self.horizontalLayout_5.addWidget(self.svColorWgt)
        self.hColorWgt = HColorArea(self.layoutWidget1)
        self.hColorWgt.setMinimumSize(QtCore.QSize(34, 270))
        self.hColorWgt.setMaximumSize(QtCore.QSize(34, 270))
        self.hColorWgt.setObjectName("hColorWgt")
        self.horizontalLayout_5.addWidget(self.hColorWgt)
        self.layoutWidget2 = QtWidgets.QWidget(self.mainWgt)
        self.layoutWidget2.setGeometry(QtCore.QRect(330, 270, 240, 70))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.curColorLbl = QtWidgets.QLabel(self.layoutWidget2)
        self.curColorLbl.setMinimumSize(QtCore.QSize(30, 40))
        self.curColorLbl.setMaximumSize(QtCore.QSize(30, 40))
        self.curColorLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.curColorLbl.setWordWrap(True)
        self.curColorLbl.setObjectName("curColorLbl")
        self.horizontalLayout_6.addWidget(self.curColorLbl)
        self.previewWgt = PreviewColorArea(self.layoutWidget2)
        self.previewWgt.setMinimumSize(QtCore.QSize(166, 68))
        self.previewWgt.setMaximumSize(QtCore.QSize(166, 68))
        self.previewWgt.setObjectName("previewWgt")
        self.horizontalLayout_6.addWidget(self.previewWgt)
        self.newColorLbl = QtWidgets.QLabel(self.layoutWidget2)
        self.newColorLbl.setMinimumSize(QtCore.QSize(30, 40))
        self.newColorLbl.setMaximumSize(QtCore.QSize(30, 40))
        self.newColorLbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.newColorLbl.setWordWrap(True)
        self.newColorLbl.setObjectName("newColorLbl")
        self.horizontalLayout_6.addWidget(self.newColorLbl)
        self.layoutWidget3 = QtWidgets.QWidget(self.mainWgt)
        self.layoutWidget3.setGeometry(QtCore.QRect(557, 25, 146, 110))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.hLabel.setMinimumSize(QtCore.QSize(66, 26))
        self.hLabel.setMaximumSize(QtCore.QSize(66, 26))
        self.hLabel.setScaledContents(False)
        self.hLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hLabel.setObjectName("hLabel")
        self.gridLayout_2.addWidget(self.hLabel, 0, 0, 1, 1)
        self.hSpinBox = QtWidgets.QSpinBox(self.layoutWidget3)
        self.hSpinBox.setMinimumSize(QtCore.QSize(72, 28))
        self.hSpinBox.setMaximumSize(QtCore.QSize(70, 26))
        self.hSpinBox.setAccelerated(True)
        self.hSpinBox.setMaximum(360)
        self.hSpinBox.setObjectName("hSpinBox")
        self.gridLayout_2.addWidget(self.hSpinBox, 0, 1, 1, 1)
        self.sLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.sLabel.setMinimumSize(QtCore.QSize(66, 26))
        self.sLabel.setMaximumSize(QtCore.QSize(66, 26))
        self.sLabel.setScaledContents(False)
        self.sLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLabel.setObjectName("sLabel")
        self.gridLayout_2.addWidget(self.sLabel, 1, 0, 1, 1)
        self.sSpinBox = QtWidgets.QSpinBox(self.layoutWidget3)
        self.sSpinBox.setMinimumSize(QtCore.QSize(72, 28))
        self.sSpinBox.setMaximumSize(QtCore.QSize(70, 26))
        self.sSpinBox.setAccelerated(True)
        self.sSpinBox.setMaximum(255)
        self.sSpinBox.setObjectName("sSpinBox")
        self.gridLayout_2.addWidget(self.sSpinBox, 1, 1, 1, 1)
        self.vLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.vLabel.setMinimumSize(QtCore.QSize(66, 26))
        self.vLabel.setMaximumSize(QtCore.QSize(66, 26))
        self.vLabel.setScaledContents(False)
        self.vLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vLabel.setObjectName("vLabel")
        self.gridLayout_2.addWidget(self.vLabel, 2, 0, 1, 1)
        self.vSpinBox = QtWidgets.QSpinBox(self.layoutWidget3)
        self.vSpinBox.setMinimumSize(QtCore.QSize(72, 28))
        self.vSpinBox.setMaximumSize(QtCore.QSize(70, 26))
        self.vSpinBox.setAccelerated(True)
        self.vSpinBox.setMaximum(255)
        self.vSpinBox.setObjectName("vSpinBox")
        self.gridLayout_2.addWidget(self.vSpinBox, 2, 1, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.mainWgt)
        self.layoutWidget4.setGeometry(QtCore.QRect(558, 153, 146, 110))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rLabel = QtWidgets.QLabel(self.layoutWidget4)
        self.rLabel.setMinimumSize(QtCore.QSize(66, 26))
        self.rLabel.setMaximumSize(QtCore.QSize(66, 26))
        self.rLabel.setScaledContents(False)
        self.rLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rLabel.setObjectName("rLabel")
        self.gridLayout_3.addWidget(self.rLabel, 0, 0, 1, 1)
        self.rSpinBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.rSpinBox.setMinimumSize(QtCore.QSize(72, 28))
        self.rSpinBox.setMaximumSize(QtCore.QSize(70, 26))
        self.rSpinBox.setAccelerated(True)
        self.rSpinBox.setMaximum(255)
        self.rSpinBox.setObjectName("rSpinBox")
        self.gridLayout_3.addWidget(self.rSpinBox, 0, 1, 1, 1)
        self.gLabel = QtWidgets.QLabel(self.layoutWidget4)
        self.gLabel.setMinimumSize(QtCore.QSize(66, 26))
        self.gLabel.setMaximumSize(QtCore.QSize(66, 26))
        self.gLabel.setScaledContents(False)
        self.gLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gLabel.setObjectName("gLabel")
        self.gridLayout_3.addWidget(self.gLabel, 1, 0, 1, 1)
        self.gSpinBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.gSpinBox.setMinimumSize(QtCore.QSize(72, 28))
        self.gSpinBox.setMaximumSize(QtCore.QSize(70, 26))
        self.gSpinBox.setAccelerated(True)
        self.gSpinBox.setMaximum(255)
        self.gSpinBox.setObjectName("gSpinBox")
        self.gridLayout_3.addWidget(self.gSpinBox, 1, 1, 1, 1)
        self.bLabel = QtWidgets.QLabel(self.layoutWidget4)
        self.bLabel.setMinimumSize(QtCore.QSize(66, 26))
        self.bLabel.setMaximumSize(QtCore.QSize(66, 26))
        self.bLabel.setScaledContents(False)
        self.bLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bLabel.setObjectName("bLabel")
        self.gridLayout_3.addWidget(self.bLabel, 2, 0, 1, 1)
        self.bSpinBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.bSpinBox.setMinimumSize(QtCore.QSize(72, 28))
        self.bSpinBox.setMaximumSize(QtCore.QSize(70, 26))
        self.bSpinBox.setAccelerated(True)
        self.bSpinBox.setMaximum(255)
        self.bSpinBox.setObjectName("bSpinBox")
        self.gridLayout_3.addWidget(self.bSpinBox, 2, 1, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.mainWgt)
        self.layoutWidget5.setGeometry(QtCore.QRect(570, 350, 138, 28))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.okBtn = QtWidgets.QPushButton(self.layoutWidget5)
        self.okBtn.setMinimumSize(QtCore.QSize(62, 26))
        self.okBtn.setMaximumSize(QtCore.QSize(62, 26))
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_7.addWidget(self.okBtn)
        self.cancelBtn = QtWidgets.QPushButton(self.layoutWidget5)
        self.cancelBtn.setMinimumSize(QtCore.QSize(62, 26))
        self.cancelBtn.setMaximumSize(QtCore.QSize(62, 26))
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_7.addWidget(self.cancelBtn)
        self.listWidget_2 = QtWidgets.QListWidget(self.mainWgt)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 10, 91, 351))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.tabWidget.addTab(self.color_tab1, "")
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.email_lab.setText(_translate("Settings", "Email地址"))
        self.sender_lab.setText(_translate("Settings", "发信名称"))
        self.password_lab.setText(_translate("Settings", "密码"))
        self.ssl_lab.setText(_translate("Settings", "ssl端口"))
        self.save1_btn.setText(_translate("Settings", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.email_tab), _translate("Settings", "邮箱设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.color_tab), _translate("Settings", "memo颜色"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.time_tab), _translate("Settings", "提醒时间"))
        self.basicGroup.setTitle(_translate("Settings", "基本颜色"))
        self.customGroup.setTitle(_translate("Settings", "自定义颜色"))
        self.label.setText(_translate("Settings", "#"))
        self.addCustomColorBtn.setText(_translate("Settings", "添加到自定义颜色"))
        self.curColorLbl.setText(_translate("Settings", "当前颜色"))
        self.newColorLbl.setText(_translate("Settings", "新的颜色"))
        self.hLabel.setText(_translate("Settings", "色调(H):"))
        self.hSpinBox.setSuffix(_translate("Settings", "度"))
        self.sLabel.setText(_translate("Settings", "饱和度(S):"))
        self.vLabel.setText(_translate("Settings", "亮度(V):"))
        self.rLabel.setText(_translate("Settings", "红(R):"))
        self.gLabel.setText(_translate("Settings", "绿(G):"))
        self.bLabel.setText(_translate("Settings", "蓝(B):"))
        self.okBtn.setText(_translate("Settings", "确定"))
        self.cancelBtn.setText(_translate("Settings", "取消"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Settings", "优先级1"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Settings", "优先级2"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Settings", "优先级3"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Settings", "优先级4"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("Settings", "非常重要"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("Settings", "重要"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("Settings", "一般"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("Settings", "非必须"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.color_tab1), _translate("Settings", "color"))

from basiccolorarea import BasicColorArea
from customcolorarea import CustomColorArea
from hcolorarea import HColorArea
from previewcolorarea import PreviewColorArea
from svcolorarea import SVColorArea
