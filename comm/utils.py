import datetime
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMessageBox, QWidget
from config import ENV, PROTOCOL
from comm.operateSqlite import be_sql, sqlite_db
import requests
import logging
import os

# 服务器切换


def url(url, env='debug'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                prefix = ENV[env].value
            except:
                prefix = ENV['debug'].value
            return func(prefix+url, args, kwargs)
        return wrapper
    return decorator


# 返回等分字典
def getSize(divide):
    sizeDict = {}
    screenSize = QApplication.desktop().screenGeometry()
    sizeDict['width'] = (screenSize.width() / divide['width'])
    # sizeDict['height']=(screenSize.heigth()/divide['height'])
    return sizeDict


# 设置app
def setApp(app):
    app.setStyle(QStyleFactory.create('Fusion'))
    # 关闭所有窗口,也不关闭应用程序
    QApplication.setQuitOnLastWindowClosed(False)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./ui/app_icon.png"), QtGui.QIcon.Normal,
                   QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    app.setWindowIcon(QIcon('./ui/app_icon.png'))


# 获取用户信息
def get_user_info(table, username):
    filter_list = [['username', '=', username]]
    sql = be_sql().sel_sql(table, filter_list=filter_list)
    ret = sqlite_db.select(sql)
    if not ret['status']:
        logging.error(ret['msg'])
    info = ret['records'] if 'records' in ret.keys() else list()
    returninfo


# 获取索引
def get_index(dict, keys):
    if not keys or not dict:
        return None
    index_list = []
    for key in keys:
        try:
            index_list.append(list(dict.keys()).index(key))
        except Exception as e:
            print(e)
    return index_list


# 发送邮件
def mail(info, title, recipients, content):
    # 获取授权密码
    sql = "select * from email_settings where username ='%s'" % info['username']
    ret = sqlite_db.select(sql)
    if not ret['status']:
        logging.error(ret['msg'])
    records = ret['records'] if 'records' in ret.keys() else list()
    record, password = records[0], records[0]['password']
    # ssl 端口设置
    port = 25
    if record['user_ssl'] == 1:
        port = record['ssl_port']

    ret = {'status': 1, 'msg': ''}
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr([record['sender_name'], info['addr']])
        msg['To'] = ','.join([recipients])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        # server_offer = re.findall('@(.+?)\.',info['addr'])
        if port != 25:
            server = smtplib.SMTP_SSL("smtp.%s" % info['addr'].split('@')[-1],
                                      port)  # 发件人邮箱中的SMTP服务器，端口是25

        server.login(info['addr'], password)  # 括号中对应的是发件人邮箱账号、邮箱密码

        server.sendmail(info['addr'], msg['To'].split(','),
                        msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
    except Exception as e:
        logging.warning(str(e.smtp_error, encoding='gbk'))
        ret = {'status': -1,
               'msg': '账号%s %s' % (info['addr'], str(e.smtp_error, encoding='gbk'))}
    return ret


def cryptograph_text(text, text_type, **kwargs):
    '''
    :param text: 需要加密的文本
    :param text_type: 文本类型目前有 'password','msg','detail'
    :return: 密文或者空
    '''
    text = '\ '.join(text.split())
    try:
        # 密码加密
        if 'password' == text_type:
            return cryptograph_text(text)
        # msg加密
        elif 'msg' == text_type or 'message' == text_type:
            return get_aes_cryText(kwargs['user_name'], text)
        # detail加密
        elif 'detail' == text_type:
            return get_aes_cryText(kwargs['user_name'], text)
        else:
            return None
    except Exception as e:
        logging.warning(e)
        return None


def decrypt_text(text, text_type, **kwargs):
    try:
        # msg解密
        if 'msg' == text_type or 'message' == text_type:
            return get_aes_decryText(kwargs['user_name'], text)
        # detail解密
        elif 'detail' == text_type:
            return get_aes_decryText(kwargs['user_name'], text)
        else:
            return None
    except Exception as e:
        logging.warning(e)
        return None


# 创建提醒时间线程
def create_reminder(parent, time):
    try:
        time = datetime.datetime.strptime(time, '%H:%M:%S')
    except Exception as e:
        return QMessageBox.information(parent, ' ', str(e), QMessageBox.Ok)
    sec = (time - datetime.datetime.strptime('00:00:00', '%H:%M:%S')).seconds


def get_aes_cryText(user_name, text):
    """ 返回加密字符串 """
    r = os.popen('./be-aes %s -c %s' % (user_name, text))
    text = r.read()
    return text[:-1]


def get_aes_decryText(user_name, text):
    '''
    返回明文字符串
    :param user_name: 用户名
    :param text: 密文
    :return: 明文
    '''
    r = os.popen('./be-aes %s -d %s' % (user_name, text))
    text = r.read()
    return text[:-1]


def cryptograph_text(text):
    """md5(text)."""
    logging.info(text)
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


def get_json_lines(filename: str, offsetlines=0, endlines=-1):
    get_file_data(filename, is_json=True,
                  offsetlines=offsetlines, endlines=endlines)


def get_data_lines(filename: str, has_title=False, offsetlines=0, endlines=-1):
    get_file_data(filename, has_title=has_title,
                  offsetlines=offsetlines, endlines=endlines)


def get_file_data(filename: str, has_title=False, offsetlines=0, endlines=-1, is_json=False):
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            print('%s 文件没内容' % filename)
            return None
    if is_json:
        has_title = False
    if has_title:
        title = lines[0].rstrip(os.linesep).split(',')
        length = len(title)
        if offsetlines != 0:
            offsetlines = 1
        is_json = False
    for i in range(len(lines)):
        if i < offsetlines:
            continue
        if i == endlines:
            break
        else:
            value = lines[i].rstrip(os.linesep).split(',')
            if has_title:
                yield zip(title, value)
            elif is_json:
                yield(json.loads(lines[i].rstrip(os.linesep)))
            else:
                yield value

user_host =''

class base_api(object):
    """ 该类是requests的二次封装,算是一个sub版,如有入参错误查看requests即可. """

    def __init__(self):
        self.last_url, self.last_response = None, None

    @staticmethod
    def is_normal(response: requests.Response, code_ranges=list()) -> bool:
        """ check http status code,you can use code_ranges assert expectation value """
        if not code_ranges:
            return response.ok
        elif isinstance(code_ranges, list) and response.status_code in code_ranges:
            return True
        return False

    def get_api(self, url, method='post', *args, **kwargs) -> dict:
        ret = dict(status=True)
        try:
            if 'post' == method:
                response = requests.post(url, **kwargs)
            elif 'get' == method:
                response = requests.get(url, **kwargs)
            elif 'options' == method:
                response = requests.options(url, **kwargs)
            if 'code_ranges' in kwargs.keys():
                kwargs['code_ranges'] = list()
                ret['status'] = base_api.is_normal(
                    response, code_ranges=kwargs['code_ranges'])
            try:
                ret['body'] = response.json()
            except:
                ret['body'] = response.text
            self.last_url, self.last_response = url, response
        except Exception as e:
            ret['status'], ret['reason'] = False, e
        return ret

    def post(self, url, *args, **kwargs):
        """ get_api use post method """
        return self.get_api(url, method='post', *args, **kwargs)

    def get(self, url, *args, **kwargs):
        """ get_api use get method """
        return self.get_api(url, method='get', *args, **kwargs)

    def options(self, url, *args, **kwargs):
        """ get_api use options method """
        return self.get_api(url, method='options', *args, **kwargs)

    def __doc__(self):
        """该类是requests的二次封装,算是一个sub版,如有入参错误查看requests即可.
        last_url,last_response分别为最近一次的请求地址和请求结果(Response)。在并发请求的时候请注意这两个属性的使用.
        """


if __name__ == '__main__':
    pass
    app = QApplication(sys.argv)
    tips = QWidget()
    # tips.resize(300,120)

    tips.setGeometry(1366 - 310, 768 - 170, 300, 120)
    tips.show()
    sys.exit(app.exec_())
    # dbName = r'AirMemo.db'
    # # add_records(dbName)
    # print(get_records(dbName))
    # # clear_records(filename=dbName,Severdate='2019-01-05')
    # print(get_records(dbName))
