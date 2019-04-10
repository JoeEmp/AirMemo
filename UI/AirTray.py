import logging

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction, QDialog, \
    QMessageBox

from utils import check_login_state, get_records

class AirTray(QSystemTrayIcon):
    widget = None
    __user_info = {}

    def __init__(self, widget_dict=None):
        super().__init__()
        self.set_data()
        self.show()

    def set_menu(self, widget_dict):
        self.widget_dict = widget_dict
        self.main_menu = QMenu()
        self.show_action = QAction('&show',
                                   triggered=self.widget_dict['main_win'].show)
        self.settings_action = QAction('&settings', triggered=QDialog.show)
        self.quit_action = QAction('&exit', triggered=self.quitapp)

        self.main_menu.addAction(self.show_action)
        self.main_menu.addAction(self.settings_action)
        self.main_menu.addAction(self.quit_action)

        self.set_icon()

        self.setContextMenu(self.main_menu)

    def set_icon(self):
        # 这里的路径从main.py 算起
        self.setIcon(QIcon('./UI/app_icon.png'))
        pass

    def set_data(self):
        self.__user_info = self.check()
        self.set_icon()

    # 获取 username 以及 token ，默认为 'visitor'
    def check(self):
        result = check_login_state()
        if result:
            return {'username': result[0][0], 'token': result[0][1]}
        else:
            return {'username': 'visitor', 'token': ''}

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        print(reason)

    def get_info(self):
        return self.__user_info

    def update_info(self):
        self.__user_info = self.check()

    def quitapp(self):
        try:
            self.widget_dict['main_win'].show()
            sel = QMessageBox.question(self.widget_dict['main_win'], "提示", "确定要退出Airmemo",
                                       QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
            if sel == QMessageBox.Yes:
                self.widget_dict['main_win'].close()
                QCoreApplication.instance().quit()
                # 在应用程序全部关闭后，TrayIcon其实还不会自动消失，
                # 直到你的鼠标移动到上面去后，才会消失，
                # 这是个问题，（如同你terminate一些带TrayIcon的应用程序时出现的状况），
                # 这种问题的解决我是通过在程序退出前将其setVisible(False)来完成的。
                self.setVisible(False)
        except Exception as e:
            logging.error(e)
