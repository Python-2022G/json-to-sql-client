# Import libraries
import requests
from tinydb import TinyDB
from pprint import pprint


db = TinyDB('db.json')

tables = db.tables()
        
c = 0
for table in tables:
    collection = db.table(table)
    smartphones = collection.all()
    for smartphone in smartphones:
        smartphone['price'] = float(smartphone['price'][:-5].replace(' ', ''))
        smartphone['name'] = smartphone['brend']
        smartphone['ram'] = int(smartphone['ram'])
        smartphone['memory'] = int(smartphone['memory'])
        smartphone.pop('brend')
        c += 1
        
        response = requests.post('http://127.0.0.1:8000/add/', json=smartphone)
        print(smartphone['name'], response.status_code)
print(c)

