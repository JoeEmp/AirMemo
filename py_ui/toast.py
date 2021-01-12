from PyQt5 import QtCore, QtQuickWidgets, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QColor
import logging


class Toast(object):
    """
    Toast控件
    """
    long = 2000
    short = 1000

    def __init__(self, parent, qml=''):
        """
        初始化widget
        :param parent: 显示窗口
        :param qml: 具体加载的qml 默认为 'py_ui/toast.qml'
        """
        self.toast = QtQuickWidgets.QQuickWidget(parent)
        # 设置为透明和允许显示
        self.toast.setClearColor(QColor(Qt.transparent))
        self.toast.setAttribute(Qt.WA_AlwaysStackOnTop)
        self.parent = parent
        if not qml:
            qml = 'py_ui/toast.qml'
        self.toast.setSource(QUrl(qml))
        # widget是透明的，可以先设置状态
        self.show()

    def show(self):
        self.toast.show()

    def show_toast(self, text, time=short, height=0.8):
        """
        :param text: 显示文本
        :param time: 显示时长(单位 ms)
        :param height: parent内的显示高度(默认居中)
        """
        try:
            self.set_time(time)
            self.toast.rootObject().set_text(text)
            self.toast.move(int((self.parent.width() - self.width()) / 2),
                            int(self.parent.height() * height))
            self.toast.rootObject().show_toast()
        except Exception as e:
            logging.error(e)

    def width(self):
        try:
            return self.toast.rootObject().width()
        except Exception as e:
            logging.error(e)
            return 5

    def rootObject(self):
        return self.toast.rootObject()

    def set_time(self, time):
        """
        设置显示时间
        :param time: 单位为毫秒
        :return:
        """
        if isinstance(time, int):
            self.toast.rootObject().set_time(time)
        else:
            self.toast.rootObject().set_time(self.short)
            logging.warning('time类型不对 {}'.format(type(time)))
