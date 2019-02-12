from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)


# 返回等分字典
def getSize(divide):
    sizeDict = {}
    screenSize = QApplication.desktop().screenGeometry()
    sizeDict['width'] = (screenSize.width() / divide['width'])
    # sizeDict['height']=(screenSize.heigth()/divide['height'])
    return sizeDict


# 设置app
def setApp(app):
    app.setStyle(QStyleFactory.create('Fusion'))
    # 关闭所有窗口,也不关闭应用程序
    QApplication.setQuitOnLastWindowClosed(False)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./ui/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    app.setWindowIcon(QIcon('./ui/app_icon.png'))

def get_records(filename, filter=None):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        if filter == None:
            cur = c.execute('SELECT * FROM Msg WHERE is_del=0;')
        else:
            # sql="select %s,%s from Msg where is_del=0;"%(for s in filter)
            pass
    except Exception as e:
        logging.error(e)
    return cur.fetchall()

def update_records(filename, data):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        if data['id'] != -1:
            c.execute("update  Msg set %s='%s' WHERE id=%d;"%(data['col'],data['text'],data['id']))
            logging.info('update record successfully!!!')
            db.commit()
            return True
    except Exception as e:
        print(e)
        return False

def add_records(filename):
    db = sqlite3.connect(filename)
    c = db.cursor()
    logging.info('link db successfully')
    for i in range(2, 4):
        cur = c.execute("insert into Msg(id, Message) VALUES(%d,'123')" % i)
    db.commit()
    logging.info('done')

# 根据系统返回天数删除软删除记录
def clear_records(filename, Severdate):
    db = sqlite3.connect(filename)
    c = db.cursor()
    cur = c.execute("delete from Msg where del_time<strftime('yyyy-mm-dd',%s);" % Severdate)
    db.commit()
    logging.info('clear done')


if __name__ == '__main__':
    pass
    dbName = r'AirMemo.db'
    # add_records(dbName)
    print(get_records(dbName))
    # clear_records(filename=dbName,Severdate='2019-01-05')
    print(get_records(dbName))
