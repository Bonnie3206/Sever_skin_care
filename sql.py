import pyodbc
import pymssql
import json

##https://learn.microsoft.com/zh-tw/sql/connect/python/pymssql/step-3-proof-of-concept-connecting-to-sql-using-pymssql?view=sql-server-ver16
##https://www.cnblogs.com/zhengbiqing/p/11156107.html
import pathlib
from pathlib import Path
import os
import numpy as np
import json
import getProduct

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
        "DRIVER={SQL Server};"
        "SERVER=localhost;"
        "DATABASE=skin_care_db;"
        "Trusted_Connection=yes;"
    )
    if connect:
        print("連線成功")

    else:
        print("連線失敗")

    return connect


def insert_ingredient_intro_to_db(ingred_name, ingred_intro):
    with connect_db.cursor() as cursor:
        ##查詢Ingredient_introduction_table是否有叫做ingredient的成分
        query = f"SELECT * FROM Ingredient_introduction_table where ingredient = ?"
        cursor.execute(query, ingred_name)
        ingred_name_results = cursor.fetchall()

        print(ingred_name)
        if not ingred_name_results:  # 如果目前資料庫沒有此成分，則新增
            query = f"INSERT INTO Ingredient_introduction_table (ingredient,ingredient_introduction) VALUES (?,?)"
            cursor.execute(query, (ingred_name, ingred_intro))
            connect_db.commit()
            print("新增成功")
            print("---------------------")

        else:
            print("已有此成分")
            print("---------------------")


def insert_brand_to_db(brand_name):
    with connect_db.cursor() as cursor:
        if len(select_brand(brand_name)) == 0:  # 如果目前資料庫沒有此品牌，則新增
            query = f"INSERT INTO Brand_table (brand) VALUES (?)"
            cursor.execute(query, brand_name)
            connect_db.commit()
            print("新增成功")

        else:
            print("已有此品牌")
            print("---------------------")


def select_brand(brand_name):
    with connect_db.cursor() as cursor:
        query = f"SELECT * FROM Brand_table where brand = ?"

        cursor.execute(query, brand_name)  # 查詢是否有叫做brand_name的品牌

        results = cursor.fetchall()

        print(results)

    return results


def insert_product_to_db(product_name, ingred):
    with connect_db.cursor() as cursor:
        brand = "PARIS"
        ###SELECT
        ##查詢是否有叫做brand_name的品牌，並將該品牌的brand_number取至brand_number_results
        query = f"SELECT brand_number FROM Brand_table where brand = ?"
        cursor.execute(query, brand)
        brand_number_results = cursor.fetchone()
        brand_number_results = int(brand_number_results[0])

        ##依據該brand_numeber查詢是否有叫做product_name的商品
        query = f"SELECT * FROM Product_table where product_name = ?"
        cursor.execute(query, product_name)
        product_name_results = cursor.fetchall()

        print(product_name)
        if len(product_name_results) == 0:  # 如果目前資料庫沒有此商品，則新增
            query = (
                f"INSERT INTO Product_table (brand_number,product_name) VALUES (?,?)"
            )
            cursor.execute(query, (brand_number_results, product_name))
            connect_db.commit()
            print("新增成功")
            print("---------------------")

            print("ingred")
            print(ingred)
            print("---------------------")

            query = f"INSERT INTO Product_table (product_name,ingred) VALUES (?,?)"

        else:
            print("已有此商品")
            print("---------------------")


if __name__ == "__main__":
    connect_db = conn()
    ###ingredient_introduction_table###
    prefer_ingred = getProduct.prefer_ingred
    for ingred in prefer_ingred:
        insert_ingredient_intro_to_db(ingred["name"], ingred["introduction"])

    #######insert_product_to_db#######

    # 打開json檔，並將資料存入cosmetics_data
    # 依據cosmetics_data的長度跑迴圈，並將每個商品名稱存入product_name

    # with open("ingred.json", "r", encoding="utf-8") as json_file:

    #     cosmetics_data = json.load(json_file)

    # for i in cosmetics_data:

    #     insert_product_to_db(i["name"],i["ingerdients"])

    #######insert_brand_to_db#######
    # brand_name = ['SK2','PARIS','LANCOME','CLINIQUE','KIEHL','SHISEIDO','LA MER','DIOR','ESTEE LAUDER','CLARINS','YSL']

    # for i in brand_name:
    #     insert_brand_to_db(i)

    # select_brand(brand_name)

    # connect_db.close()
