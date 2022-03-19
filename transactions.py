"""
transaction.py is a Object Relational Mapping to the transaction table

The ORM will work map SQL rows with the schema
    (item_num,amount,category,date,description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

------ Written by Zheng.
"""

import sqlite3

def to_trans_dict(trans_tuple):
    ''' trans is a transaction tuple (item_num, amount, category, date, description) ----- Written by Zheng'''
    trans = {
        'item':trans_tuple[1]
        , 'amount':trans_tuple[2]
        , 'category':trans_tuple[3]
        , 'date':trans_tuple[4]
        , 'description':trans_tuple[5]}
    return trans

def to_trans_dict_list(trans_tuples):
    ''' convert a list of trans tuples into a list of dictionaries ----- Written by Zheng'''
    return [to_trans_dict(trans) for trans in trans_tuples]

class Transaction:
    ''' Transaction represents a table of transactions ----- Written by Zheng '''
    def __init__(self, filename) -> None:
        con= sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item text, amount int, category text, date int, description text)''')
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
        return to_trans_dict_list(tuples)

    def select_one(self,rowid):
        ''' return a transaction with a specified rowid ----- Written by Zheng '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
             ----- Written by Zheng
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""INSERT INTO transactions
                 VALUES(?,?,?,?,?)"""
                ,(item['item']
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

    def delete(self, item):
        ''' delete a transaction defined by item # ----- Written by Zixin '''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''delete from transactions
                        where item = (?)''',(item,))
        con.commit()
        con.close()
    
    def sumByDate(self):
        ''' sum up item nums group by date ----- Written by Zixin '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''select date, sum(amount) from transactions group by date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        res = {
            'date':tuples[0][0],
            'sum':tuples[0][1]
        }
        return res