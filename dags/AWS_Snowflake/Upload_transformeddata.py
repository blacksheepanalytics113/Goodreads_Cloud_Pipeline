import boto3
from boto3 import session
from botocore.session import Session
from botocore.client import Config
from boto3.s3.transfer import S3Transfer
import datetime 
import requests
from datetime import date 
import configparser


def upload_file():
# def lambda_handler(event, context):
# global upload_file


    url = 'https://www.goodreads.com/list/show/183940.Best_Books_of_2023'
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
                # print(html_content)

    
        region_name='eu-north-1',
        ACCESS_ID = 'xxxxxxxxxxxxxxxxxxxxx',
        SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'
        folder_path = 'transformeddata/'

        # Replace with your S3 bucket name and desired file path
        bucket_name = 'goodreadsrawdata'
        file_name= 'C:\Users\user\Videos\Snowflake\Goodreads_AWS_Snowflake\Transformed_Files'
        key = f'{folder_path}/{file_name}'

        # Initialize the S3 client
        session = boto3.session.Session()
        s3Resource = boto3.resource('s3')
        s3= session.client('s3',region_name = 'eu-north-1',aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY)
        # s3 = boto3.client('s3',region_name = 'eu-north-1')
        transfer = S3Transfer(s3)
        
        # Upload the file to S3
        try:
            # s3.copy_object(Bucket = 'goodreadsrawdata', CopySource= f'{folder_path}/{file_name}', Key = html_content)
            transfer.upload_file(html_content ,'goodreadsrawdata',html_content)
            # client.put_object_acl(ACL='public-read',Bucket=bucket_name, Key=key, Body=html_content)
            print(f'status uploaded  from  {bucket_name} to {folder_path}') 
        except Exception as error:
            print(f'Error uploading from {bucket_name} to {folder_path}: {str(error)}')
upload_file()
    
        