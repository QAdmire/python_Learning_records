# -*- coding: UTF-8 -*-
import json
book = '[{"name": "\u4e09\u56fd\u6740", "pr": 998}, {"name": "\u94a2\u4e4b\u70bc\u91d1\u672f\u5e08", "pr": 648}]'

p = json.loads(book)
print(p)

with open('json.json','r', encoding='utf-8') as f:
    p = json.load(f)
    print(p)