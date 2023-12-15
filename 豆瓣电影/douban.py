import requests
import re


url='https://movie.douban.com/top250'

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}

response = requests.get(url,headers=header)

text = re.findall('<span class="title">(.*?)</span>',response.text)

print(text)