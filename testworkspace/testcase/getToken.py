#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests

def getToken():
    token = ""
    url = 'http://120.55.42.27/caifu/user/signIn'
    data = {
        'name': '13572489850',
        'password': 123456
    }
    response = requests.post(url=url, data=data)
    if response.status_code == 200:
        dict = response.json()['properties']
        token = dict[0]['token']
    return token