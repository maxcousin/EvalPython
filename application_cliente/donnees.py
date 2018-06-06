import requests

def getDonnees():
    r = requests.get('http://127.0.0.1:5000/readData')
    return r.json()

#print(getDonnees())