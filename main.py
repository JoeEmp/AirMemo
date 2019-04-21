import ctypes
import sys

from PyQt5.QtWidgets import QApplication
from py_ui.AirTray import AirTray
from py_ui.main_win import *

from utils import setApp

if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("AirMemo_appid")
    app = QApplication(sys.argv)
    setApp(app)
    tray = AirTray()
    mainWindow = Ui_MainWindow(tray)
    setting_win = 1
    dict = {'main_win': mainWindow, 'setting_win': setting_win}
    tray.set_menu(dict)
    tray.show()
    mainWindow.show()
    sys.exit(app.exec_())
