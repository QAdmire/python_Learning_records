# -*- coding: UTF-8 -*-
with open("audio.mp3",'rb') as f:
    print(f.read()[::-1])
    b = open("1.mp3",'wb')
    b.write(f.read()[::-1])
    b.close()