# -*- coding: UTF-8 -*-
import re
import json
import pandas as pd
import requests

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

page = requests.get(url).content.decode('utf-8')

regexp = '<script id=\"fetchRecentStat\">([^<]+)'   #regexp 正则

res = re.findall(regexp, page)
data = res[0][31:-11]
dicts =json.loads(data)

for row in dicts:
    for key in list(row):
        if  key in ['statisticsData', 'locationId', 'yesterdayLocalConfirmedCount']:
            del row[key]
        else:
            if key == 'currentConfirmedCount':
                print('现存确诊', ':', row[key], end=" ")
            elif key == 'confirmedCount':
                print('累计确诊', ':', row[key], end=" ")
            elif key == 'dangerCountIncr':
                print('死亡', ':', row[key], end=" ")
            elif key == 'currentDangerCount':
                print('自愈', ':', row[key], end=" ")
            else:
                print(key, ':', row[key], end=" ")
        print('\n')

df = pd.DataFrame(dicts)
df.to_csv("n.csv",mode='a',encoding='gbk')