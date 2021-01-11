import config
from comm.operateSqlite import sqlite_db
from comm.utils import cryptograph_text, decrypt_text
import logging
from comm.net import url,air_api

@url('/api/AirMemo/pc/login')
def login(url,username, password,*args,**kwargs):
    """request login api """
    # cryptograph_password()
    data = {'username': username, 'password': cryptograph_text(password, 'password')}
    return air_api().post(url, data=data)

@url('/api/AirMemo/pc/check_login')
def check_login(url,username, token,*args,**kwargs):
    data = {
        "username":username,
        "token":token
    }
    return air_api().post(url, data=data)

def get_login_status(*args,**kwargs):
    """check login status. """
    result = check_local_status()
    if not result:
        return {'status': 1}
    else:
        return check_login(**result)

def check_local_status() ->dict:
    '''check someone who with token'''
    sql = "select username,token from user where token is not NULL or username = 'visitor' order by id desc limit 0,1"
    ret = sqlite_db.select(sql,just_first=True)
    print(ret)
    if not ret['status']:
        logging.error(ret['msg'])
    return ret.get('records',dict())
