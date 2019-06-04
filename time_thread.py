import datetime
import logging

import sys
from PyQt5.QtWidgets import QApplication, QWidget

import config
from PyQt5.QtCore import QThread, pyqtSignal,QTimer


class TimeThread(QThread):
    trigger = pyqtSignal()
    _sec = 0

    def __init__(self,time,parent=None):
        super().__init__(parent)
        try:
            # self.text = parent.text()
            time = datetime.datetime.strptime(time,'%H:%M:%S')
            self.sec = (time-datetime.datetime.strptime('00:00:00','%H:%M:%S')).seconds
        except Exception as e:
            logging.warning(e)

    def run(self):
        timer = QTimer()
        timer.timeout.connect(time_out_tips)
        timer.start(self.sec)
        # # 循环完毕后发出信号
        # self.trigger.emit()


def time_out_tips(self):
    print('时间到了')
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)
    top.show()
    s= '123'
    th = TimeThread(time='00:00:02',parent=top)
    th.start()
    sys.exit(app.exec_())
