import config
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
from comm.operateSqlite import sqlite_db
import logging

def add_msg(data:dict):
    '''
    添加数据 更改会影响 增加逻辑 延后重构 wrb
    :param filename: sqlit3文件名
    :param data:  dict {'id':-1,'{ele}':'','username':''}
    :return:
    '''
    if data['id'] == -1:
        data.pop('id')
        # 明文加密
        for k, v in data.items():
            if 'username' != k:
                data[k] = cryptograph_text(v, k, user_name=data['username'])
        sql = "insert into msg(username,msg,detail) values(:username,:msg,:detail)"
        ret = sqlite_db.transaction(sql,data)
        if not ret['status']:
            logging.error("msg:{}\nsql:{}".format(ret['msg'],ret['sql']))
        return ret