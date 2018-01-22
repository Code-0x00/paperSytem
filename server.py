#encoding:utf8
#!/usr/bin/python3

import sqlite3

class PAPERDB():
    def __init__(self):
        self.conn = sqlite3.connect('Papers.db')
        self.c = self.conn.cursor()
        try:
            self.table_create()
        except:
            print("Table already exist")

    def __del__(self):
        self.conn.close()

    def table_create(self):
        self.c.execute('''CREATE TABLE PAPER (
            ID      TEXT PRIMARY KEY    NOT NULL,
            INFO        TEXT
            );''')
        self.conn.commit()

    def insert(self,id,info):
        try:
            self.c.execute("""INSERT INTO PAPER (ID,INFO) \
                       VALUES ("%s",'%s')"""%(id,info));
        except:
            self.c.execute("""UPDATE PAPER set \
                            INFO = '%s' where ID= '%s'"""%(info,id))
        self.conn.commit()

    def select(self):
        ret=[]
        cursor=self.c.execute("""SELECT ID,INFO from PAPER order by ID""")
        for row in cursor:
            tmp={}
            tmp['ID']=row[0]
            tmp['INFO']=row[1]
            ret.append(tmp)
        return ret
        
        def delete(self,id):
            self.c.execute("DELETE from PAPER where ID='{}';".format(id))
            self.conn.commit()
        
    def debug(self):
        self.select()
        
if __name__=='__main__':
    test=PAPERDB()
    try:
        test.table_create()
    except:
        print("Table already exist")
    test.debug()