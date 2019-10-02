from comm.pubilc import check_login_state
from comm.user_cache import mine
from module.note import get_notes
import config

def add_user_note():
    username = mine.get_value('user_info')['username']
    get_notes(config.LDB_FILENAME,username)

def update_user_info():
    '''
    检测登录用户的信息
    :return:
    '''
    result = check_login_state()
    if result:
        result = result[0]
    else:
        result = {'username': 'visitor', 'token': ''}
    mine.update_item('user_info', result)