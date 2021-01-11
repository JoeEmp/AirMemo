import sys
from comm.operateSqlite import link_db
from py_ui.AirTray import AirTray
from py_ui.main_win import *
from py_ui.settings import *
from comm.utils import setApp
from PyQt5.QtNetwork import QLocalServer, QLocalSocket
import config
from comm.user_cache import mine

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
        link_db(config.LDB_FILENAME)
        tray = AirTray()
        mainWindow = Ui_MainWindow(tray)
        setting_win = Ui_Settings(tray)
        dict = {'main_win': mainWindow, 'setting_win': setting_win}
        tray.set_menu(dict)
        tray.show()
        # mainWindow.show()
        setting_win.show()
        sys.exit(app.exec_())
    finally:
        localServer.close()

if __name__ == '__main__':
    main()
