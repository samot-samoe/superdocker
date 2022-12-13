from ast import Str
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
password = {"databases/DB.yaml":"postgres"}
url = 'http://localhost:27364/'

payload = {
    'username': os.getenv('SUPERSET_USER'),
    'password': os.getenv('SUPERSET_PASSWORD'),
    # 'username':'admin',
    # 'password':'admin',
    'provider': 'db'
}
r = requests.post(url+'api/v1/security/login',json=payload)
# r = requests.post('http://localhost:27364/api/v1/security/login',json=payload)
access_token = r.json()
# print(access_token)
headerAuth ={
    'Authorization':'Bearer '+ str(access_token['access_token']),
    # 'Referrer': 'http://localhost:27364/api/v1/security/login'
}

headerData={
    'Referrer': url+'api/v1/security/login/',
    # 'Referrer': 'http://localhost:27364/api/v1/security/login',
    'Authorization':'Bearer '+str(access_token['access_token']),
    # 'X-CSRFToken': str(csrf_token['result']),
    'Content-type':'application/json'
}
# requests.post(url+'api/v1/database/',headers=headerData,json=data_out)   
requests.get(url+'api/v1/dashboard/export/',headers = headerData)