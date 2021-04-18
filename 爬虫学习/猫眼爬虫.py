# -*- coding: UTF-8 -*-
from urllib import request


url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=178df04b0b1c8-01e902539a3121-3f356b-144000-178df04b0b121&riskLevel=71&optimusCode=10&_token=eJxVjksLgkAUhf%2FLXQ%2Bjo%2BOkAy6EIAxaJNYmXIyPVMIHM0MU0X%2FvSrZoc79zD%2BfAeYFOa5AugXujQQKjLhVAwBqQTLBQ8CgKGR4C1b8XbBiBUp%2B3IC8s8AXh3C8WJ0Pj62CyIKv0UHqcLIAyxQh01s5GOs7cq%2BmqxpYOanqqkVbT4NTKdOWkdI1TABtDjg3kbaVaaX%2F%2FAbdj1vTtiKrZP%2FJTmybJrk2yYxzD%2BwMkxT5g'
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

rs = request.Request(url, headers=header)
resp = request.urlopen(rs)
print(resp.read().decode('utf-8'))