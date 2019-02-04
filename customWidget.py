'''
为qt控件加入所需的方法
'''

from PyQt5.QtWidgets import *

class AirLineEdit(QLineEdit):
    def focusOutEvent(self, QFocusEvent):
        self.setDisabled(True)

    def focusInEvent(self, QFocusEvent):
        self.setDisabled(False)