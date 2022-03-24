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
        s = str(1+i%3)
        cat ={'item': i,
            'amount': (1+i%3)*100,
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
    assert sum == 1900

@pytest.mark.subByMonth_transaction
def test_sumByMonth_transaction(tran_db):
    '''sum the accounts by month'''
    tuples = tran_db.sumByMonth()
    month = tuples[0][0]
    sum = tuples[0][1]
    assert month == 3
    assert sum == 1900
        
@pytest.mark.sumByYear_transaction
def test_sumByYear_transaction(tran_db):
    ''' sum the accounts by year'''
    tuples = tran_db.sumByYear()
    year = tuples[0][0]
    sum = tuples[0][1]
    assert year == 2022
    assert sum == 1900

@pytest.mark.sumByCat_transaction
def test_sumByCat_transaction(tran_db):
    tuples = tran_db.sumByCat()
    assert tuples[0][0] == 'category1'
    assert tuples[0][1] == 400
    assert tuples[1][0] == 'category2'
    assert tuples[1][1] == 600   
    assert tuples[2][0] == 'category3'
    assert tuples[2][1] == 900

