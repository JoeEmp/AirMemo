from comm.operateSqlite import sqlite_db


def get_user_reminder_conf(username):
    sql = """ 
        select * from reminder where username=? order by sequence;
    """
    return sqlite_db.select(sql, [username])
