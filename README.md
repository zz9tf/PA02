# PA02 Read me

## This is a Finance Tracker app, which can record and track transactions whith 11 functions:

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

**Each row of the transactions has these detailed information:**

```'item #','amount','category','date','description'```

- Using this app, you can show, add or modify the categories by inputting 1, 2 or 3.
- Using this app, you can show, add, delete the transactions by inputting 4, 5 or 6. 
- You can input 9, 8 or 7 to track the summaries of transactions by year, month or date. 
- You can quit this app by inputting 0 and print the menu of all the functions by inputting 11.


## Script
#### All features in tracker.py
(base) floradembp:PA02 flora$ ls
README.md		script_Nan		test_transactions.py
__pycache__		script_Qishi		tracker.py
category.db		script_Zheng		transaction.db
category.py		script_Zixin		transactions.py
pytest.ini		test.db
requirement.md		test_category.py
(base) floradembp:PA02 flora$ python3 tracker.py

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

> 1
id  name       description                   
---------------------------------------------
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
> 11

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

> 0
(base) floradembp:PA02 flora$ script
Script started, output file is typescript

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bash-3.2$ ls
README.md		script_Nan		test_transactions.py
__pycache__		script_Qishi		tracker.py
category.db		script_Zheng		transaction.db
category.py		script_Zixin		transactions.py
pytest.ini		test.db			typescript
requirement.md		test_category.py
bash-3.2$ python3 tracker.py

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

> 1
id  name       description                   
---------------------------------------------
> 2
category name: cat
category description: my pet               
> 1
id  name       description                   
---------------------------------------------
1   cat        my pet                        
> 3
modifying category
rowid: 1
new category name: my pet
new category description: a cat
> 1
id  name       description                   
---------------------------------------------
1   my pet     a cat                         
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
> 5
-- add transaction --
item #: 4
the amount of new item: 50
category: food
new item description: bread
date of this update(yyyymmdd): 20220325
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
4          4          50         food       20220325   bread                         
> 6
-- delete transaction --
the id you want to delete: 4
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
> 7
-- summarize transactions by date --
date       sum       
---------------
20220224   250       
20220228   30        
> 8
-- summarize transactions by month --
month      sum       
---------------
2          280       
> 9
-- summarize transactions by year --
year       sum       
---------------
2022       280       
> 10
-- summarize transactions by category --
date       sum       
---------------
food       280       
> 11

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

