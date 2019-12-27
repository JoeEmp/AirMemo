from comm.operateSqlite import be_sql, exec_sql
import config
from comm.utils import cryptograph_text, protocol, user_host, decrypt_text
import requests
import logging
import comm.pubilc as pubilc


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
        cur = exec_sql(sql)
        for c in cur:
            c['message'] = decrypt_text(c['message'], 'message', user_name=username)
            c['detail'] = decrypt_text(c['detail'], 'detail', user_name=username)
    except Exception as e:
        logging.error(e)
        return []
    return cur


def update_notes(data, ele, **kwargs):
    '''
    更新内容
    :param filename:
    :param data:
    :param ele: 元素(如 'msg','detail')
    :return:
    '''
    try:
        if data['id'] != -1:
            filter_list = [
                ['id', '=', str(data['id'])]
            ]
            # 加密
            data[ele] = cryptograph_text(data[ele], ele, user_name=kwargs['user_name'])
            sql = be_sql().update_sql('Msg', {ele: data[ele], 'update_time': data['update_time']}, filter_list)
            # print(sql)
            cur = exec_sql(sql)
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


def delete_notes(filename, filter_list):
    return change_del_flag(filename, filter_list)


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
    return exec_sql(sql, is_update=1)


# 获取用户云端的数据
def get_cloud_notes(username, token):
    '''
    获取用户云端的数据
    :param username: 用户名 str
    :param token:   token str
    :return: 响应
    '''
    path = '/api/AirMemo/pc/cloud_page'
    data = {'username': username, 'token': token, 'page_id': '1', 'page_size': '5000'}
    pubilc.req_ser(path, data)
