# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/timeout_tip.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(280, 110)
        Form.setMaximumSize(QtCore.QSize(280, 110))
        Form.setBaseSize(QtCore.QSize(280, 95))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.late_btn = QtWidgets.QPushButton(Form)
        self.late_btn.setGeometry(QtCore.QRect(180, 70, 94, 35))
        self.late_btn.setStyleSheet("alternate-background-color: rgb(65, 70, 255);")
        self.late_btn.setObjectName("late_btn")
        self.confirm_btn = QtWidgets.QPushButton(Form)
        self.confirm_btn.setGeometry(QtCore.QRect(110, 70, 68, 35))
        self.confirm_btn.setObjectName("confirm_btn")
        self.title_lab = QtWidgets.QLabel(Form)
        self.title_lab.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.title_lab.setMaximumSize(QtCore.QSize(280, 30))
        self.title_lab.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(192, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.title_lab.setObjectName("title_lab")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 261, 51))
        self.textEdit.setStyleSheet("")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        self.confirm_btn.clicked['bool'].connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.late_btn.setText(_translate("Form", "稍后提醒"))
        self.confirm_btn.setText(_translate("Form", "确认"))
        self.title_lab.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#505050;\">A</span><span style=\" color:#505050;\">irmemo</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-color:#000000 \">       野太第点队国争完吃不的教快感所东者不阶屋也导神门马习员完车有</p></body></html>"))


