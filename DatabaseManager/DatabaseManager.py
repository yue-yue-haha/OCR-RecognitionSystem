# Database manager for controlling the database
import sqlite3


class DatabaseManager(object):

    def __init__(self, db, jsonstr):
        self.db = db
        self.jsonstr = jsonstr

    def store(self):
        con = sqlite3.connect(self.db)

        cur = con.cursor()

        cur.execute("create table if not exists datas(name,title,telephone,email,company,address)")

        tmp = self.jsonstr
        # print(tmp['name'][0], tmp['title'][0], tmp['tel'][0], tmp['email'][0],tmp['comp'][0],tmp['addr'][0])

        cur.executemany("insert into datas(name,title,telephone,email,company,address) values (?,?,?,?,?,?)",
                        [(tmp['name'][0], tmp['title'][0], tmp['tel'][0], tmp['email'][0], tmp['comp'][0],
                          tmp['addr'][0])])

        # for row in con.execute("select name,title,telephone,email,company,address from datas"):
        #     print(row)

        con.commit()
        con.close()

    def get_all(self):
        con = sqlite3.connect(self.db)
        tables = con.execute("select name,title,telephone,email,company,address from datas")

        return tables

