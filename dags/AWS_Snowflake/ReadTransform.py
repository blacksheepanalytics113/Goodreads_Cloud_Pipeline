import boto3
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import csv
import os
import requests
import json
from upload_rawdata import upload_file
from Save_Files.SaveRead_File import read_json
from Save_Files.SaveRead_File import save_file





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
    api_key = 'AIzaSyA_l_f-3hNQwmS2z2DAWjcM_wfyaftCS2w'
    
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
    print(author_name)
    
    # namee = author_name
    # Convert the list to a JSON object
    author_namee = {"names": author_name}
    publisher_name = {"names": publisher_name}
    book_name = {"names": book_name}
    published_date =  {"names": published_date}
    book_description = {"names": book_description}
    book_genre = {"names": book_genre}

    # Convert transformed files to json 
    bk_json = json.dumps(book_name,indent =4)
    print(bk_json)
    auth_json = json.dumps(author_namee,indent=4)
    # print(auth_json)
    pblr_json = json.dumps(publisher_name,indent =4 )
    pbldt_json = json.dumps(published_date,indent = 4)
    desc_json = json.dumps(book_description,indent =4 )
    gnr_json = json.dumps(book_genre,indent=4)        
    
    # Save the JSON string to a file
    
    with open("author_name.json", "w") as json_file:
        json_file.write(auth_json)
    with open("books.json", "w") as json_file:
        json_file.write(bk_json)
    with open("published_date.json", "w") as json_file:
        json_file.write(pbldt_json)
    with open("publisher_name.json", "w") as json_file:
        json_file.write(pblr_json)
    with open("book_genre.json", "w") as json_file:
        json_file.write(gnr_json)
    with open("book_description.json", "w") as json_file:
        json_file.write(desc_json)
# print("JSON data has been saved to 'author_name.json'")







html_transform()
