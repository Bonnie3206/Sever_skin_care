import pymssql
##https://learn.microsoft.com/zh-tw/sql/connect/python/pymssql/step-3-proof-of-concept-connecting-to-sql-using-pymssql?view=sql-server-ver16

conn = pymssql.connect(
    server='<server-address>',
    user='<username>',
    password='<password>',
    database='<database-name>',
    as_dict=True
)