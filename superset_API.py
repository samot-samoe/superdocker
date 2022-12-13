import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment
import json
import os

class UserSupersetApi:
    def __init__(self, username=None, password=None):
        self.s = requests.Session()
        self.base_url = "http://localhost:27364/"
        self._csrf = self._getCSRF(self.url('login/'))
        self.headers = {'X-CSRFToken': self._csrf, 'Referer': self.url('login/')}
        # note: does not use headers because of flask_wtf.csrf.validate_csrf
        # if data is dict it is used as form and ends up empty but flask_wtf checks if data ...
        self.s.post(self.url('login/'),
        data={'username': username, 'password': password, 'csrf_token': self._csrf},
                   allow_redirects=False)
        
    def url(self, url_path):
        return self.base_url + url_path

    def get(self, url_path):
        return self.s.get(self.url(url_path), headers=self.headers)

    def post(self, url_path, data=None, json_data=None, **kwargs):
        kwargs.update({'url': self.url(url_path), 'headers': self.headers})
        if data:
            data['csrf_token'] = self._csrf
            kwargs['data'] = data
        if json_data:
            kwargs['json'] = json_data
        return self.s.post(**kwargs, allow_redirects=False)

    def _getCSRF(self, url_path):
        response = self.s.get(url_path)
        soup = bs(response.content, "html.parser")
        for tag in soup.find_all('input', id='csrf_token'):
            csrf_token = tag['value']
        return csrf_token
    
    '''
    builds User Name
    fails if 2 people have the same name
    '''
    @staticmethod  
    def build_username (first_name, last_name):
        return f'{first_name}_{last_name}'

## authenticate + set global vars

superset_username = os.getenv('SUPERSET_USER')
superset_pw = os.getenv('SUPERSET_PASSWORD')
file_name = 'students_data.json'

superset = UserSupersetApi(superset_username, superset_pw)

## create users based on file

# users = [
#     {
#     'first_name': 'one',
#     'last_name':'one',
#     'username': 'one',
#     'email': 'twoooofoppppppp@gdpost.com',
#     'password': 'one',
#     'conf_password': 'one',
#     'roles': [] 
#     },
#     {
#     'first_name': 'two',
#     'last_name':'two',
#     'username': 'two',
#     'email': 'twooooffo@gdpost.com',
#     'password': 'two',
#     'conf_password': 'two',
#     'roles': [] 
#     }
# ]
# for user in users:
#     payload = {'first_name': user['first_name'],
#                'last_name': user['last_name'],
#                'username': user['username'],
#                'email': user['email'],
#                'active': True,
#                'conf_password': user['password'],
#                'password': user['password'],
#                'roles': user['roles']} 
#     print(superset.post(url_path='users/add', json=payload))
    
# with open(file_name , 'r') as f:
#     for l in f:
#         user_dct = json.loads(l)
        
        
#         payload = {"first_name": user_dct["first_name"],
#                    "last_name": user_dct["last_name"],
#                    "username": user_dct["username"],
#                    "email": user_dct["email"],
#                    "active": 'y',
#                    "conf_password": user_dct["password"],
#                    "password": user_dct["password"],
#                    "roles": user_dct["roles"]
#                   } 

#         superset.post(url_path=f'users/add', json=payload)

file_name = '/home/samo/Desktop/superset/tired/students_data.json'
# json.loa

with open(file_name, 'r') as f:
    myjson = json.load(f)
    # print(myjson[2])
    # print(len(myjson))
    print(myjson[0]["roles"])
    for l in myjson:
        # print(json.loads(l))
        user_dct = l
        # 
        # 
        payload = {"first_name": user_dct["first_name"],
                   "last_name": user_dct["last_name"],
                   "username": user_dct["username"],
                   "email": user_dct["email"],
                   "active": 'y',
                   "conf_password": user_dct["password"],
                   "password": user_dct["password"],
                   "roles": user_dct["roles"]
                  } 
        superset.post(url_path=f'users/add', json=payload)


## delete users based on file

# provides pk given a username
# res = superset.get(url_path='users/api/read')
# 
# pks = res.json()['pks']
# users = res.json()['result']
# n_pk = len(pks)
# 
# build dict of all current users
# pk_lut = dict()
# for i in range(n_pk):
    # pk_lut[users[i]['email']] = pks[i]
    # 
# for all entries in file delete users from superset based on email
# with open(file_name , 'r') as f:
    # for l in f:
        # user_dct = json.loads(l)
        # pk = pk_lut[user_dct['email']]
        # superset.post(url_path=f'users/delete/{pk}')