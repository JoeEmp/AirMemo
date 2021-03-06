'''
为qt控件加入所需的方法
'''
from datetime import datetime
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit, QMenu, QAction, QMessageBox, QDialog, QLabel
from module.note import update_notes, add_notes, delete_note
import config
from comm.operateSqlite import *
import re
from comm.time_thread import time_thread
import time


class AirLineEdit(QLineEdit):
    __eld_text = ''
    __lineSignal = pyqtSignal(str, int)  # 绑定main_win 的 get_update_signal
    update_id_Signal = pyqtSignal(int)

    def __init__(self, main_win, info, parent=None, color='ffffff'):
        super().__init__(parent)
        self.get_reminder(info)
        self.main_win = main_win
        # 绑定槽
        self.__lineSignal.connect(main_win.get_update_Signal)
        self.createContextMenu()
        self.color = color

    def get_reminder(self, info):
        '''
        获取用户的前三条时间
        :param info: 用户信息 {'username':'','token':''}
        :return: None
        '''
        sql = "select time from reminder where username = '%s'  order by sequence limit 3" % info[
            'username']
        ret = sqlite_db.select(sql)
        if not ret['status']:
            logging.error(ret['msg'])
        self.times = ret['records'] if 'records' in ret.keys() else list()
        return None

    def createContextMenu(self):
        ''' 创建右键菜单，菜单的数量没有办法动态控制，wrb'''
        #  必须将ContextMenuPolicy设置为Qt.CustomContextMenu  
        #  否则无法使用customContextMenuRequested信号  
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        #  创建QMenu  
        self.contextMenu = QMenu(self)
        self.contextMenu.setStyleSheet("selection-background-color: blue;")

        self.act_copy = QAction('复制', triggered=self.copy)
        self.act_paste = QAction('粘贴', triggered=self.paste)
        self.act_undo = QAction('撤销', triggered=self.undo)
        self.act_selall = QAction('全选', triggered=self.selectAll)
        self.act_del = QAction('删除该消息', triggered=self.delete_note)
        self.set_reminder0 = QAction(
            self.times[0]['time'], triggered=self.set_time)
        self.set_reminder1 = QAction(
            self.times[1]['time'], triggered=self.set_time)
        self.set_reminder2 = QAction(
            self.times[2]['time'], triggered=self.set_time)

        self.contextMenu.addAction(self.act_copy)
        self.contextMenu.addAction(self.act_paste)
        self.contextMenu.addAction(self.act_undo)
        self.contextMenu.addAction(self.act_selall)
        self.contextMenu.addAction(self.act_del)
        self.contextMenu.addAction(self.set_reminder0)
        self.contextMenu.addAction(self.set_reminder1)
        self.contextMenu.addAction(self.set_reminder2)

    def showContextMenu(self, pos):
        ''' 右键点击时调用的函数 '''
        #  菜单显示前，将它移动到鼠标点击的位置  QtCore.QPoint(95, 20) 20为微调结果
        self.contextMenu.move(pos + self.main_win.pos() + QPoint(95, 20))
        # logging.info(pos+self.main_win.pos()+QPoint(95,20))
        self.contextMenu.show()

    def set_time(self):
        '''
        设置提醒时间
        :return:
        '''
        time = datetime.strptime(self.sender().text(), '%H:%M:%S')
        sec = (time - datetime.strptime('00:00:00', '%H:%M:%S')).seconds
        self.thread = time_thread(parent=self, sec=sec)
        self.thread.run()

    def delete_note(self):
        id = re.findall('\d+', self.objectName())[0]
        if -1 == id:
            QMessageBox.information(
                self, '提示', {}.format('无法删除空数据'), QMessageBox.Ok)
        else:
            delete_note(id)
            self.__lineSignal.emit(self.main_win.user_info['username'], 0)

    def enterEvent(self, *args, **kwargs):
        self.__eld_text = self.text()
        self.setStyleSheet("background:#ffffff")

    def leaveEvent(self, *args, **kwargs):
        # self.setEnabled(False)
        '''
        更新note
        :param args:
        :param kwargs:
        :return:
        '''
        data = {'id': -1, 'message': '', 'username': ''}
        try:
            # 使用 objName 获取id bwrb
            data['id'] = int(self.objectName().replace('note_le', ''))
        except Exception as e:
            logging.warning(e)
        data['message'] = self.text()
        if not data['message']:
            data['message'] != self.__eld_text
        # 插入新的数据
        if data['id'] == -1 and data['message']:
            data['username'] = self.main_win.user_info['username']
            new_id = add_notes(data)['records']['id']
            self.setObjectName('note_le' + str(new_id))
            self.update_id_Signal.emit(new_id)
        # 更新旧的数据
        elif data['message'] != self.__eld_text:
            data['update_time'] = "(datetime(CURRENT_TIMESTAMP, 'localtime') )"
            update_notes(data, 'message',
                         username=self.main_win.user_info['username'])
        self.setStyleSheet("background:#%s" % self.color)


class AirTextEdit(QTextEdit):
    __eld_text = ''

    def __init__(self, main_win, parent=None, color='ffffff'):
        self.main_win = main_win
        super().__init__(parent)
        self.color = color

    def enterEvent(self, *args, **kwargs):
        self.__eld_text = self.toPlainText()
        # self.setEnabled(True)
        self.setStyleSheet('background:#ffffff')

    def leaveEvent(self, *args, **kwargs):
        '''
        更新detail
        :param args:
        :param kwargs:
        :return:
        '''
        # self.setEnabled(False)
        data = {'id': -1, 'detail': ''}
        try:
            # 使用 objName 获取id bwrb
            data['id'] = int(self.objectName().replace('detail_tx', ''))
        except Exception as e:
            logging.warning(e)
        data['detail'] = self.toPlainText()
        # 更新数据库
        if data['detail'] != self.__eld_text:
            update_notes(data, 'detail',
                         username=self.main_win.user_info['username'])
        self.setStyleSheet('background:#%s' % self.color)


class hideButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.flag = 0

    # flag 为Ture时为展开
    def switch(self, ele, flag):
        try:
            if flag:
                ele.hide()
            else:
                ele.show()
        except Exception as e:
            logging.error(e)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)
        painter = QPainter(self)
        pix = QPixmap()
        pix.load(config.LEFT_ICON)
        painter.translate(50, 50)  # 让图片的中心作为旋转的中心
        painter.rotate(90)  # 顺时针旋转90度
        painter.translate(-50, -50)  # 使原点复原
        painter.drawPixmap(0, 0, 100, 100, pix)


'''
class color_sider(QSlider):
    def printEvent(self):
        painter=QPrinter(self)
        painter.setRenderHint(QPainter.a, true)
        Linear=QLinearGradient(100, 100, 100, 200) # 垂直渐变

        Linear.setColorAt(0, QColor=QColor.red())
        Linear.setColorAt(1, QColor.blue())

        painter.setBrush(Linear)
        painter.setPen(Qt::transparent)
        painter.drawRect(100, 100, 100, 100)
'''
