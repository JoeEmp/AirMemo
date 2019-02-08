'''
为qt控件加入所需的方法
'''

from PyQt5.QtWidgets import QPushButton,QLineEdit,QTextEdit,QSystemTrayIcon, \
    QMenu, QAction
import logging
from UI.settings import settings_Dialog
from module import update_records
import config

class AirLineEdit(QLineEdit):
    __eld_text=''

    def enterEvent(self, *args, **kwargs):
        self.__eld_text=self.text()
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
        if data['text'] != self.__eld_text:
            update_records(config.LDB_FILENAME,data)

class AirTextEdit(QTextEdit):
    __eld_text=''

    def enterEvent(self, *args, **kwargs):
        self.__eld_text=self.toPlainText()
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
        if data['text'] != self.__eld_text:
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

class AirTray(QSystemTrayIcon):

    def __init__(self,*__args):
        super().__init__()

    def set_menu(self,widget):
        self.main_menu=QMenu()
        self.show_action=QAction('&show',tritriggered=widget.show)
        self.settings_action=QAction('&settings',tritriggered=settings_Dialog())
        self.quit_action=QAction('&exit',tritriggered=self.quit)
        pass

    def set_icon(self):

        pass

    def quit(self,widget):
        pass