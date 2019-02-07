import sys
from UI.main_win import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import ctypes
from module import setApp
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    app = QApplication(sys.argv)
    setApp(app)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())