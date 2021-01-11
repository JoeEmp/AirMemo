from comm.operateSqlite import be_sql, sqlite_db
import config
from comm.utils import cryptograph_text, decrypt_text
import requests
from comm.net import url, air_api
import logging


def get_notes(username='visitor', is_del='0'):
    sql = "select * from Msg where username = ? and is_del = 0"
    ret = sqlite_db.select(sql, [username])
    # 解密
    for note in ret.get('records', list()):
        note['message'] = decrypt_text(
            note['message'], 'message', username=username)
        note['detail'] = decrypt_text(
            note['detail'], 'detail', username=username)
    return ret


def update_notes(data, ele, **kwargs):
    # 加密
    data[ele] = cryptograph_text(data[ele], ele, username=kwargs['username'])
    sql = "update Msg set {}=:{},update_time=datetime(CURRENT_TIMESTAMP, 'localtime') where id != -1 and id = ?".format(
        ele, ele)
    ret = sqlite_db.transaction(sql, [data['id']])
    if not ret['status']:
        logging.error("message:{}\nsql:{}".format(ret['msg'], ret['errorsql']))
    return ret


def add_notes(data):
    for k, v in data.items():
        if 'username' != k:
            ele = k
            data[k] = cryptograph_text(v, k, username=data['username'])
    sql = "insert into Msg({},username) values(?,?)".format(ele)
    ret = sqlite_db.transaction(sql, [data[ele], data['usename']])
    if not ret['status']:
        logging.error("message:{}\nsql:{}".format(ret['msg'], ret['errorsql']))
    sql = "select * from Msg where username = ? and is_del = 0 order by id desc limit 0 ,1"
    ret = sqlite_db.select(
        sql, [data['username']], just_first=True)
    return ret


def delete_note(id):
    return change_del_flag(id=id)


def change_del_flag(id, is_del=1):
    ''' '''
    sql = "update Msg set is_del = ? where id=?"
    return sqlite_db.transaction(sql, [is_del, id])


@url('/api/AirMemo/pc/cloud_page')
def get_cloud_notes(url, username, token, *args, **kwargs):
    data = {'username': username, 'token': token,
            'page_id': '1', 'page_size': '5000'}
    return air_api().post(url, data=data)
