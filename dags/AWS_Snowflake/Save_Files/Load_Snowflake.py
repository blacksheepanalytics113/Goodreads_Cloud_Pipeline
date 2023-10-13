import json
import requests
from pprint import pprint
import psycopg2
import datetime
import snowflake.connector
from SaveRead_File import read_json
# from ReadTransform import html_transform


def save_json_snowflake():
    print('Connecting to the Snowflake Warehouse...')
    # try:
            # Replace with your Snowflake connection details
    conn = snowflake.connector.connect(
        user='ACCOUNTADMIN',
        password='Ajiye2023',
        account='https://br51793.central-us.azure.snowflakecomputing.com',
        warehouse='COMPUTE_WH',
        database='S3_LOAD',
        schema='PUBLIC'
    )
    cur = conn.cursor()   
    # file_name = download_file('products','Products')
    file_name = 'authors.json'
    json_object = read_json(file_name)
    print(json_object)
        
        
        # for json in json_object:
        #     for list in json['data']:
        #         product_category = list['category']['name']
                
        #         cur.execute('SELECT * from "Products"  where "Food_Id" = %s',[list['id']])
        #         Products = cur.fetchall()
        #         if len(Products) == 0:
        #             # print(list['name'])
        #             cur.execute('Insert Into "Products" ("Name", "Description", "Barcode","price","Food_Id","Prod_Category","Status","Source") values (%s,%s,%s,%s,%s,%s,%s,%s)',([list['name'],str(list['description']),str(list['barcode']),list['price'],list['id'],product_category,0,'Foodics']))
        #             conn.commit()
        #             print(list['name'])
        #             cur.execute('Update "Upload_Meta" Set "Status" = %s where "FileName" = %s',[1,file_name])
    conn.commit()
            
        # close the communication with the PostgreSQL
    cur.close()

    # except (Exception,snowflake.connector.errors.OperationalError) as error:
    #         print(error)
    # # finally:
    # #         if conn is not None:
    conn.close()
    print('Warehouse connection closed.')
save_json_snowflake()


