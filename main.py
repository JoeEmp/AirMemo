import ctypes
import sys

# from PyQt5.QtWidgets import QApplication
from py_ui.AirTray import AirTray
from py_ui.main_win import *
from py_ui.demo import *
from utils import setApp
from PyQt5.QtCore import QSharedMemory
from PyQt5.QtNetwork import QLocalServer,QLocalSocket


def main():
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("AirMemo_appid")
    app = QApplication(sys.argv)

    serverName = 'AirMemo_client'
    socket = QLocalSocket()
    socket.connectToServer(serverName)
    
    # 如果连接成功，表明server已经存在，当前已有实例在运行
    if socket.waitForConnected(500):
        sys.exit(app.quit())
    
    # 没有实例运行，创建服务器   
    localServer = QLocalServer()     
    localServer.listen(serverName)
    try:
        setApp(app)
        tray = AirTray()
        mainWindow = Ui_MainWindow(tray)
        setting_win = Ui_Settings(tray)
        dict = {'main_win': mainWindow, 'setting_win': setting_win}
        tray.set_menu(dict)
        tray.show()
        mainWindow.show()
        sys.exit(app.exec_())
    finally:
        localServer.close() 

if __name__ == '__main__':
    main()