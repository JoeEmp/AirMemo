# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'UI/timeout_tip.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import platform
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Ui_timeout_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowFlag(Qt.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:#ffffff")

        self.setObjectName('timeout')
        self.resize(280, 110)
        self.setMaximumSize(QtCore.QSize(280, 110))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.late_btn = QtWidgets.QPushButton(self)
        self.late_btn.setGeometry(QtCore.QRect(184, 72, 88, 26))
        self.late_btn.setStyleSheet("alternate-background-color: rgb(65, 70, 255);")
        self.late_btn.setObjectName("late_btn")

        self.confirm_btn = QtWidgets.QPushButton(self)
        self.confirm_btn.setGeometry(QtCore.QRect(114, 72, 62, 26))
        self.confirm_btn.setObjectName("confirm_btn")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 261, 51))
        self.textEdit.setStyleSheet("")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setObjectName("textEdit")

        self.title_lab = QtWidgets.QLabel(self)
        self.title_lab.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.title_lab.setMaximumSize(QtCore.QSize(280, 30))
        self.title_lab.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(192, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.title_lab.setObjectName("title_lab")

        self.confirm_btn.clicked.connect(self.close)
        self.late_btn.clicked.connect(self.late)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "timeout tips"))
        self.late_btn.setText(_translate("Form", "稍后提醒"))
        self.confirm_btn.setText(_translate("Form", "确认"))
        self.title_lab.setText(_translate("Form",
                                          "<html><head/><body><p><span style=\" font-size:18pt; color:#505050;\">A</span><span style=\" color:#505050;\">irmemo</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-color:#000000 \">       %s</p></body></html>") % self.parent().text())

    def late(self):
        self.hide()
        # 调试使用 5秒
        self.late_btn.setText('00:00:05')
        self.parent().set_time()
        self.close()

    def show(self):
        screenSize = QApplication.desktop().screenGeometry()
        x = screenSize.width() - 280 - 15
        y = 30
        super().show()
        platform_name = platform.system()
        if platform_name == 'Darwin':
            self.move(x, y)
        elif platform_name == 'Linux':
            # 暂时没有在linux上开发，不知道可不可以做动画效果
            self.move(x, y)
        elif platform_name == 'Window':
            self.move(screenSize.width())
            for i in range(280 + 15 + 1):
                self.move(screenSize.width() - i, y)
        else:
            self.move(x, y)
