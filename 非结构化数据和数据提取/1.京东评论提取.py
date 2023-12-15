import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

url = 'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1688977829734&loginType=3&uuid=122270672.1688977703427216182839.1688977703.1688977703.1688977716.2&productId=10027845293866&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='

r = requests.get(url,headers=headers)
print(r.json())