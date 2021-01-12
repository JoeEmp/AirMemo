import config
from comm.operateSqlite import sqlite_db
from comm.utils import cryptograph_text, decrypt_text
import logging
from comm.net import url, air_api

# CREATE TABLE Email_settings (
#     id          INTEGER       PRIMARY KEY,
#     username    VARCHAR (320) NOT NULL,
#     addr        VARCHAR (320) NOT NULL,
#     password    VARCHAR (20),
#     sender_name VARCHAR (30),
#     ssl_port    INTEGER,
#     user_ssl    INTEGER       DEFAULT (0),
#     is_default  INTEGER       DEFAULT (0)
# );


def add_email_conf(username, addr, password, sender_name, ssl_port, user_ssl, *args, **kwargs):
    param = (username, addr, password, sender_name, ssl_port, user_ssl)
    sql = """insert into 
        email_settings(username,addr, password, sender_name, ssl_port, user_ssl) 
        values(?,?,?,?,?,?)
    """
    return sqlite_db.transaction(sql, param)


def del_email_conf(id):
    sql = """delete from email_settings where id=? ; """
    param = [id]
    return sqlite_db.transaction(sql,param)


def update_email_conf(id, username, addr, password, sender_name, ssl_port, user_ssl, *args, **kwargs):
    param = (username, addr, password, sender_name, ssl_port, user_ssl, id)
    sql = """update 
        email_settings
            set username = ?,
            addr = ?,
            password = ?,
            sender_name = ?,
            ssl_port = ?,
            user_ssl = ?
        where id = ?
    """
    return sqlite_db.transaction(sql, param)


def get_user_email_conf(username, *args, **kwargs):
    sql = """ 
        select * from email_settings where username=?;
    """
    return sqlite_db.select(sql, [username], *args, **kwargs)


def get_email_conf(sql):
    print(sql)
    return sqlite_db.select(sql)

def set_is_default_email_conf(id,username):
    sql = """update email_settings set is_default = 0 where username = ? """
    param = [username]
    if not sqlite_db.transaction(sql,param)['status']:
        return 
    sql = """update email_settings set is_default = 1 where id= ? ;"""
    param = [id]
    return sqlite_db.transaction(sql,param)