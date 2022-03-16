import sqlite3


class Transaction:
    def __init__(self, filename) -> None:
        con= sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS categories
                    (item_num int , 
                    amount float, 
                    category text,
                    date date, 
                    description text)''')
        con.commit()
        con.close()
        self.dbfile = filename