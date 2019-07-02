from PyQt5.QtWidgets import QWidget
from operateSqlite import be_sql, exec_sql
import config
from utils import cryptograph_password, protocol, user_host
import requests
import logging


def get_notes(filename, username='visitor', is_del='0'):
    '''
    查询当前用户的笔记
    :param filename: sqlite3文件名
    :param username: 用户名
    :param is_del:   是否删除，默认为否
    :return: list of dict 异常直接返回空列表
    '''
    try:
        table = 'msg'
        filter_list = [
            ['username', '=', username],
            ['is_del', '=', is_del]
        ]
        if is_del == 'all':
            filter_list.pop()
        sql = be_sql().sel_sql(table, filter_list=filter_list)
        # print(sql)
        cur = exec_sql(filename, sql)
    except Exception as e:
        logging.error(e)
        return []
    return cur


def update_notes(filename, data, ele):
    '''
    更新内容
    :param filename:
    :param data:
    :param ele: 元素(如 note_le,detail_tx)
    :return:
    '''
    try:
        if data['id'] != -1:
            filter_list = [
                ['id', '=', str(data['id'])]
            ]
            sql = be_sql().update_sql('Msg', {ele: data[ele]}, filter_list)
            cur = exec_sql(filename, sql)
            logging.info('%s update No.%s record successfully!!!' % (ele, data['id']))
            return cur
    except Exception as e:
        print('update error')
        print(e)
        return None


def add_notes(filename, data):
    '''
    添加数据 更改会影响 增加逻辑 延后重构 wrb
    :param filename: sqlit3文件名
    :param data:  dict {'id':-1,'{ele}':'','ussername':''}
    :return:
    '''
    sql = ''
    try:
        if data['id'] == -1:
            del data['id']
            sql = be_sql().ins_sql('Msg', data)
            exec_sql(filename, sql)
            logging.info('add records done')
            return len(exec_sql(filename, 'select * from Msg')) - 1
    except Exception as e:
        logging.error('add error ', ending='\t')
        logging.error(sql)
        print(e)
        return -1


def delete_notes(filename, filter_list):
    return change_del_flag(filename, filter_list)


def restore_note(filename, filter_list):
    return change_del_flag(filename, filter_list, is_del=0)


def change_del_flag(filename, filter_list, is_del=1):
    '''
    软删除数据
    :param filename:
    :param filer_list:
    :return:
    '''
    table = 'Msg'
    sql = be_sql().update_sql(table=table, value_dict={'is_del': str(is_del)},
                              filter_list=filter_list)
    # print(sql)
    return exec_sql(filename, sql, is_update=1)


def clear_notes(filename, sever_date):
    '''
    根据系统返回天数物理删除记录
    :param filename:
    :param sever_date:
    :return:
    '''
    try:
        exec_sql(filename, ("delete from Msg where del_time<strftime('yyyy-mm-dd',%s);" % sever_date))
        logging.info('clear done')
    except Exception as e:
        print("clear error")
        logging.warning(e)


def login(username, password):
    '''
    客户端登录请求
    :param username:
    :param password:
    :return:
    '''
    url = '/api/login'
    headers = {
        'User-Agent': 'AirMemo'
    }
    # cryptograph_password()
    data = {'username': username, 'password': cryptograph_password(password)}
    try:
        r = requests.post(protocol + user_host + url, headers=headers, data=data)
        return r.json()
    except Exception as e:
        logging.warning(e)
        return {}


def get_login_state():
    '''
    查询用户在 服务器 的登录状态
    :return:
    '''
    # 检查本地token
    result = check_login_state()
    # 本地无用户登录
    if not result:
        return {'state': 1}
    # 本地有token的用户去服务器校验
    else:
        try:
            url = '/api/check_login'
            headers = {
                'User-Agent': 'AirMemo'
            }
            data = result[0]
            r = requests.post(protocol + user_host + url, headers=headers,
                              data=data)
        except Exception as e:
            logging.error(e)
            return {'state': -1, 'errMsg': '无法连接服务器'}
        try:
            print(r)
            state = r.json()
        except Exception as e:
            logging.error(e)
            return {'state': -1,'errMsg': '接口返回数据出错-%s'%r.status_code}
    # print(state)
    return state


def check_login_state():
    '''
    查找 本地 token非空的人
    :return: 查询结果 结构[{'username':'','token':''}]
             无查询结果时 结构为[]
    '''
    table = 'user'
    need_col_list = ['username', 'token']
    filter_list = [['token', 'is not', 'NULL']]
    sql = be_sql().sel_sql(table, need_col_list, filter_list)
    return exec_sql(config.LDB_FILENAME, sql)


def logout(username):
    '''
    注销
    :param username: 用户名 str
    :return: 响应
    '''
    result = check_login_state()
    logging.debug(result)
    try:
        if result:
            url = '/api/logout'
            headers = {
                'User-Agent': 'AirMemo'
            }
            data = {'username': username, 'token': result[0]['token']}
            r = requests.post(protocol + user_host + url, headers=headers,
                              data=data)
            return r.json()
    except Exception as e:
        logging.error(e)
        return {'state': '-1'}


def register(username, password):
    '''
    注册用户
    :param username: 用户名
    :param password: 密码
    :return: 响应
    '''
    url = '/api/register'
    headers = {
        'User-Agent': 'AirMemo'
    }
    data = {'username': username, 'password': password}
    r = requests.post(protocol + user_host + url, headers=headers, data=data)
    try:
        return r.json()
    except Exception as e:
        logging.warning(e)
        return server_error_msg()


# 到达时间时触发槽
def time_out_slot():
    '''
    计时器超时槽函数
    :return:
    '''
    tips = QWidget()
    tips.resize(300, 120)
    # tips.setGeometry(1366-300,768-140,300, 120)
    tips.show()


# 获取用户云端的数据
def get_cloud_notes(username, token):
    '''
    获取用户云端的数据
    :param username: 用户名 str
    :param token:   token str
    :return: 响应
    '''
    url = '/api/cloud_page'
    headers = {
        'User-Agent': 'AirMemo'
    }
    data = {'username': username, 'token': token, 'page_id': '1', 'page_size': '5000'}
    r = requests.post(protocol + user_host + url, headers=headers, data=data)
    try:
        return r.json()
    except Exception as e:
        logging.warning(e)
        return server_error_msg()


def server_error_msg():
    return {"state": -1, "errMsg": "服务端异常"}
