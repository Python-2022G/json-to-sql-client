# Import libraries
import requests
from tinydb import TinyDB
from pprint import pprint
# Define a function to get the data from the database
def get_data(path: str ,brand: str):
    # Get the data from the database
    db = TinyDB('db.json')
  
    # Get list of tables
    tables = db.tables()
    data = {}
    for table in tables:
        data[table] = db.table(table).all()
    
    # # Return the data
    return data

db = get_data(path='db.json',brand='apple')

# Add the data to the database through the API

BASE_URL = 'http://localhost:8000/api/add'
for data in db.values():
    for idx,item in enumerate(data):
        item['name']=item['brend'] 
        price = item['price']        
        item['price']=float(price[:-5].replace(' ',''))
        response = requests.post(BASE_URL, json=item)
        
        # Print progress to the console
        print(f'Progress: {idx+1}/{len(data)} \t Status: {response.status_code}')
        
        

