import hashlib

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory, QDialog
import sqlite3
import config
import logging
import requests
from operateSqlite import be_sql, exec_sql

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
def get_records(filename, username='visitor',is_del='0'):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        table = 'msg'
        filter_list = [
            ['username', '=', username],
            ['is_del', '=', is_del]
        ]
        sql = be_sql().sel_sql(table, filter_list=filter_list)
        # print(sql)
        cur = c.execute(sql)
    except Exception as e:
        logging.error(e)
    return cur.fetchall()


# 更新数据 wrb 更改会影响 修改逻辑
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
        logging.error('add error ')
        logging.error("insert into Msg (%s) VALUES ('%s')" % (
                data['col'], data['text']))
        print(e)
        return -1


# 软删除 数据
def delete_records(filename, filer_list):
    table = 'Msg'
    sql = be_sql().update_sql(table=table, value_dict={'is_del': '1'},
                              filter_list=filer_list)
    print(sql)
    return exec_sql(filename, sql, is_update=1)


# 根据系统返回天数删除软删除记录
def clear_records(filename, sever_date):
    db = sqlite3.connect(filename)
    c = db.cursor()
    cur = c.execute(
            "delete from Msg where del_time<strftime('yyyy-mm-dd',%s);" % sever_date)
    db.commit()
    logging.info('clear done')


# 获取用户信息
def get_user_info(table, username):
    filter_list = [['username', '=', username]]
    sql = be_sql().sel_sql(table, filter_list=filter_list)
    return exec_sql(config.LDB_FILENAME, sql)


# 获取索引
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
    headers = {
        'User-Agent': 'AirMemo'
    }
    cryptograph_password()
    data = {'username': username, 'password': cryptograph_password(password)}
    r = requests.post(protocol + user_host + url, headers=headers, data=data)
    print(r.json())
    return r.json()


# wrb
def get_login_state():
    '''
    查询 服务器的登录状态
    :return:
    '''
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


# wrb  目标将 list 转成 dict 本地状态
def check_login_state():
    '''
    查找token非空的人
    :return: 查询结果 结构[(username,token)]
             无查询结果时 结构为[]
    '''
    table = 'user'
    need_col_list = ['username', 'token']
    filter_list = [['token', 'is not', 'NULL']]
    sql = be_sql().sel_sql(table, need_col_list, filter_list)
    return exec_sql(config.LDB_FILENAME, sql)


# wrb after check_login
def logout(username):
    '''
    :return:
    '''
    result = check_login_state()
    print(result)
    try:
        if result:
            result = result[0]
            url = '/logout'
            headers = {
                'User-Agent': 'AirMemo'
            }
            data = {'username': username, 'token': result[1]}
            r = requests.post(protocol + user_host + url, headers=headers,
                              data=data)
            return r.json()
    except Exception as e:
        logging.error(e)
        return {'state': '-1'}


# 同login
def register(username, password):
    url = '/register'
    headers = {
        'User-Agent': 'AirMemo'
    }
    data = {'username': username, 'password': password}
    r = requests.post(protocol + user_host + url, headers=headers, data=data)
    return r.json()


# 产生密文密码
def cryptograph_password(password):
    if password:
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        cryptograph = m.hexdigest()
    else:
        cryptograph = None
    return cryptograph

if __name__ == '__main__':
    pass
    # dbName = r'AirMemo.db'
    # # add_records(dbName)
    # print(get_records(dbName))
    # # clear_records(filename=dbName,Severdate='2019-01-05')
    # print(get_records(dbName))
    filter_list = [
        ['id', '=', str(-1)]
    ]
    ret = delete_records(config.LDB_FILENAME, filter_list)
    print(ret)

    print([] is None)
