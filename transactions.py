"""
transaction.py is a Object Relational Mapping to the transaction table

The ORM will work map SQL rows with the schema
    (item_num,amount,category,date,description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

------ Written by Zheng.
"""

import sqlite3

def to_cat_dict(cat_tuple):
    ''' cat is a transaction tuple (rowid, name, desc) ----- Written by Zheng'''
    cat = {
        'item_num':cat_tuple[1]
        , 'amount':cat_tuple[2]
        , 'category':cat_tuple[3]
        , 'date':cat_tuple[4]
        , 'description':cat_tuple[5]}
    return cat

def to_cat_dict_list(cat_tuples):
    ''' convert a list of category tuples into a list of dictionaries ----- Written by Zheng'''
    return [to_cat_dict(cat) for cat in cat_tuples]

class Transaction:
    ''' Transaction represents a table of transactions ----- Written by Zheng '''
    def __init__(self, filename) -> None:
        con= sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount float, category text, date date, description text)''')
        con.commit()
        con.close()
        self.dbfile = filename

    def select_all(self):
        ''' return all of the transactions as a list of dicts. ----- Written by Zheng'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def select_one(self,rowid):
        ''' return a transaction with a specified rowid ----- Written by Zheng '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict(tuples[0])

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
             ----- Written by Zheng
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
