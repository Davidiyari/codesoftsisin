import json
from hashlib import md5
from  requests import get 
from datetime  import datetime 

class RestMarvel:
    timestamp=datetime.now().strtime('%Y-%m-%d%H:%M:%S')
    pub_key = '038be6b0436d0e725cb554e8c'
    priv_key='+84568456465456564564564564465'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update (f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params

    def get_heroes(self):
        params = {'ts0':self.timestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        result = get('https://gateway.marvel.com:443/v1/public/characters',
    params=params)
        
        data = result.json()
        print = (data)
        print(data['status'])

get=RestMarvel
get.get_heroes