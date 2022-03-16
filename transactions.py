import sqlite3


class Transaction:
    def __init__(self, filename) -> None:
        con= sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount float, category text, date date, description text)''')
        con.commit()
        con.close()
        self.dbfile = filename
    
    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""INSERT INTO transactions
                 VALUES(?,?,?,?,?)"""
                ,(item['item_num']
                ,item['amount']
                ,item['category']
                ,item['date']
                ,item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]