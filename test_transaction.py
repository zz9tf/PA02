"""
test_transactions.py is a Pytest file

Methods in transaction.py will be tested here.

------ Written by Zixin.
"""

from transactions import Transaction
import pytest

def test_show_trans():
    ''' test show transactions ----- Written by Zixin '''
    t = Transaction("test.db")
    t.drop()
    tran1 = {"item": "00000001",
            "amount": 100,
            "category": "food",
            "date": 20220224,
            "description": "sth"}
    t.add(tran1)
    tran2 = {"item": "00000010",
            "amount": 20,
            "category": "vehicle",
            "date": 20220228,
            "description": "sth else"}
    t.add(tran2)
    res = t.select_all()
    assert res[0]["item"] == "00000001"
    assert res[0]["amount"] == 100
    assert res[0]["category"] == "food"
    assert res[0]["date"] == 20220224
    assert res[0]["description"] == "sth"
    assert res[1]["item"] == "00000010"
    assert res[1]["amount"] == 20
    assert res[1]["category"] == "vehicle"
    assert res[1]["date"] == 20220228
    assert res[1]["description"] == "sth else"

def test_delete():
    ''' test delete ----- Written by Zixin '''
    t = Transaction("test.db")
    t.drop()
    tran1 = {"item": "00000001",
            "amount": 100,
            "category": "food",
            "date": 20220224,
            "description": "sth"}
    t.add(tran1)
    tran2 = {"item": "00000002",
            "amount": 20,
            "category": "food",
            "date": 20220224,
            "description": "sth."}
    t.add(tran2)
    tran3 = {"item": "00000003",
            "amount": 300,
            "category": "food",
            "date": 20220228,
            "description": "sth.."}
    t.add(tran3)
    t.delete(1)
    t.delete(2)
    res = t.select_all()
    assert len(res) == 1
    assert res[0]["rowid"] == 3
    assert res[0]["item"] == "00000003"
    assert res[0]["amount"] == 300
    assert res[0]["category"] == "food"
    assert res[0]["date"] == 20220228
    assert res[0]["description"] == "sth.."


def test_sumByDate():
    ''' test sumByDate ----- Written by Zixin '''
    t = Transaction("test.db")
    t.drop()
    tran1 = {"item": "00000001",
            "amount": 100,
            "category": "food",
            "date": 20220224,
            "description": "sth"}
    t.add(tran1)
    tran2 = {"item": "00000002",
            "amount": 20,
            "category": "food",
            "date": 20220224,
            "description": "sth."}
    t.add(tran2)
    tran3 = {"item": "00000003",
            "amount": 300,
            "category": "food",
            "date": 20220228,
            "description": "sth.."}
    t.add(tran3)
    res = t.sumByDate()
    assert res[0][0] == 20220224
    assert res[0][1] == 120
    assert res[1][0] == 20220228
    assert res[1][1] == 300
