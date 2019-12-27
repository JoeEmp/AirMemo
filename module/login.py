import config
import requests

from comm.operateSqlite import exec_sql, be_sql
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
import logging
import comm.pubilc as pubilc


def login(username, password):
    '''
    客户端登录请求
    :param username:
    :param password:
    :return:
    '''
    path = '/api/AirMemo/pc/login'
    # cryptograph_password()
    data = {'username': username, 'password': cryptograph_text(password, 'password')}
    return pubilc.req_ser(path, data)


def get_login_status():
    '''
    查询用户在 服务器 的登录状态
    :return: {"status":,"msg":,"token":}
    '''
    # 检查本地token
    result = check_login_status()
    # 本地无用户登录
    if not result:
        return {'status': 1}
    # 本地有token的用户去服务器校验
    else:
        try:
            path = '/api/AirMemo/pc/check_login'
            data = result[0]
            r = pubilc.req_ser(path, data)
        except Exception as e:
            logging.error(e)
            return {'status': -1, 'msg': '未知错误'}
    return r


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
    return exec_sql(sql)
