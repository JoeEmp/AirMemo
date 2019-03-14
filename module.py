from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory,QDialog
import sqlite3
import config
import logging
import requests

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


def update_records(filename, data,ele):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        if data['id'] != -1:
            c.execute("update  Msg set %s='%s' WHERE id=%d;"%(data['col'],data['text'],data['id']))
            logging.info('%s update record successfully!!!'%str(ele))
            db.commit()
            return True
    except Exception as e:
        print('update error')
        print(e)
        return False


def add_records(filename,data):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        if data['id'] == -1:
            # print("insert into Msg (%s) VALUES (%s)"%(data['col'],data['text']))
            c.execute("insert into Msg (%s) VALUES ('%s')"%(data['col'],data['text']))
            db.commit()
            logging.info('add records done')
            return len(get_records(config.LDB_FILENAME))+1
    except Exception as e:
        print('add error ',data)
        print(e)
        return -1

# 根据系统返回天数删除软删除记录
def clear_records(filename, Severdate):
    db = sqlite3.connect(filename)
    c = db.cursor()
    cur = c.execute("delete from Msg where del_time<strftime('yyyy-mm-dd',%s);" % Severdate)
    db.commit()
    logging.info('clear done')


def remove_note():
    pass


def get_index(dict,keys):
    if not keys or not dict:
        return None
    index_list=[]
    for key in keys:
        try:
            index_list.append(list(dict.keys()).index(key))
        except Exception as e:
            print(e)
    return index_list


def login(username,password):
    protocol = 'http://'
    dev_url = '127.0.0.1:5000/login'
    env_url = '149.129.125.8/login'
    data={'username':username,'password':password}
    r=requests.post(protocol + dev_url,data=data)
    print(r.text)

def login_state():
    return 2

if __name__ == '__main__':
    pass
    # dbName = r'AirMemo.db'
    # # add_records(dbName)
    # print(get_records(dbName))
    # # clear_records(filename=dbName,Severdate='2019-01-05')
    # print(get_records(dbName))