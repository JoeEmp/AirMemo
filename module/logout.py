import config
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
import requests
import logging
from comm.pubilc import check_login_status


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
            url = '/api/AirMemo/pc/logout'
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
        return {'status': '-2'}
