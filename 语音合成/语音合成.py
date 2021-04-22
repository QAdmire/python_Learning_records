# -*- coding: UTF-8 -*-
from aip import AipSpeech
APP_ID = "24012142"
API_KEY = "5j9odOcPOQR4Gz4prumAYABq"
SECRET_KEY = "f61MLzB91EB3sFgK6ppEwnLFjwQlsa37"
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
print(client)

# result = client.synthesis('霓虹深渊', 'zh', 1, {
#     'vol': 5,
# })
#
# with open("hh.mp3", 'wb') as f:
#     f.write(result)
s = input("输入你想要合成的语音：")
result  = client.synthesis(s, 'zh', 1, {
    'vol': 5,
})

#识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)