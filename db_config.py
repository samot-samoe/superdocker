from ast import Str
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = 'http://ccrii1.ranepa.ru:27364/'

payload = {
    # 'username': os.getenv('SUPERSET_USER'),
    # 'password': os.getenv('SUPERSET_PASSWORD'),
    'username':'admin',
    'password':'admin',
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

r2=requests.get(url+"api/v1/database/",headers=headerAuth)
# r2=requests.get('http://localhost:27364/api/v1/database',headers=headerAuth)
resp_chart=r2.json()

r3 = requests.get(url+'api/v1/security/csrf_token/',headers = headerAuth)
# r3 = requests.get('http://localhost:27364/api/v1/security/csrf_token',headerAuth)
r3.json()
csrf_token = r3.json()
print(csrf_token)
headerData={
    'Referrer': url+'api/v1/security/login/',
    # 'Referrer': 'http://localhost:27364/api/v1/security/login',
    'Authorization':'Bearer '+str(access_token['access_token']),
    'X-CSRFToken': str(csrf_token['result']),
    # 'Content-type':'application/json'
}

username = "admin"
password = "admin"
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')
db_name = os.getenv('POSTGRES_DB')

sqlalchemy_url = "postgresql://" + db_user + ":" + db_password + "@" + db_host + ":" + str(db_port)+"/" + db_name


data_out = {
    #   "allow_csv_upload": True,
      "allow_ctas": True,
      "allow_cvas": True,
      "allow_dml": True,
      "allow_file_upload": True,
      "allow_multi_schema_metadata_fetch": True,
      "allow_run_async": False,
      "cache_timeout": 0,
    #   "configuration_method": "sqlalchemy_form",
      "database_name": "DB",
    #   "engine":"postgresql",
      "expose_in_sqllab": True,
      "sqlalchemy_uri": "postgresql://postgres:postgres@postgres:5432/db",
      "impersonate_user": False,
    #   "is_managed_externally": True, 
      "uuid": "2da16a65-2163-4f72-8b12-d05fb10e0c7d"
    }
r4 = requests.post(url+'api/v1/database/',headers=headerData,json=data_out)  
result = r4.json()
print(result)

# # ---------------------Dataset---------------------
# headerDataset={
#     'Referrer': url+'api/v1/security/login/',
#     # 'Referrer': 'http://localhost:27364/api/v1/security/login',
#     'Authorization':'Bearer '+str(access_token['access_token']),
#     'X-CSRFToken': str(csrf_token['result']),
#     'Content-type':'multipart/form-data'
# }
# file = {'dataset_export_20221101T212029.zip':open('/home/samo/Desktop/superset/tired/dataset_export_20221101T212029.zip', 'rb')}
# password = {"databases/DB.yaml": "postgres"}
# # /home/samo/Desktop/superset/tired/dataset_export_20221101T212029.zip
# requests.post(url+'api/v1/dataset/import/',headers=headerDataset,data = password,files = file)
# # requests.post(url+'api/v1/dataset/import/',headers=headerDataset,data = password,files = {'file':open('/home/samo/Desktop/superset/tired/customer_clustering.yaml')})

file_name = '/home/samo/Desktop/superset/tired/students_data.json'
# json.loa

# with open(file_name, 'r') as f:
#     myjson = json.load(f)
#     # print(myjson[2])
#     # print(len(myjson))
#     print(myjson[0]["roles"])
#     for l in myjson:
#         # print(json.loads(l))
#         user_dct = l
#         # 
#         # 
#         payload = {"first_name": user_dct["first_name"],
#                    "last_name": user_dct["last_name"],
#                    "username": user_dct["username"],
#                    "email": user_dct["email"],
#                    "active": 'y',
#                    "conf_password": user_dct["password"],
#                    "password": user_dct["password"],
#                    "roles": user_dct["roles"]
#                   } 
#         requests.post(url=url+'users/add', json=payload)#,headers=headerAuth)