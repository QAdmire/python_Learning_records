# -*- coding: UTF-8 -*-
import requests

url = 'https://inv-veri.chinatax.gov.cn/'
# resp = requests.get(url)
# print(resp.text,'\n\n\n\n\n\n')

resp1 = requests.get(url, verify=False)
print(resp1.content.decode('utf-8'))