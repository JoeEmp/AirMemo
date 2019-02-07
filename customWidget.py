'''
为qt控件加入所需的方法
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow,QPushButton,QLineEdit,QTextEdit
import logging
from module import update_records
import config

class AirLineEdit(QLineEdit):


    def enterEvent(self, *args, **kwargs):
        self.setEnabled(True)

    def leaveEvent(self, *args, **kwargs):
        self.setEnabled(False)
        data={'id':-1,'text':'','col':'message'}
        try:
            #使用 objName 获取id bwrb
            data['id']=int(self.objectName().replace('note_le',''))
        except Exception as e:
            print(e)
        data['text']=self.text()
        update_records(config.LDB_FILENAME,data)

class AirTextEdit(QTextEdit):


    def enterEvent(self, *args, **kwargs):
        self.setEnabled(True)

    def leaveEvent(self, *args, **kwargs):
        self.setEnabled(False)
        data={'id':-1,'text':'','col':'detail'}
        try:
            #使用 objName 获取id bwrb
            data['id']=int(self.objectName().replace('detail_tx',''))
        except Exception as e:
            print(e)
        data['text']=self.toPlainText()
        update_records(config.LDB_FILENAME,data)

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
