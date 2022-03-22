'''
test_transactions runs unit and integration tests on the transactions module
'''

import pytest
from transactions import Transaction


@pytest.fixture
def tran_db(tmpdir):
    filename = tmpdir.join('test_tracker.db')
    db = Transaction(filename)
    
    for i in range(10):
        s = str(i)
        cat ={'item': i,
            'amount': i*3838.92%10000,
            'category':'category'+s,
            'date': "20220316",
            'description':'description '+s,}
        db.add(cat)
    yield db


@pytest.mark.add_transaction
def test_add_transaction(tran_db):
    ''' add a transaction to db, the select it'''
    tran0 = {"category":'testing_add',
            'item': 10,
            'amount': 199.67,
            'description': "This is a test",
            "date": "20220316"}
    cats0 = tran_db.select_all()
    rowid = tran_db.add(tran0)
    tran1 = tran_db.select_all()
    assert len(tran1) == len(cats0) + 1
    tran1 = tran_db.select_one(rowid)
    assert tran1['category']==tran0['category']
    assert tran1['description']==tran0['description']

@pytest.mark.delete_transaction
def test_delete_transaction(tran_db):
    ''' add a category to db, the select it, then delete it'''
    tran0 = {"category":'testing_delete',
            'item': 30,
            'amount': 450,
            'description': "This is a test",
            "date": "20220102"}
    rowid = tran_db.add(tran0)
    len1 = len(tran_db.select_all())
    deletedDict = tran_db.delete(rowid)
    len2 = len(tran_db.select_all())
    assert len1 == len2 + 1
    assert deletedDict['category']==tran0['category']
    assert deletedDict['description']==tran0['description']

@pytest.mark.sumByDate_transaction
def test_sumByDate_transaction(tran_db):
    ''' add a category to db, the select it, then delete it'''
    tuples = tran_db.sumByDate()
    date = tuples[0][0]
    sum = tuples[0][1]
    assert date == 20220316
    assert sum == 42751.4