## Column Checker

The pourpose of this script is to check if two databases have the same columns and tables. 

### How to use

First, you need to export all tables and its respective columns of both databases you want to check. 

You can do this by running 

```
select TABLE_NAME as [table], COLUMN_NAME as [column]
from INFORMATION_SCHEMA.COLUMNS
```

on your database IDE and then export the result in .csv. 

The first database must have the name "DB1.csv" and the other "DB2.csv". Paste both files in the folder of this script. 

Then, run `python3 check_columns.py` and see the results. 

### Requirements

- Python 3
- Pandas library (if you don't have it run `pip3 install pandas`)

