import sys
from UI.main_win import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import ctypes
from utils import setApp
from PyQt5.QtCore import Qt
from UI.AirTray import AirTray
from UI.settings import Ui_Settings

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
