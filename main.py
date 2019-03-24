import sys
from UI.main_win import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import ctypes
from utils import setApp
from PyQt5.QtCore import Qt
from UI.AirTray import AirTray

if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("AirMemo_appid")
    app = QApplication(sys.argv)
    setApp(app)
    tray = AirTray()
    mainWindow = Ui_MainWindow(tray)
    dict = {'main_win':mainWindow}
    tray.set_menu(dict)
    tray.show()
    mainWindow.show()
    sys.exit(app.exec_())