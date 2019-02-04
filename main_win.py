import sys
from UI.main import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import ctypes
from module import setApp

if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    app = QApplication(sys.argv)
    setApp(app)
    mainWindow = QMainWindow()
    # mainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    ui = Ui_MainWindow()
    ui.setUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())