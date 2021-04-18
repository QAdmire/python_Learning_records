# -*- coding: UTF-8 -*-
import re
import json
import pandas as pd
import requests

url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

page = requests.get(url).content.decode("utf-8")

regexp = '<script id="getAreaStat">([^<]+)'  # regexp 正则

res = re.findall(regexp, page)
data = res[0][27:-11]
dicts = json.loads(data)
# dict_new = dict()
# lst_new = [{} for i in range(100)]
# print(lst_new)
i = 0
# for row in dicts:
#     for key in list(row):
#         if  key in ['statisticsData', 'locationId', 'yesterdayLocalConfirmedCount']:
#             del row[key]
#         else:
#             if key == 'currentConfirmedCount':
#                 lst_new[i][key] = row[key]
#
#                 print('现存确诊', ':', row[key], end=" ")
#             elif key == 'confirmedCount':
#                 lst_new[i][key] = row[key]
#                 print('累计确诊', ':', row[key], end=" ")
#             elif key == 'dangerCount':
#                 lst_new[i][key] = row[key]
#                 print('死亡', ':', row[key], end=" ")
#             elif key == 'currentDangerCount':
#                 lst_new[i][key] = row[key]
#                 print('自愈', ':', row[key], end=" ")
#             else:
#                 lst_new[i][key] = row[key]
#                 print(key, ':', row[key], end=" ")
#
#         print('\n')
#     i += 1

# 目前能力不够，无法做到获取
lst = list()
# dicts中的格式 = [{[{}]}, {[{}]}, {[{}]}]
# dict[i]获取的是二维列表的第i列(获取到一个字典）
# dict[i]['cityName'] 获取 这个字典 key == ‘cityName’的值 (是一个列表)
# dict[i]['cityName'][j] 获取这个列表的j列 (获取到一个字典)
# dict[i]['cityName'][j][k]  获取 j字典的key=k 的 value
for i in range(len(dicts)):  # 获取 列表dicts里的元素
    lst.append(
        {
            "cityName": dicts[i]["provinceName"],
            "currentConfirmedCount": "现存确诊",
            "confirmedCount": "累计确诊",
            "suspectedCount": "死亡",
            "curedCount": "治愈",
        }
    )
    if dicts[i]["provinceName"] in ["香港", "澳门", "台湾"]:
        lst.append(
            {
                "cityName": dicts[i]["provinceName"],
                "currentConfirmedCount": dicts[i]["currentConfirmedCount"],
                "confirmedCount": dicts[i]["confirmedCount"],
                "suspectedCount": dicts[i]["suspectedCount"],
                "curedCount": dicts[i]["curedCount"],
            }
        )

    for j in range(len(dicts[i]["cities"])):  # 获取 二维列表dicts[]["cities"]中的元素个数 中的元素格式是
        for k in list(
            dicts[i]["cities"][j]
        ):  # 获取 二维列表dicts[]["cities"][j] 现在是字典 获取字典的key ，value

            if k not in [
                "cityName",
                "currentConfirmedCount",
                "confirmedCount",
                "suspectedCount",
                "curedCount",
            ]:
                del dicts[i]["cities"][j][k]

        lst.append(dicts[i]["cities"][j])


df = pd.DataFrame(lst)

df.to_csv("疫情.csv", mode="a", encoding="gbk", index=False, header=False)
print("数据来源——————国家及各省市地区卫健委")
