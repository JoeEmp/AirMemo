# 这个工具类 操作 sqlite3
import logging
import sqlite3
import records
from config import LDB_FILENAME

sqlite_db = None


def dict_factory(cursor, row):
    '''
    # 官方api提供，使返回的数据结构为 list of dict
    :param cursor:
    :param row:
    :return:
    '''
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    return dict


def link_db(filename):
    '''
    链接数据库修改本文件的db变量
    :param filename:
    :return:
    '''
    global sqlite_db
    try:
        if not sqlite_db:
            sqlite_db = AirDataBase(filename)
    except Exception as e:
        logging.error(e)


class be_sql(object):
    '''
    构建字符串 提供 简单查询、更新，插入
    '''

    def update_sql(self, table, value_dict, filter_list=None):
        '''
        :param table:  表名 str
        :param value_dict:  {'col':'value'} dict
        :param filter_list: [['col','Operator','value']] case [['username','=','joe']] list of list
        :return: str
        '''
        try:
            s_value = ''
            for k, v in value_dict.items():
                # 对关键词特殊处理
                if v == 'NULL' or "(datetime(CURRENT_TIMESTAMP, 'localtime') )" == v:
                    s_value += k + ' = ' + v + ","
                else:
                    s_value += k + ' = ' + "'" + v + "',"
            s_value = s_value[:-1]
            # 无过滤条件，直接返回
            if not filter_list:
                return 'update %s set %s' % (table, s_value)
            # 组合过滤条件
            else:
                s_filter = ''
                for item in filter_list:
                    for i in item:
                        # 做了 空判断
                        if i is item[-1] and i != 'NULL':
                            s_filter += "'" + i + "'" + ' '
                        else:
                            s_filter += i + ' '
                    s_filter += ' and '
                s_filter = s_filter[:-4]
                sql = 'update %s set %s where %s' % (table, s_value, s_filter)
            # print(sql)
        except Exception as e:
            logging.warning(e)
            return ''
        return sql

    def ins_sql(self, table, dict):
        '''
        :param table: 表名
        :param dict:  {'col':'value'}
        :return: str
        '''
        s_col = ''
        s_value = ''
        for col, value in dict.items():
            s_col += col + ','
            s_value += "'" + value + "',"
        sql = 'insert into %s(%s) values(%s)' % (
            table, s_col[:-1], s_value[:-1])
        return sql

    def sel_sql(self, table, need_col_list=None, filter_list=None):
        '''
        生成简单的查询语句 多条件用 and连接 无分页，排序。
        :param table:           # 表名(tablename or dbname.tablename) str
        :param need_col_list:   # 需要的字段名 list
        :param filter_list:     # 过滤条件 list of list
        :return:                # sql语句 str

        例子：
        table = 'tablename'
        need_col_list = ['*']
        filter_list = [['username','=','joe']]
        sql = be_sql().be_sel_sql(table,need_col_list,filter_list)
        '''
        if not need_col_list:
            s_need = '*,'
        else:
            s_need = ''
            for col in need_col_list:
                s_need += col + ','
        if not filter_list:
            return 'select %s from %s' % (s_need[:-1], table)
        else:
            s_filter = ''
            for item in filter_list:
                for i in item:
                    # 做了 空判断
                    if i is item[-1] and i != 'NULL':
                        s_filter += "'" + i + "'" + ' '
                    else:
                        s_filter += i + ' '
                s_filter += ' and '
            s_filter = s_filter[:-4]
            sql = 'select %s from %s where %s' % (s_need[:-1], table, s_filter)
        return sql

    def del_sql(self, table, filter_list=None):
        '''
        :param table: 表名 str
        :param filter_list: 过滤条件 list of list
        :return: str
        '''
        if not filter_list:
            return 'delete from %s ;' % (table)
        else:
            s_filter = ''
            for item in filter_list:
                for i in item:
                    # 做了 空判断
                    if i is item[-1] and i != 'NULL':
                        s_filter += "'" + i + "'" + ' '
                    else:
                        s_filter += i + ' '
                s_filter += ' and '
            s_filter = s_filter[:-4] + ';'
            return 'delete from %s where %s' % (table, s_filter)


def exec_sql(sql, is_update=None):
    '''
    :param filename: 文件名(含路径) str
    :param sql: 需要执行的sql str
    :param is_update: 默认为空返回全部，传入其他返回影响行数。如果是行数我会直接传'count'
    :except:  返回 None
    :return:  fetchall
    '''
    c = sqlite_db.cursor()
    try:
        cur = c.execute(sql)
        sqlite_db.commit()
    except Exception as e:
        logging.error(e)
        return None
    if not is_update:
        return cur.fetchall()
    else:
        return cur.rowcount


class BaseDataBase(object):
    def __init__(self):
        self.db = None

    def select(self, sql: str, params=None, just_first=False):
        conn = self.db.get_connection()
        ret = dict(status=False)
        if 'create table' in sql.lower():
            ret['msg'] = "cann't create table ,you should use transaction to create table"
            return ret
        if params:
            rows = conn.query(sql, **params)
        else:
            rows = conn.query(sql)
        if just_first:
            ret['records'] = rows.first(as_dict=True)
        else:
            ret['records'] = rows.all(as_dict=True)
        ret['status'] = True
        return ret

    def transaction(self, sql, params=None):
        if params:
            return self.transactions([sql], [params])
        else:
            return self.transactions([sql])

    def transactions(self, sqls: list, multiparams=None):
        """ 同records实现 """
        conn = self.db.get_connection()
        transaction = conn.transaction()
        try:
            for i in range(len(sqls)):
                if multiparams:
                    conn.query(sqls[i], **multiparams[i])
                else:
                    conn.query(sqls[i])
            transaction.commit()
        except Exception as e:
            transaction.rollback()
            return dict(status=False, msg=e, errorsql=sqls[i])
        finally:
            conn.close()
        return dict(status=True, msg='transaction complete')


class AirDataBase(BaseDataBase):
    def __init__(self, filename):
        self.db = records.Database('sqlite:///{}'.format(filename))


link_db(LDB_FILENAME)

if __name__ == '__main__':
    pass
    db = AirDataBase('AirMemo.db')
    select_dict = dict(username='koko')
    ret = db.select(
        'select * from User where username = :username', select_dict)
    print(ret)
    ret = db.select('select * from User', just_first=True)
    print(ret)
    ret = db.transaction('select * from User')
    print(ret)
    ret = db.transactions(['insert into User(username) values(\'cool\')',
                           'insert into User(name) values(\'cool2\')'])
    print(ret)
