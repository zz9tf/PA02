'''
test_categories runs unit and integration tests on the category module
'''

import pytest
from category import Category, to_cat_dict
from transactions import Transaction

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Category(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat1 = {'name':'food','desc':'groceries and takeout'}
    cat2 = {'name':'car','desc':'gas and repairs'}
    cat3 = {'name':'fun','desc':'movies and dining out'}
    id1=empty_db.add(cat1)
    id2=empty_db.add(cat2)
    id3=empty_db.add(cat3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        cat ={'name':'name'+s,
               'desc':'description '+s,
                }
        rowid = small_db.add(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])



@pytest.mark.simple
def test_to_cat_dict():
    ''' teting the to_cat_dict function '''
    a = to_cat_dict((7,'testcat','testdesc'))
    assert a['rowid']==7
    assert a['name']=='testcat'
    assert a['desc']=='testdesc'
    assert len(a.keys())==3


@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    cats0 = med_db.select_all()
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = med_db.select_one(rowid)
    assert cat1['name']==cat0['name']
    assert cat1['desc']==cat0['desc']


@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    cats2 = med_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1

@pytest.mark.update
def test_update(med_db):
    ''' add a category to db, updates it, and see that it changes'''

    # then we add this category to the table and get the new list of rows
    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(cat0)

    # now we upate the category
    cat1 = {'name':'new cat','desc':'new desc'}
    med_db.update(rowid,cat1)

    # now we retrieve the category and check that it has changed
    cat2 = med_db.select_one(rowid)
    assert cat2['name']==cat1['name']
    assert cat2['desc']==cat1['desc']



@pytest.fixture
def tran_db(tmpdir):
    filename = tmpdir.join('test_tracker.db')
    db = Transaction(filename)
    
    for i in range(10):
        s = str(i)
        cat ={'item_num': i,
            'amount': i*3838.92%10000,
            'category':'category'+s,
            'date': "2022-03-16",
            'description':'description '+s,}
        db.add(cat)
    yield db

@pytest.mark.add_transaction
def test_add_transaction(tran_db):
    ''' add a category to db, the select it, then delete it'''

    tran0 = {"category":'testing_add',
            'item_num': 10,
            'amount': 199.67,
            'description': "This is a test",
            "date": "2022-03-16"}
    cats0 = tran_db.select_all()
    rowid = tran_db.add(tran0)
    tran1 = tran_db.select_all()
    assert len(tran1) == len(cats0) + 1
    tran1 = tran_db.select_one(rowid)
    assert tran1['category']==tran0['category']
    assert tran1['description']==tran0['description']