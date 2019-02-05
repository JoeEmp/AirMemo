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
    ui = Ui_MainWindow()
    mainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    mainWindow.setStyleSheet('QMainWindow{background-image:url(e:/Python/Python36/AirMemo/UI/bg.png);}')
    ui.setUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())