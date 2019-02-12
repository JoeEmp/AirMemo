'''
为qt控件加入所需的方法
'''
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton,QLineEdit,QTextEdit,QSystemTrayIcon, \
    QMenu, QAction,QDialog, QMessageBox
import logging
# from UI.settings import settings_Dialog
from module import update_records
import config
import re

class AirLineEdit(QLineEdit):
    __eld_text=''

    def enterEvent(self, *args, **kwargs):
        self.__eld_text=self.text()
        self.setEnabled(True)

    def leaveEvent(self, *args, **kwargs):
        # self.focusInEvent()
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
    widget=None

    def __init__(self,widget):
        super().__init__(widget)
        self.widget=widget
        self.set_menu()
        self.set_icon()
        self.show()

    def set_menu(self):
        self.main_menu=QMenu()
        self.show_action=QAction('&show',triggered=self.widget.show)
        self.settings_action=QAction('&settings',triggered=QDialog.show)
        self.quit_action=QAction('&exit',triggered=self.quitapp)

        self.main_menu.addAction(self.show_action)
        self.main_menu.addAction(self.settings_action)
        self.main_menu.addAction(self.quit_action)
        self.setContextMenu(self.main_menu)
        pass

    def set_icon(self):
        self.setIcon(QIcon('./UI/app_icon.png'))
        pass

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        print(reason)

    def quitapp(self):
        self.parent().show() # w.hide() #隐藏
        sel = QMessageBox.question(self.widget, "提示", "确定要退出Airmemo", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if sel == QMessageBox.Yes:
            QCoreApplication.instance().quit()
            # 在应用程序全部关闭后，TrayIcon其实还不会自动消失，
            # 直到你的鼠标移动到上面去后，才会消失，
            # 这是个问题，（如同你terminate一些带TrayIcon的应用程序时出现的状况），
            # 这种问题的解决我是通过在程序退出前将其setVisible(False)来完成的。
            self.setVisible(False)
