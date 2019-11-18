#!/usr/bin/python
# -*- coding: utf-8 -*-
import json as JSON
import vk_api
import re
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

vk_session = vk_api.VkApi('login', 'pass')
vk_session.auth()
vk = vk_session.get_api()

i = 0
groups_file = open('groups.txt', 'r+')
y = groups_file.readlines()
e = 0
gender = input("êîãî ïàðñèì Æ èëè Ì ? åñëè Æ ââåäèòå 1 åñëè Ì ââåäèòå 2:  ")
gender=int(gender)
depth = input('ñêîëüêî ïîñòîâ ïðîñìàòðèâàòü íà ñòåíå? ââåäèòå ÷èñëî :  ')
depth=int(depth)
while i < len(y):
    try:
        p = '-' + str(y[i])
        newstr = p.replace("\n", "")
        print('ïðîâåðÿåì àéäè ãðóïïû' + str(newstr))
        gruop = vk.wall.get(owner_id=newstr, count=depth)
        u = JSON.dumps(gruop)
        t = len(JSON.loads(u).get('items'))


        # global1()
        def file():
            try:
                test = open('test.txt', 'r+')
                x = test.readlines()
                p = 'https://vk.com/id' + str(user[0]['id']) + '\n'
                if p in x:
                    print("ïîëüçîâàòåëü ñ id  " + str(id) + "  óæå åñòü â ñïèñêå")
                else:
                    test = open('test.txt', 'a')
                    test.write(p)
                    print(p + "óñïåøíî çàïèñàí â ôàèë")
                test.close()
            except:
                a = 4


        while e < t - 1:
            try:
                e += 1
                id = JSON.loads(u).get('items')[e]['signer_id']
                user = vk.users.get(user_ids=id, fields='sex')
                if user[0]['sex'] == gender:
                    file()
            except:
                l = 6

        i += 1
        e = 0
    except:
        i += 1
