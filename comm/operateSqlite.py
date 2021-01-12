import logging
import sqlite3
from config import LDB_FILENAME

sqlite_db = None


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


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
                sql = 'update %s set %s where %s' % (table, s_value[:-1], s_filter)
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


def exec_sql(sql):
    AirDataBase.select(sql)

class AirDataBase():
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.conn.row_factory = dict_factory
        super().__init__()

    def cursor(self, cursor=None):
        if cursor:
            return self.conn.cursor(cursor)
        return self.conn.cursor()

    def select(self, sql: str, params=None, just_first=False):
        ret = {"status": True}
        cur = self.conn.cursor()
        if None == params:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        if just_first:
            ret['records'] = cur.fetchone()
        else:
            ret['records'] = cur.fetchall()
        return ret

    def transaction(self, sql, param=None):
        if None == param:
            return self.transactions([sql], [[]])
        else:
            return self.transactions([sql], [param])

    def transactions(self, sqls, params):
        """deal many sql transaction. if needn't param use empty list."""
        ret = {'status': True}
        cur = self.conn.cursor()
        try:
            for i in range(len(sqls)):
                if 0 == len(params[i]):
                    cur.execute(sqls[i])
                else:
                    cur.execute(sqls[i], params[i])
            self.conn.commit()
        except Exception as e:
            ret['msg'] = e
            ret['errorsql'] = sqls[i]
            ret['status'] = False
        self.conn.rollback()
        if 1 == len(sqls):
            ret['rowcount'] = cur.rowcount
        return ret

link_db(LDB_FILENAME)

if __name__ == '__main__':
    db = AirDataBase_v2('../AirMemo.db')
    select_dict = dict(username='koko')
    ret = db.select(
        'select * from user')  # where username = ?', ['koko'])
    print(ret)
    ret = db.select('select * from user', just_first=True)
    print(ret)
    ret = db.transaction("delete from user where username = ?", ['cool1'])
    print(ret)
