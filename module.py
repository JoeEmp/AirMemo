from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory, QDialog
import sqlite3
import config
import logging
import requests
from utils import be_sql, exec_sql

protocol = 'http://'
local_host = '127.0.0.1:5000'
pro_host = '149.129.125:5000'
user_host = local_host


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
    icon.addPixmap(QtGui.QPixmap("./ui/app_icon.png"), QtGui.QIcon.Normal,
                   QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    app.setWindowIcon(QIcon('./ui/app_icon.png'))


# 查询当前用户的笔记
def get_records(filename, username='visitor'):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        table = 'msg'
        filter_list = [
            ['username', '=', username],
            ['is_del', '=', '0']
        ]
        sql = be_sql().sel_sql(table, filter_list=filter_list)
        # print(sql)
        cur = c.execute(sql)
    except Exception as e:
        logging.error(e)
    return cur.fetchall()


# 更新数据 wrb
def update_records(filename, data, ele):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        if data['id'] != -1:
            c.execute("update  Msg set %s='%s' WHERE id=%d;" % (
                data['col'], data['text'], data['id']))
            logging.info('%s update record successfully!!!' % str(ele))
            db.commit()
            return True
    except Exception as e:
        print('update error')
        print(e)
        return False


# 添加数据 wrb 更改会影响 增加逻辑
def add_records(filename, data):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        if data['id'] == -1:
            # print("insert into Msg (%s) VALUES (%s)"%(data['col'],data['text']))
            c.execute("insert into Msg (%s) VALUES ('%s')" % (
                data['col'], data['text']))
            db.commit()
            logging.info('add records done')
            return len(get_records(config.LDB_FILENAME)) + 1
    except Exception as e:
        logging.error('add error ', data)
        print(e)
        return -1


# 根据系统返回天数删除软删除记录
def clear_records(filename, Severdate):
    db = sqlite3.connect(filename)
    c = db.cursor()
    cur = c.execute(
            "delete from Msg where del_time<strftime('yyyy-mm-dd',%s);" % Severdate)
    db.commit()
    logging.info('clear done')

# 未实现
def remove_note():
    pass


def get_index(dict, keys):
    if not keys or not dict:
        return None
    index_list = []
    for key in keys:
        try:
            index_list.append(list(dict.keys()).index(key))
        except Exception as e:
            print(e)
    return index_list


def login(username, password):
    url = '/login'
    data = {'username': username, 'password': password}
    r = requests.post(protocol + user_host + url, data=data)
    return r.json()


def login_state():
    # 检查本地token
    result = check_login_state()
    # 本地无用户登录
    if not result:
        return {'state': 1}
    # 本地有token的用户去服务器校验
    else:
        result = result[0]
        try:
            url = '/check_login'
            headers = {
                'User-Agent': 'AirMemo'
            }
            data = {'username': result[0], 'token': result[1]}
            r = requests.post(protocol + user_host + url, headers=headers,
                              data=data)
        except Exception as e:
            logging.error(e)
            return {'state': -1, 'errMsg': '无法连接服务器'}
        try:
            state = r.json()
        except Exception as e:
            logging.error(e)
            return {'errMsg': '接口返回数据出错'}
    # print(state)
    return state


def check_login_state():
    table = 'user'
    need_col_list = ['username', 'token']
    filter_list = [['token', 'is not', 'NULL']]
    sql = be_sql().sel_sql(table, need_col_list, filter_list)
    return exec_sql(config.LDB_FILENAME, sql)


if __name__ == '__main__':
    pass
    # dbName = r'AirMemo.db'
    # # add_records(dbName)
    # print(get_records(dbName))
    # # clear_records(filename=dbName,Severdate='2019-01-05')
    # print(get_records(dbName))
