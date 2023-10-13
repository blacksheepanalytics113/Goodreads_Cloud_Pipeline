import json
import requests
# from Goodreads_AWS_Snowflake.transform_rawdata import html_transform
from transform_rawdata import html_transform

def save_jsonn():
     #Serialize Json Data 
    Data_json_string = json.dumps(bk_json)
    # if bk_json == True:
    bk_json ='Bookname.json'
     # print(Modifier_json_string)
     
    with open(bk_json, 'w', encoding='utf-8') as output_file:
            output_file.write(bk_json)
            
            print(f'Successfully saved the HTML content to {bk_json}')
    # else:
    #         print(f'Failed to retrieve the web page. Status code: {url}')
save_jsonn()
  
  