from comm.operateSqlite import be_sql, exec_sql
import config
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
import requests
import logging


def add_msg(filename, data):
    '''
    添加数据 更改会影响 增加逻辑 延后重构 wrb
    :param filename: sqlit3文件名
    :param data:  dict {'id':-1,'{ele}':'','username':''}
    :return:
    '''
    sql = ''
    try:
        if data['id'] == -1:
            del data['id']
            #
            for k, v in data.items():
                if 'username' != k:
                    data[k] = cryptograph_text(v, k, user_name=data['username'])
            sql = be_sql().ins_sql('Msg', data)
            exec_sql(sql)
            logging.info('add records done')
            return len(exec_sql('select * from Msg')) - 1
    except Exception as e:
        logging.error('add error ', ending='\t')
        logging.error(sql)
        print(e)
        return -1