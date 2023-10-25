import pyodbc
import pymssql
##https://learn.microsoft.com/zh-tw/sql/connect/python/pymssql/step-3-proof-of-concept-connecting-to-sql-using-pymssql?view=sql-server-ver16
##https://www.cnblogs.com/zhengbiqing/p/11156107.html
import pathlib
from pathlib import Path
import os
import numpy as np

##1025

def conn():

    # connect = pymssql.connect(
    # server='localhost:1433',
    # user=r'domain\\DESKTOP-ESET18D',
    # password='pass',
    # database='skin_care_db',
    # charset='CP936'
# )
    connect = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=localhost;'
            'DATABASE=skin_care_db;'
            'Trusted_Connection=yes;'
    )
    if connect:

        print("連線成功")

    else:

        print("連線失敗")

    return connect


def insert_brand_to_db(brand_name):

    with connect_db.cursor() as cursor:

        if len(select_brand(brand_name)) == 0:

            query = f'INSERT INTO Brand_table (brand) VALUES (?)'
            cursor.execute(query, brand_name)
            connect_db.commit()
            print("新增成功")
            
        else:
            print("已有此品牌")
            print("---------------------")

def select_brand(brand_name):


    with connect_db.cursor() as cursor:
        
    
        query = f'SELECT * FROM Brand_table where brand = ?'

        cursor.execute(query, brand_name)


        results = cursor.fetchall()

        print(results)

    return results

if __name__ == "__main__":
    
    brand_name = ['SK2','PARIS','LANCOME','CLINIQUE','KIEHL','SHISEIDO','LA MER','DIOR','ESTEE LAUDER','CLARINS','YSL']

    connect_db = conn()

    for i in brand_name:
        insert_brand_to_db(i)

    #select_brand(brand_name)
    #insert_brand_to_db(brand_name)

    connect_db.close()