> 0
bash-3.2$ ls
README.md		script_Nan		test_transactions.py
__pycache__		script_Qishi		tracker.py
category.db		script_Zheng		transaction.db
category.py		script_Zixin		transactions.py
pytest.ini		test.db			typescript
requirement.md		test_category.py
bash-3.2$ pylint tracker.py
************* Module tracker
tracker.py:127:65: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:44:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:103:8: W0622: Redefining built-in 'id' (redefined-builtin)
tracker.py:111:12: W0622: Redefining built-in 'tuple' (redefined-builtin)
tracker.py:62:0: R0914: Too many local variables (16/15) (too-many-locals)
tracker.py:103:8: C0103: Variable name "id" doesn't conform to snake_case naming style (invalid-name)
tracker.py:62:0: R0912: Too many branches (17/12) (too-many-branches)
tracker.py:62:0: R0915: Too many statements (64/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.17/10 (previous run: 9.08/10, +0.09)

bash-3.2$ pylint transactions.py
************* Module transactions
transactions.py:16:0: C0301: Line too long (110/100) (line-too-long)
transactions.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:103:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:108:0: C0301: Line too long (110/100) (line-too-long)
transactions.py:113:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:123:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:87:8: C0103: Variable name "deletedDict" doesn't conform to snake_case naming style (invalid-name)
transactions.py:94:4: C0103: Method name "sumByDate" doesn't conform to snake_case naming style (invalid-name)
transactions.py:104:4: C0103: Method name "sumByMonth" doesn't conform to snake_case naming style (invalid-name)
transactions.py:111:8: W0104: Statement seems to have no effect (pointless-statement)
transactions.py:114:4: C0103: Method name "sumByYear" doesn't conform to snake_case naming style (invalid-name)
transactions.py:124:4: C0103: Method name "sumByCat" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 8.50/10

bash-3.2$ pytest -v test_transactions.py
============================= test session starts ==============================
platform darwin -- Python 3.9.5, pytest-6.2.5, py-1.9.0, pluggy-1.0.0 -- /Users/flora/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/flora/Brandeis/103a_Fundamentals of Software Engineering/103hw/PA02, configfile: pytest.ini
collected 6 items                                                              

test_transactions.py::test_add_transaction PASSED                        [ 16%]
test_transactions.py::test_delete_transaction PASSED                     [ 33%]
test_transactions.py::test_sumByDate_transaction PASSED                  [ 50%]
test_transactions.py::test_sumByMonth_transaction PASSED                 [ 66%]
test_transactions.py::test_sumByYear_transaction PASSED                  [ 83%]
test_transactions.py::test_sumByCat_transaction PASSED                   [100%]

============================== 6 passed in 0.20s ===============================
bash-3.2$ exit
exit

Script done, output file is typescript
(base) floradembp:PA02 flora$ cat tyscript
cat: tyscript: No such file or directory
(base) floradembp:PA02 flora$ cat typescript
Script started on Fri Mar 25 10:12:57 2022

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bash-3.2$ ls
README.md		script_Nan		test_transactions.py
__pycache__		script_Qishi		tracker.py
category.db		script_Zheng		transaction.db
category.py		script_Zixin		transactions.py
pytest.ini		test.db			typescript
requirement.md		test_category.py
bash-3.2$ python3 tracker.py

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

> 1
id  name       description                   
---------------------------------------------
> 2
category name: cat
category description: my pet               
> 1
id  name       description                   
---------------------------------------------
1   cat        my pet                        
> 3
modifying category
rowid: 1
new category name: my pet
new category description: a cat
> 1
id  name       description                   
---------------------------------------------
1   my pet     a cat                         
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
> 5
-- add transaction --
item #: 4
the amount of new item: 50
category: food
new item description: bread
date of this update(yyyymmdd): 20220325
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
4          4          50         food       20220325   bread                         
> 6
-- delete transaction --
the id you want to delete: 4
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
> 7
-- summarize transactions by date --
date       sum       
---------------
20220224   250       
20220228   30        
> 8
-- summarize transactions by month --
month      sum       
---------------
2          280       
> 9
-- summarize transactions by year --
year       sum       
---------------
2022       280       
> 10
-- summarize transactions by category --
date       sum       
---------------
food       280       
> 11

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

> 0
bash-3.2$ ls
README.md		script_Nan		test_transactions.py
__pycache__		script_Qishi		tracker.py
category.db		script_Zheng		transaction.db
category.py		script_Zixin		transactions.py
pytest.ini		test.db			typescript
requirement.md		test_category.py
bash-3.2$ pylint tracker.py
************* Module tracker
tracker.py:127:65: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:44:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:103:8: W0622: Redefining built-in 'id' (redefined-builtin)
tracker.py:111:12: W0622: Redefining built-in 'tuple' (redefined-builtin)
tracker.py:62:0: R0914: Too many local variables (16/15) (too-many-locals)
tracker.py:103:8: C0103: Variable name "id" doesn't conform to snake_case naming style (invalid-name)
tracker.py:62:0: R0912: Too many branches (17/12) (too-many-branches)
tracker.py:62:0: R0915: Too many statements (64/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.17/10 (previous run: 9.08/10, +0.09)

bash-3.2$ pylint transactions.py
************* Module transactions
transactions.py:16:0: C0301: Line too long (110/100) (line-too-long)
transactions.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:103:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:108:0: C0301: Line too long (110/100) (line-too-long)
transactions.py:113:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:123:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:87:8: C0103: Variable name "deletedDict" doesn't conform to snake_case naming style (invalid-name)
transactions.py:94:4: C0103: Method name "sumByDate" doesn't conform to snake_case naming style (invalid-name)
transactions.py:104:4: C0103: Method name "sumByMonth" doesn't conform to snake_case naming style (invalid-name)
transactions.py:111:8: W0104: Statement seems to have no effect (pointless-statement)
transactions.py:114:4: C0103: Method name "sumByYear" doesn't conform to snake_case naming style (invalid-name)
transactions.py:124:4: C0103: Method name "sumByCat" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 8.50/10

bash-3.2$ pytest -v test_transactions.py
============================= test session starts ==============================
platform darwin -- Python 3.9.5, pytest-6.2.5, py-1.9.0, pluggy-1.0.0 -- /Users/flora/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/flora/Brandeis/103a_Fundamentals of Software Engineering/103hw/PA02, configfile: pytest.ini
collected 6 items                                                              

test_transactions.py::test_add_transaction PASSED                        [ 16%]
test_transactions.py::test_delete_transaction PASSED                     [ 33%]
test_transactions.py::test_sumByDate_transaction PASSED                  [ 50%]
test_transactions.py::test_sumByMonth_transaction PASSED                 [ 66%]
test_transactions.py::test_sumByYear_transaction PASSED                  [ 83%]
test_transactions.py::test_sumByCat_transaction PASSED                   [100%]

============================== 6 passed in 0.20s ===============================
bash-3.2$ exit
exit

Script done on Fri Mar 25 10:19:31 2022
(base) floradembp:PA02 flora$ cat typescript
Script started on Fri Mar 25 10:12:57 2022

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bash-3.2$ ls
README.md		script_Nan		test_transactions.py
__pycache__		script_Qishi		tracker.py
category.db		script_Zheng		transaction.db
category.py		script_Zixin		transactions.py
pytest.ini		test.db			typescript
requirement.md		test_category.py
bash-3.2$ python3 tracker.py

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

> 1
id  name       description                   
---------------------------------------------
> 2
category name: cat
category description: my pet               
> 1
id  name       description                   
---------------------------------------------
1   cat        my pet                        
> 3
modifying category
rowid: 1
new category name: my pet
new category description: a cat
> 1
id  name       description                   
---------------------------------------------
1   my pet     a cat                         
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
> 5
-- add transaction --
item #: 4
the amount of new item: 50
category: food
new item description: bread
date of this update(yyyymmdd): 20220325
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
4          4          50         food       20220325   bread                         
> 6
-- delete transaction --
the id you want to delete: 4
> 4
-- show transactions --


rowid      item       amount     category   date       description                   
----------------------------------------------------------------------
1          00001234   100        food       20220224   sth                           
2          00001288   150        food       20220224   sth else                      
3          00004345   30         food       20220228   sth....                       
> 7
-- summarize transactions by date --
date       sum       
---------------
20220224   250       
20220228   30        
> 8
-- summarize transactions by month --
month      sum       
---------------
2          280       
> 9
-- summarize transactions by year --
year       sum       
---------------
2022       280       
> 10
-- summarize transactions by category --
date       sum       
---------------
food       280       
> 11

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

> 0
bash-3.2$ ls
README.md		script_Nan		test_transactions.py
__pycache__		script_Qishi		tracker.py
category.db		script_Zheng		transaction.db
category.py		script_Zixin		transactions.py
pytest.ini		test.db			typescript
requirement.md		test_category.py

#### Pylint
bash-3.2$ pylint tracker.py
************* Module tracker
tracker.py:127:65: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:44:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:103:8: W0622: Redefining built-in 'id' (redefined-builtin)
tracker.py:111:12: W0622: Redefining built-in 'tuple' (redefined-builtin)
tracker.py:62:0: R0914: Too many local variables (16/15) (too-many-locals)
tracker.py:103:8: C0103: Variable name "id" doesn't conform to snake_case naming style (invalid-name)
tracker.py:62:0: R0912: Too many branches (17/12) (too-many-branches)
tracker.py:62:0: R0915: Too many statements (64/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.17/10 (previous run: 9.08/10, +0.09)

bash-3.2$ pylint transactions.py
************* Module transactions
transactions.py:16:0: C0301: Line too long (110/100) (line-too-long)
transactions.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:103:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:108:0: C0301: Line too long (110/100) (line-too-long)
transactions.py:113:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:123:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:87:8: C0103: Variable name "deletedDict" doesn't conform to snake_case naming style (invalid-name)
transactions.py:94:4: C0103: Method name "sumByDate" doesn't conform to snake_case naming style (invalid-name)
transactions.py:104:4: C0103: Method name "sumByMonth" doesn't conform to snake_case naming style (invalid-name)
transactions.py:111:8: W0104: Statement seems to have no effect (pointless-statement)
transactions.py:114:4: C0103: Method name "sumByYear" doesn't conform to snake_case naming style (invalid-name)
transactions.py:124:4: C0103: Method name "sumByCat" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 8.50/10

#### Pytest
bash-3.2$ pytest -v test_transactions.py
============================= test session starts ==============================
platform darwin -- Python 3.9.5, pytest-6.2.5, py-1.9.0, pluggy-1.0.0 -- /Users/flora/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/flora/Brandeis/103a_Fundamentals of Software Engineering/103hw/PA02, configfile: pytest.ini
collected 6 items                                                              

test_transactions.py::test_add_transaction PASSED                        [ 16%]
test_transactions.py::test_delete_transaction PASSED                     [ 33%]
test_transactions.py::test_sumByDate_transaction PASSED                  [ 50%]
test_transactions.py::test_sumByMonth_transaction PASSED                 [ 66%]
test_transactions.py::test_sumByYear_transaction PASSED                  [ 83%]
test_transactions.py::test_sumByCat_transaction PASSED                   [100%]

============================== 6 passed in 0.20s ===============================
bash-3.2$ exit
exit
