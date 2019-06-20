# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/new_recycle.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidgetItem, QDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 370)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 280, 350))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        for i in range(2):
            item = QListWidgetItem()
            item.setSizeHint(QSize(10, 40))
            self.listWidget.addItem(item)

            # 设置item布局
            itemWidget = QtWidgets.QWidget()
            itemWidget.setGeometry(QtCore.QRect(40, 190, 231, 51))
            itemWidget.setObjectName("itemWidget")
            item_verticalLayout = QtWidgets.QVBoxLayout(itemWidget)
            item_verticalLayout.setContentsMargins(0, 0, 0, 0)
            item_verticalLayout.setObjectName("item_verticalLayout")
            message_check = QtWidgets.QCheckBox(itemWidget)
            message_check.setObjectName("message_check")
            message_check.setText('message')
            item_verticalLayout.addWidget(message_check)
            detail_sub_lab = QtWidgets.QLabel(itemWidget)
            detail_sub_lab.setObjectName("detail_sub_lab")
            detail_sub_lab.setText('detail')
            item_verticalLayout.addWidget(detail_sub_lab)

            self.listWidget.setItemWidget(item, itemWidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.restore_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.restore_btn.setObjectName("restore_btn")
        self.horizontalLayout.addWidget(self.restore_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "回收站"))
        self.restore_btn.setText(_translate("Dialog", "还原"))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dlg = QDialog()
    Ui_Dialog().setupUi(dlg)
    dlg.show()
    app.exec_()
