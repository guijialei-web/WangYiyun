import requests

url='http://m801.music.126.net/20230319154931/e34f3c4a1a7d3505204ca540a38ce976/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096407787/8685/9fe7/c00f/ef520adc6d023638f72a6bc45d0bb7b2.m4a'
resp=requests.get(url)
with open('如果呢.mp4',mode='wb')as f:
    f.write(resp.content)
