# 构建字符串 提供 简单查询、更新，插入。
class be_sql(object):
    '''
    doc
    '''
    def update_sql(self,table,value_dict,filter_list=None):
        s_value = ''
        for k,v in value_dict.items():
            s_value += k + '=' + "'"+ k +"',"
        if not filter_list:
            return 'update %s set %s ;'%(table,s_value[:-1])
        else:
            s_filter = ''
            for item in filter_list:
                for i in item:
                    # 做了 空判断
                    if i is item[-1] and i != 'NULL':
                        s_filter += "'" + i + "'"+' '
                    else:
                        s_filter += i+' '
                s_filter += ' and '
            s_filter = s_filter[:-4]+';'
            sql = 'update %s set %s where %s;'%(table,s_value[:-1],s_filter)
        return sql

    def ins_sql(self,table,col_list,value_list):
        s_col = ''
        s_value = ''
        for col in col_list:
            s_col += col+','
        for value in value_list:
            s_value += "'"+value+"',"
        sql = 'insert into %s(%s) values(%s);'%(table,s_col[:-1],s_value[:-1])
        return sql


    def sel_sql(self,table,need_col_list=None,filter_list=None):
        """ 生成简单的查询语句 多条件用 and连接 无分页，排序。
        参数：
        table 表名
        need_col_list 展示字段
        fileter_list 过滤条件
        [
            ['col','like','value'],
            ['col','=','value'],
            ['col','<=','']
        ]
        返回 str
        例子：
        table = 'tablename'                    # 表名(tablename or dbname.tablename) str
        need_col_list = ['*']                  # 需要的字段名 list
        filter_list = [['username','=','joe']] # 过滤条件 list of list
        sql = be_sql().be_sel_sql(table,need_col_list,filter_list)
        """
        if not need_col_list:
            s_need = '*,'
        else:
            s_need = ''
            for col in need_col_list:
                s_need += col+','
        if not filter_list:
            return 'select %s from %s'%(s_need[:-1],table)
        else:
            s_filter = ''
            for item in filter_list:
                for i in item:
                    # 做了 空判断
                    if i is item[-1] and i != 'NULL':
                        s_filter += "'" + i + "'"+' '
                    else:
                        s_filter += i+' '
                s_filter += ' and '
            s_filter = s_filter[:-4]+';'
            sql = 'select %s from %s where %s'%(s_need[:-1],table,s_filter)
        return sql

if __name__ == '__main__':
    pass
    table = 'user'
    need_col_list = ['username','token']
    filter_list = [['token','is not','NULL']]
    sql = be_sql().sel_sql(table,need_col_list,filter_list)
    print(sql)