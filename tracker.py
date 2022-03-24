#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''

import sys
from transactions import Transaction
from category import Category

transactions = Transaction('transaction.db')
category = Category('category.db')


# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''




def process_choice():
    """  the method to process the choice of users"""

    choice = input("> ")

    if choice=='0':
        sys.exit()
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice=='4':
        print("-- show transactions --")
        trans = transactions.select_all()
        print_transactions(trans)
    elif choice=='5':
        print("-- add transaction --")
        item = input("item #: ")
        amount = int(input("the amount of new item: "))
        cate = input("category: ")
        desc = input("new item description: ")
        date = int(input("date of this update(yyyymmdd): "))
        tran = {"item": item,
                "category": cate,
                "amount": amount,
                "description": desc,
                "date": date}
        transactions.add(tran)
    elif choice=='6':
        print("-- delete transaction --")
        id = input("the id you want to delete: ")
        transactions.delete(id)
    elif choice=='7':
        print("-- summarize transactions by date --")
        res = transactions.sumByDate()
        #print(res)
        print("%-10s %-10s"%('date', 'sum'))
        print("-"*15)
        for tuple in res:
            print("%-10d %-10d"%(tuple[0], tuple[1]))
    elif choice=='8':
        print("-- summarize transactions by month --")
        res = transactions.sumByMonth()
        print("%-10s %-10s"%('month', 'sum'))
        print("-"*15)
        for tuple in res:
            print("%-10d %-10d"%(tuple[0], tuple[1]))
    elif choice=='9':
        print("-- summarize transactions by year --")
        res = transactions.sumByYear()
        #print(res)
        print("%-10s %-10s"%('year', 'sum'))
        print("-"*15)
        for tuples_year in res:
            print("%-10d %-10d"%(tuples_year[0], tuples_year[1]))  
    elif choice=='10':
        print("-- summarize transactions by category --")
        res = transactions.sumByCat()
        print("%-10s %-10s"%('date', 'sum'))
        print("-"*15)
        for tuple in res:
            print("%-10s %-10d"%(tuple[0], tuple[1]))
    elif choice=='11':
        print(menu)
    else:
        print("choice",choice,"not yet implemented")




def toplevel():
    ''' handle the user's choice and read the command args and process them'''
    print(menu)
    while True :
        process_choice()
    print('bye')

# here are some helper functions

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-10s %-30s"%(
        'rowid', 'item','amount','category','date','description'))
    print('-'*70)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10s %-10d %-10s %-10d %-30s"%values)

def print_category(cat):
    ''' print category '''
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    ''' print categories '''
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()
