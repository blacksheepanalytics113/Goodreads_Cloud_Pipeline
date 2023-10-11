import boto3
import requests
from datetime import date 

s3 = boto3.client('s3')

def save_file():
  
    url = 'https://www.goodreads.com/list/show/183940.Best_Books_of_2023'

    response = requests.get(url)
    responses = response.text
    if response.status_code == 200:
        response ='raww.html'
        
        with open(response, 'w', encoding='utf-8') as output_file:
            output_file.write(responses)
            
        print(f'Successfully saved the HTML content to {url}')
    else:
        print(f'Failed to retrieve the web page. Status code: {url}')
save_file()



def read_json():
     f = open ('raww.html', "r")
     # Reading from file
     data = f.read()
     f.close()
     # print(data)
     
     return data
read_json()