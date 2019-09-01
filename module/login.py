import config
import requests
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
import logging
from comm .pubilc import check_login_state

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
    data = {'username': username, 'password': cryptograph_text(password, 'password')}
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
            url = '/api/pc/check_login'
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
            # print(r)
            state = r.json()
        except Exception as e:
            logging.error(e)
            return {'state': -1, 'errMsg': '接口返回数据出错-%s' % r.status_code}
    # print(state)
    return state
