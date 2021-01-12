from PyQt5.QtWidgets import QWidget
from comm.operateSqlite import be_sql, sqlite_db
import config
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
import requests
import logging


def get_notes(username='visitor', is_del='0'):
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
        ret = sqlite_db.select(sql)
        if ret['status']:
            for record in ret['records']:
                record['message'] = decrypt_text(
                    record['message'], 'message', user_name=username)
                record['detail'] = decrypt_text(
                    record['detail'], 'detail', user_name=username)
    except Exception as e:
        logging.error(e)
    return ret


def restore_note(filter_list):
    return change_del_flag(filter_list, is_del=0)


def change_del_flag(filter_list, is_del=1):
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
    return sqlite_db.transaction(sql)


def clear_notes(filename, sever_date):
    '''
    根据系统返回天数物理删除记录
    :param filename:
    :param sever_date:
    :return:
    '''
    try:
        sqlite_db.transaction(
            ("delete from Msg where del_time<strftime('yyyy-mm-dd',%s);" % sever_date))
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
    data = {'username': username,
            'password': cryptograph_text(password, 'password')}
    try:
        r = requests.post(protocol + user_host + url,
                          headers=headers, data=data, proxies=config.proxies)
        return r.json()
    except Exception as e:
        logging.warning(e)
        return dict()


def get_login_status():
    '''
    查询用户在 服务器 的登录状态
    :return:
    '''
    # 检查本地token
    result = check_login_status()
    # 本地无用户登录
    if not result:
        return {'status': 1}
    # 本地有token的用户去服务器校验
    else:
        try:
            url = '/api/AirMemo/pc/check_login'
            headers = {
                'User-Agent': 'AirMemo'
            }
            data = result[0]
            r = requests.post(protocol + user_host + url,
                              headers=headers, data=data, proxies=config.proxies)
        except Exception as e:
            logging.error(e)
            return {'status': -1, 'msg': '无法连接服务器'}
        try:
            # print(r)
            status = r.json()
        except Exception as e:
            logging.error(e)
            return {'status': -1, 'msg': '接口返回数据出错-%s' % r.status_code}
    # print(status)
    return status


def check_login_status():
    '''
    查找 本地 token非空的人
    :return: 查询结果 结构[[{'username':'','token':''}],]
             无查询结果时 结构为[]
    '''
    table = 'user'
    need_col_list = ['username', 'token']
    filter_list = [['token', 'is not', 'NULL']]
    sql = be_sql().sel_sql(table, need_col_list, filter_list)
    logging.warning('sql_lite {}'.format(sqlite_db))
    return sqlite_db.select(sql, just_first=True)


def logout(username):
    '''
    注销
    :param username: 用户名 str
    :return: 响应
    '''
    result = check_login_status()
    logging.debug(result)
    try:
        if result:
            url = '/api/logout'
            headers = {
                'User-Agent': 'AirMemo'
            }
            data = {'username': username, 'token': result[0]['token']}
            r = requests.post(protocol + user_host + url, headers=headers,
                              data=data,
                              proxies=config.proxies
                              )
            return r.json()
    except Exception as e:
        logging.error(e)
        return {'status': '-1'}


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
    r = requests.post(protocol + user_host + url,
                      headers=headers, data=data, proxies=config.proxies)
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
    data = {'username': username, 'token': token,
            'page_id': '1', 'page_size': '5000'}
    r = requests.post(protocol + user_host + url,
                      headers=headers, data=data, proxies=config.proxies)
    try:
        return r.json()
    except Exception as e:
        logging.warning(e)
        return server_error_msg()


def server_error_msg(code=-1, e=None):
    ret = {'status': -1}
    if issubclass(TimeoutError, e):
        ret['msg'] = '返回超时'
    else:
        ret['msg'] = "%s - 服务端异常" % code
    return ret


def req_ser(path, data=None, headers=None):
    '''
    集成了接口的返回错误处理，和网络问题
    :param path:    路径如 '/api/cloud_page'
    :param data:
    :param headers: 不传入默认使用 { 'User-Agent': 'AirMemo' }
    :return:
    '''
    if not headers:
        headers = {
            'User-Agent': 'AirMemo'
        }
    try:
        r = requests.post(protocol + user_host + path,
                          headers=headers, data=data, proxies=config.proxies)
    except Exception as e:
        logging.error(e)
        return {'status': -1, 'msg': '无法连接服务器'}
    try:
        return r.json()
    except Exception as e:
        logging.warning(e)
        return server_error_msg(r.status_code)
