'''
为qt控件加入所需的方法
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

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