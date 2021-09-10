import pandas as pd

def toset(df):

    return set(df.tolist())

dev = pd.read_csv('./DB1.csv')
prod = pd.read_csv('./DB2.csv')

dev_tables = toset(dev['table'].unique())
prod_tables = toset(prod['table'].unique())

missing_tables = dev_tables - prod_tables

both_tables = dev_tables - missing_tables

tables_missing_columns = {}

for table in both_tables:

    dev_columns = toset(dev.loc[dev['table'] == table]['column'])
    prod_columns = toset(prod.loc[prod['table'] == table]['column'])

    table_missing_columns = dev_columns - prod_columns

    if(len(table_missing_columns) > 0):

        tables_missing_columns[table] = list(table_missing_columns)

print('MISSING TABLES:')
for table in missing_tables:

    print(' - ' + table)

print('\n')
print('MISSING COLUMNS:')

for table in tables_missing_columns:

    print(' - ' + table)

    for colum in tables_missing_columns[table]:

        print('   - ' + colum)