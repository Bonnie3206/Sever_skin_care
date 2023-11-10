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

def delete(table_name,condition):
    ##更新之前先刪掉舊資料
    with connect_db.cursor() as cursor:
        query = f"DELETE from {table_name} WHERE {condition};"
        cursor.execute(query)
        connect_db.commit()
        print("刪除成功")
        
def insert_product_ingred_to_db(json_file):
    with connect_db.cursor() as cursor:

    ###將成分存入json檔###
        with open(json_file, "r", encoding="utf-8") as f:
            data=json.load(f)
            for i in data:
                
                product_name = i["name"]
                ingred_name = i["ingredient"]
            
                ###SELECT
                #Product_table中查詢叫做product_name的product_number
                query = f"SELECT product_number FROM Product_table where product_name = ?"
                cursor.execute(query, product_name)
                product_number_results = cursor.fetchone()
                product_number = int(product_number_results[0])

                for ingred in ingred_name:

                    #Ingredient_introduction_table中查詢叫做ingredient_en的ingredient_number
                    query = f"SELECT ingredient_number FROM Ingredient_introduction_table where ingredient_en = ?"
                    cursor.execute(query, ingred)
                    ingred_number_results = cursor.fetchone()
                    ingred_number = int(ingred_number_results[0])

                    print(f"product_name:{product_name},product_number:{product_number},ingred_name:{ingred},ingred_number:{ingred_number}")
                    print("---------------------")

                    ###INSERT
                    #Product_ingredient_table中新增product_number和ingred_number
                    query = f"INSERT INTO Product_ingredient_table (product_number,ingredient_number) VALUES (?,?)"
                    cursor.execute(query, (product_number,ingred_number))
                    connect_db.commit()
                    print("新增成功")
                    print("---------------------")

def insert_ingredient_intro_to_db(ingred_name, ingred_intro,ingred_name_en):
    with connect_db.cursor() as cursor:
        ##查詢Ingredient_introduction_table是否有叫做ingredient的成分
        query = f"SELECT * FROM Ingredient_introduction_table where ingredient = ?"
        cursor.execute(query, ingred_name)
        ingred_name_results = cursor.fetchall()

        print(ingred_name)
        if not ingred_name_results:  # 如果目前資料庫沒有此成分，則新增
            query = f"INSERT INTO Ingredient_introduction_table (ingredient,ingredient_introduction,ingredient_en) VALUES (?,?,?)"
            cursor.execute(query, (ingred_name, ingred_intro, ingred_name_en))
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


def insert_product_to_db(json_file):

    with connect_db.cursor() as cursor:

        # 打開json檔，並將資料存入cosmetics_data
        # 依據cosmetics_data的長度跑迴圈，並將每個商品名稱存入product_name
        
        with open(json_file, "r", encoding="utf-8") as json_file:

            cosmetics_data = json.load(json_file)

        for i in cosmetics_data:

            product_name = i["name"]
            img_url = i["img_url"]

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
            product_name_results = cursor.fetchone()#一筆資料傳入
            product_number_results = int(product_name_results[0])#取出product_number
            print(product_name)
            
            if len(product_name_results) == 0:  # 如果目前資料庫沒有此商品，則新增
                query = (
                    f"INSERT INTO Product_table (brand_number,product_name,img_url) VALUES (?,?,?)"
                )
                cursor.execute(query, (brand_number_results, product_name))
                connect_db.commit()
                print("新增成功")
                print("---------------------")

            else:
                print("已有此商品,新增img_url")
                query = (

                    f"UPDATE Product_table SET img_url = ? WHERE product_number = ?"
                )
                cursor.execute(query, (img_url, product_number_results))
                connect_db.commit()
                print("---------------------")




if __name__ == "__main__":
    connect_db = conn()
    ###ingredient_introduction_table###
    # prefer_ingred = getProduct.new_ingred
    # for ingred in prefer_ingred:
    #     insert_ingredient_intro_to_db(ingred["name"], ingred["introduction"],ingred["name_en"])

    ###insert_product_ingred_to_db

    # insert_product_ingred_to_db("ingred_paris.json")

    ######insert_product_to_db#######

    insert_product_to_db("ingred_paris.json")
    
    #######insert_brand_to_db#######
    # brand_name = ['SK2','PARIS','LANCOME','CLINIQUE','KIEHL','SHISEIDO','LA MER','DIOR','ESTEE LAUDER','CLARINS','YSL']

    # for i in brand_name:
    #     insert_brand_to_db(i)

    # select_brand(brand_name)

    # connect_db.close()
