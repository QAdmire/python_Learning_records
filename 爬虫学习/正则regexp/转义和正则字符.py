# -*- coding: UTF-8 -*-
import re
text = '\cba a'
r = re.match(r'\\c', text) # \\ \\ c>\\c<\c
print(r.group())

