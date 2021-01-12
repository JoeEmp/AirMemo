import config
from comm.utils import cryptograph_text, decrypt_text
from comm.net import url,base_api
import requests
import logging
from json.decoder import JSONDecodeError
from requests.exceptions import ReadTimeout
from comm.net import air_api

@url('/api/AirMemo/pc/register')
def register(username, password,again_pwd,*args,**kwargs):
    '''注册用户. '''
    headers = {
        'User-Agent': 'AirMemo'
    }
    data = {'username': username, 'password': password,'again_password':again_pwd}
    return air_api().post(url,data=data,headers=headers)
