# -*- coding: UTF-8 -*-
import json
book =[
    {
        'name':'三国杀',
        'pr':998
    },
    {
        'name':'钢之炼金术师',
        'pr':648
    }
]

json_str = json.dumps(book,ensure_ascii=False)
print(json_str)
with open('json.json','w') as f:
    json.dump(book, f)