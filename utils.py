import datetime
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMessageBox, QWidget
import config
from operateSqlite import be_sql, exec_sql
import logging
# from customWidget import Toast

protocol = 'http://'
local_host = '127.0.0.1:5000'
pro_host = '149.129.125.8:5000'
# 服务器切换
user_host = local_host


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
    return exec_sql(config.LDB_FILENAME, sql)


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
    record = exec_sql(config.LDB_FILENAME,
                      "select * from email_settings where username ='%s'" % info['username'])[0]
    password = record['password']

    # ssl 端口设置
    port = 25
    if record['user_ssl'] == 1:
        port = record['ssl_port']

    ret = {'state': 1, 'errMsg': ''}
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr([record['sender_name'], info['addr']])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
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
        ret = {'state': -1, 'errMsg': '账号%s %s' % (info['addr'], str(e.smtp_error, encoding='gbk'))}
    return ret


# 产生密文密码
def cryptograph_password(password):
    if password:
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        cryptograph = m.hexdigest()
    else:
        cryptograph = None
    return cryptograph


# 创建提醒时间线程
def create_reminder(parent, time):
    try:
        time = datetime.datetime.strptime(time, '%H:%M:%S')
    except Exception as e:
        return QMessageBox.information(parent, ' ', str(e), QMessageBox.Ok)
    sec = (time - datetime.datetime.strptime('00:00:00', '%H:%M:%S')).seconds


def showToast(parent,text):
    pass


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
