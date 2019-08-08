import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from py_ui.timeout_tip import *


class remind_timer(QTimer):
    overSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def start(self, sec=1):
        super().start(sec * 1000)
        self.timeout.connect(self.send_tips)

    def send_tips(self):
        '''
        发送超时信号
        :return:
        '''
        print('timeout')
        # 自动销毁
        self.killTimer(self.timerId())
        self.overSignal.emit('timeout')


class time_thread(QThread):
    def __init__(self, parent=None, sec=1):
        super().__init__()
        self.parent = parent
        self.sec = sec

    def run(self):
        self.timer = remind_timer()
        self.timer.start(sec=self.sec)
        self.timer.overSignal.connect(self.free_self)

    def free_self(self, method):
        '''
        释放线程
        :param method: 暂无用处，留待后用
        :return:
        '''
        if method == 'timeout':
            print('get timeout signal')
            Ui_timeout_Dialog(self.parent).show()
            # QMessageBox.information(self.parent, '', '请注意任务<b>%s</b>的交付时间' % self.parent.text(), QMessageBox.Ok)
            self.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)
    top.show()
    s = '123'
    # 3秒后窗口自动关闭
    th = time_thread(parent=top, sec=3)
    th.run()
    sys.exit(app.exec_())
