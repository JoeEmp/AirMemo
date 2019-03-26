'''
为qt控件加入所需的方法
'''
import os

from PyQt5.QtCore import QCoreApplication,Qt,QPoint, pyqtSignal
from PyQt5.QtGui import QIcon, QCursor, QMouseEvent
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit, QSystemTrayIcon, \
    QMenu, QAction, QDialog, QMessageBox
import logging
from utils import update_records, add_records,delete_records,check_login_state
import config
import re

class AirLineEdit(QLineEdit):
    __eld_text = ''
    __lineSignal = pyqtSignal(str,int)

    def __init__(self, main_win,parent=None):
        super().__init__(parent)
        self.createContextMenu()
        self.main_win = main_win
        # 绑定槽
        self.__lineSignal.connect(main_win.get_update_Signal)

    def createContextMenu(self):
        ''' 
        创建右键菜单 
        '''
        #  必须将ContextMenuPolicy设置为Qt.CustomContextMenu  
        #  否则无法使用customContextMenuRequested信号  
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        #  创建QMenu  
        self.contextMenu = QMenu(self)

        self.act_copy = QAction('复制',triggered = self.copy)
        self.act_paste = QAction('粘贴',triggered = self.paste)
        self.act_undo = QAction('撤销',triggered = self.undo)
        self.act_selall = QAction('全选',triggered = self.selectAll)
        self.act_del = QAction('删除该消息',triggered = self.delete_record)

        self.contextMenu.addAction(self.act_copy)
        self.contextMenu.addAction(self.act_paste)
        self.contextMenu.addAction(self.act_undo)
        self.contextMenu.addAction(self.act_selall)
        self.contextMenu.addAction(self.act_del)

    def showContextMenu(self,pos):
        ''' 
        右键点击时调用的函数 
        '''
        #  菜单显示前，将它移动到鼠标点击的位置  QtCore.QPoint(0, 20) 20为微调结果
        self.contextMenu.move(pos+self.main_win.pos()+QPoint(95,20))
        print(pos+self.main_win.pos()+QPoint(95,20))
        self.contextMenu.show()

    def delete_record(self):
        id = re.findall('\d+',self.objectName())[0]
        filter_list = [
                ['id','=',id]
                           ]
        if delete_records(config.LDB_FILENAME,filer_list=filter_list) == 0:
            QMessageBox.information(self,'提示',{}.format('无法删除空数据'))
        else:
            # 期望不删除预设数据 未实现 wrb
            self.__lineSignal.emit(self.main_win.user_info['username'],0)

    def enterEvent(self, *args, **kwargs):
        self.__eld_text = self.text()
        self.setEnabled(True)

    def leaveEvent(self, *args, **kwargs):
        # self.setEnabled(False)
        data = {'id': -1, 'text': self.text(), 'col': 'message'+','+'username'}
        try:
            # 使用 objName 获取id bwrb
            data['id'] = int(self.objectName().replace('note_le', ''))
        except Exception as e:
            print(e)
        data['text'] = self.text()
        # 插入新的数据
        if data['id'] == -1 and data['text']:
            # print(data)
            username = self.main_win.user_info['username']
            data['text'] = self.text()+"','"+username
            new_id = add_records(config.LDB_FILENAME, data)
            self.setObjectName('note_le' + str(new_id))
        # 更新旧的数据
        elif data['text'] != self.__eld_text:
            update_records(config.LDB_FILENAME, data, self.objectName())


class AirTextEdit(QTextEdit):
    __eld_text = ''

    def enterEvent(self, *args, **kwargs):
        self.__eld_text = self.toPlainText()
        self.setEnabled(True)

    def leaveEvent(self, *args, **kwargs):
        self.setEnabled(False)
        data = {'id': -1, 'text': '', 'col': 'detail'}
        try:
            # 使用 objName 获取id bwrb
            data['id'] = int(self.objectName().replace('detail_tx', ''))
        except Exception as e:
            print(e)
        data['text'] = self.toPlainText()
        # 更新数据库
        if data['text'] != self.__eld_text:
            update_records(config.LDB_FILENAME, data, self.objectName())


class hideButton(QPushButton):
    # flag 为Ture时为展开
    def switch(self, ele, flag):
        try:
            if flag:
                ele.hide()
            else:
                ele.show()
        except Exception as e:
            logging.error(e)


