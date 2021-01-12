import sqlite3
import config
import os


def init_db(filename):
    if os.path.exists(filename):
        os.system('rm -rf %s' % config.LDB_FILENAME)
    else:
        conn = sqlite3.connect(filename)
    try:
        with open('AirMemo_table_ddl.sql') as f:
            conn.cursor().executescript(f.read())
            conn.commit()
    except Exception as e:
        print(e)
        os.system('rm -rf %s' % config.LDB_FILENAME)

if __name__ == "__main__":
    init_db(config.LDB_FILENAME)
