# 这个工具类 操作 sqlite3
import logging
import sqlite3


# 构建字符串 提供 简单查询、更新，插入。
class be_sql(object):
    '''
    doc
    '''

    def update_sql(self, table, value_dict, filter_list=None):
        '''

        :param table:
        :param value_dict:
        :param filter_list:
        :return: str
        '''
        s_value = ''
        for k, v in value_dict.items():
            if v == 'NULL':
                s_value += k + ' = ' + v + ","
            else:
                s_value += k + ' = ' + "'" + v + "',"
        if not filter_list:
            return 'update %s set %s' % (table, s_value[:-1])
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
        # print(sql)
        return sql

    def ins_sql(self, table, dict):
        '''
        :param table:
        :param dict:
        :return: str
        '''
        s_col = ''
        s_value = ''
        for col, value in dict.items():
            s_col += col + ','
            s_value += "'" + value + "',"
        sql = 'insert into %s(%s) values(%s)' % (table, s_col[:-1], s_value[:-1])
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
            s_filter = s_filter[:-4] + ';'
            sql = 'select %s from %s where %s' % (s_need[:-1], table, s_filter)
        return sql


def exec_sql(filename, sql, is_update=None):
    db = sqlite3.connect(filename)
    c = db.cursor()
    try:
        cur = c.execute(sql)
        db.commit()
    except Exception as e:
        logging.error(e)
        return None
    if not is_update:
        return cur.fetchall()
    else:
        return cur.rowcount


if __name__ == '__main__':
    pass
    table = 'user'
    dict = {'username': 'loli', 'password': '123456'}
    dict1 = {'username': 'loli'}
    sql = be_sql().ins_sql(table, dict1)
    print(sql)
