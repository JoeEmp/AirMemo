# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI\demo.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(583, 386)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 216))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.rootLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setObjectName("rootLayout")
        self.titleLayout = QtWidgets.QHBoxLayout()
        self.titleLayout.setObjectName("titleLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.titleLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.titleLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titleLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.titleLayout.addWidget(self.pushButton)
        self.rootLayout.addLayout(self.titleLayout)
        self.winLayout = QtWidgets.QHBoxLayout()
        self.winLayout.setObjectName("winLayout")
        self.hideBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hideBtn.setObjectName("hideBtn")
        self.winLayout.addWidget(self.hideBtn)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.noteLayout = QtWidgets.QGridLayout()
        self.noteLayout.setObjectName("noteLayout")
        self.note_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.note_le.setObjectName("note_le")
        self.noteLayout.addWidget(self.note_le, 0, 1, 1, 1)
        self.send_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.send_btn.setText("")
        self.send_btn.setObjectName("send_btn")
        self.noteLayout.addWidget(self.send_btn, 0, 0, 1, 1)
        self.hide_detail_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hide_detail_btn.setText("")
        self.hide_detail_btn.setObjectName("hide_detail_btn")
        self.noteLayout.addWidget(self.hide_detail_btn, 0, 2, 1, 1)
        self.detail_tx = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.detail_tx.setObjectName("detail_tx")
        self.noteLayout.addWidget(self.detail_tx, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.noteLayout)
        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout.addWidget(self.add_btn)
        self.winLayout.addLayout(self.verticalLayout)
        self.rootLayout.addLayout(self.winLayout)
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "demo"))
        self.label.setText(_translate("MainWindow", "icon"))
        self.label_2.setText(_translate("MainWindow", "demo"))
        self.hideBtn.setText(_translate("MainWindow", "hide"))
        self.add_btn.setText(_translate("MainWindow", "add"))

