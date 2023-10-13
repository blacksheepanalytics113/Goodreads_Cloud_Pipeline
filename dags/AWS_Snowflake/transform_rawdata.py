import boto3
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import csv
import os
import requests
import json
from Save_Files.SaveRead_File import save_file
from Save_Files.SaveRead_File import read_json
from upload_rawdata import upload_file

# s3 = boto3.client('s3')

def html_transform():
    # Read File Function Exeuted 
    json_object = read_json()
    # print(json_object)
    
    # Parse through Data and get titles
    soup = BeautifulSoup(json_object, 'html.parser')
    tr_items = soup.find_all('tr', itemscope=True)
    titles = [a['title'] for tr in tr_items for a in tr.find_all('a', title=True)]
    # print(titles)
    
    book_name = titles[::6]
    # print(book_name)
    api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    
    gb_api = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=ebooks')
    # print(gb_api)
    service = build('books', 'v1', developerKey=api_key)
    
    # print(book_name)
    
    author_name = list()
    publisher_name = list()
    published_date = list()
    book_description = list()
    book_genre = list()
    
    
    
    for i in book_name:
        query = f'intitle:"{i}"'
        results = service.volumes().list(q=query).execute()
        items = results.get('items', [])
        # print(items)
        
        if items:
            authors = items[0]['volumeInfo'].get('authors', [])
            publisher = items[0]['volumeInfo'].get('publisher',[])
            date = items[0]['volumeInfo'].get('publishedDate', [])
            description = items[0]['volumeInfo'].get('description', [])
            genre = items[0]['volumeInfo'].get('categories', [])
            
            author_name.append(authors)
            publisher_name.append(publisher)
            published_date.append(date)
            book_description.append(description)
            book_genre.append(genre)
            
        else:
            author_name.append([])
            publisher_name.append([])
            published_date.append([])
            book_description.append([])
            book_genre.append([])
    
    book_genre = [genre[0] if genre else None for genre in book_genre]
    author_name = [','.join(sub_authors) if sub_authors else None for sub_authors in author_name]
    print(json.dumps(author_name))
    
    # Convert transformed files to json 
    bk_json = json.dumps(book_name)
    print(bk_json)
    
    auth_json = json.dumps(author_name)
    pblr_json = json.dumps(publisher_name)
    pbldt_json = json.dumps(published_date)
    desc_json = json.dumps(book_description)
    gnr_json = json.dumps(book_genre)
    
    # save files
    # if bk_json == json.dumps(book_name):
    # bk_json = 'books.json'
    # with open(bk_json, 'w', encoding='utf-8') as output_file:
    #             output_file.write(bk_json)
    # print(f'Successfully saved the Json File to {bk_json}')
    # else:
    #     print(f'Failed to retrieve the web page. Status code: {bk_json}')
        
    
    # auth_json= 'Authors.json'
    # with open(auth_json, 'w', encoding='utf-8') as output_file:
    #         output_file.write(auth_json)
    # print(f'Successfully saved the Json File to {auth_json}')
    
    # pblr_json= 'publishers.json'
    # with open(pblr_json, 'w', encoding='utf-8') as output_file:
    #         output_file.write(pblr_json)
    # print(f'Successfully saved the Json File to {pblr_json}')
    
html_transform()
          




    