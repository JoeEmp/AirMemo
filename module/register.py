import config
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
import requests
import logging
from  comm.pubilc import check_login_state,server_error_msg

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
