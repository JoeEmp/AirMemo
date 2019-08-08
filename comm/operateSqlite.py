# 这个工具类 操作 sqlite3
import logging
import sqlite3


# 构建字符串 提供 简单查询、更新，插入。
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


def exec_sql(filename, sql, is_update=None):
    '''
    :param filename: 文件名(含路径) str
    :param sql: 需要执行的sql str
    :param is_update: 默认为空返回全部，传入其他返回影响行数。如果是行数我会直接传'count'
    :except:  返回 None
    :return:  fetchall
    '''
    db = sqlite3.connect(filename)
    # sqlite 以字典格式返回查询结果
    db.row_factory = dict_factory
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


# 官方api提供，使返回的数据结构为 list of dict
def dict_factory(cursor, row):
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    return dict


if __name__ == '__main__':
    pass
    table = 'user'
    sql = 'select * from user;'
    r = exec_sql('AirMemo.db', sql)
    print(r)
