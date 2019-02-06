'''
为qt控件加入所需的方法
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
import logging

class AirLineEdit(QLineEdit):
    # clicked=pyqtSignal()
    #定义clicked信号
    # def mouseReleaseEvent(self, QMouseEvent):
    #     if QMouseEvent.button()==Qt.LeftButton:
    #         self.clicked.emit()
    def focusOutEvent(self, QFocusEvent):
        self.setDisabled(True)

    def focusInEvent(self, QFocusEvent):
        self.setDisabled(False)
    #发送clicked信号
    # def mouseDoubleClickEvent(self, QMouseEvent):
    #     self.setDisabled(True)

class hideButton(QPushButton):
    #flag 为Ture时为展开
    def switch(self,ele,flag):
        try:
            if flag:
                ele.hide()
            else:
                ele.show()
        except Exception as e:
            logging.error(e)

class FramelessWidget(QWidget):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        self.setFixedSize(QSize(400, 400))
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.show()

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
