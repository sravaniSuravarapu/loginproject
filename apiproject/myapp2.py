import requests
import json

URL ="http://127.0.0.1:8000/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = { 'id': id} 
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    print("when its els ")
    data = r.json()
    print(data)
        
get_data(1)


def add_data():
    data ={
    'fname': 'sra',
    'sname': 'sura',
    'ph_no': 9390,
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL , data = json_data)

#add_data()

def update_data():
    data ={
    'id': 2,
    'sname': 'mahesh babu',
    
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL , data = json_data)

#update_data()



def delete_data():
    data ={
    'id': 2,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL , data = json_data)

#delete_data()