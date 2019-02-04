'''
为qt控件加入所需的方法
'''

from PyQt5.QtCore import *
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

# class frameWidget(QWidget):
#
#     def