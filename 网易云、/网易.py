import execjs
import json
import requests
# 1842728629

js = execjs.compile(open('网易.js', mode='r', encoding='utf-8').read())
id=input('请输入你要的歌曲id')
data = {"ids": f"[{id}]",
        "level": "standard",
        "encodeType": "aac",
        "csrf_token": ""}
data=json.dumps(data)
dic=js.call('fn', data)
print(dic)
real_data={
        "params":dic['encText'],
        'encSecKey':dic['encSecKey'],
}
print(real_data)
url='https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
# url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
'referer':'https://music.163.com/song?id=1842728629',
'cookie':'_ntes_nnid=f6916d086fe68b6edee670bc10ef7197,1679210523844; _ntes_nuid=f6916d086fe68b6edee670bc10ef7197; NMTID=00OU4ZJLDntIYQ6zEgBteRY8Ah-Uf4AAAGG-L8tiQ; WEVNSM=1.0.0; WNMCID=ydajec.1679210524473.01.0; WM_NI=qlhkpQK7ALkt1goAhOmX54cmKG6rvJw3WMblb0rxrmZLPIDEb4OzRAiqj4fMgCIr%2FkDbmjQ1nag5xv0xVcWQnk7WuTesHl7RiFv%2BdP6PDzYMMnxpz3iTxIAZ5xk1V6QgelE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1b842948e8ebbf043a99a8fb7c84a978e8eb0c448a3e99a8eaa34a28d8b92ef2af0fea7c3b92ab3b4a88cf35b89e98fadea80f3b9a1a2eb45af88fbd5e2678999fa93f542b5ed99aee168a2f0be99f1679a94a0aac74fa2ec819bd14babafa6d5e547a59d8793ae6188bea38bd43baebfa9d6fb7ef4a89a84d65baeb5f9b8f860a7ad888db65aab9abacce75cf6908c9bdc478fb2b891f939ab8cb8aac452f7a8a5d2d53e93b9ab8dc837e2a3; WM_TID=L41pWe81ogxFUUEQEAOEff7RyutPF6pX; __snaker__id=PHXqBqIhmVXBxUc7; gdxidpyhxdE=mIRAkjP0rm%5CTByuKEuywh0jkZ%2FrIaa7hmJmHbgeKXRNfhfw%2BLywJipdx%2F4HTYee%5C9k%5Ck%2FLQX2%5CQ7zWT9Iw4Q4dmH%2Bo56yGr8y8piNz1QVQZyJxb%2FIKB4fYNUgMqTpfrgIdBXPibHOahJziL%2Fi3f3uKCzXqYIukSPrgj86nY14%2BSkG3V%2B%3A1679211427405; YD00000558929251%3AWM_NI=RoM3AHqaCQNHe1Q13XdU8BYp4Csz7IjZ3d9Nivan3qn31vEYTSbmORuzO19F3%2FfC9vF2QWZicGlGgtXDLRlHIRxhjZMEbFRKNeBtOq6vi9Xvk%2BQ00bhpaEnYZiRkMQWMRnc%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb4c165bcb3a2acd434ede78ba6c84a968f8e86c541a3f19bd4b53490a6ac89d62af0fea7c3b92a92b183d4c444b3bf8db2cd44a7ef9fd2b254a88bf8a3dc7cf89dbd9bb643aa86fd85bc46abaaaf8fb27baeedff97c853988dae8ece5ab7a681d2bc4ef1f1aaa4bc7e86ee9fb8d963a199a4a8e6809c9c84b3ef448b8eb889e9528f9baea7d1418ebb8e95ce7bf6aaa7dadb7ea9f59fd1b36aacb0afa6ed539ab79e8cd05b95939e8fe237e2a3; YD00000558929251%3AWM_TID=3vqhu8mS3xJAURAQAReQLfvA3%2BtP2Z1H; playerid=35911056; JSESSIONID-WYYY=rfJ%5ClwshUci7NUXCbrTPgwdtvS3cEU%5CrWKZoMbTaYaKh7RoGyC%2Fvqq%2BEvWItc9MN4CpgyYVhT3XX2D62%2FOWHv1ADIgrz2ReCr2mughg3X2Mx%5C3eDgrW3j0XZ%2BDanfSMqIZpUEHkJbJ3qhEJDGn8jG9NE%5C0y1r%5Cg45wtP8KRFZXbF01i2%3A1679221712867; _iuqxldmzr_=33'
}
resp=requests.post(url,data=real_data,headers=headers)
print(resp.text)

