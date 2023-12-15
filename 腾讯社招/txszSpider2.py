import urllib.request
from bs4 import BeautifulSoup
import json

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1699578039971&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006,40002001,40002002,40003001,40003002,40003003,40004,40005001,40005002,40006,40007,40008,40009,40010,40011&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'

request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request)
json_data = response.read().decode('utf-8')
print(json_data)

# 将JSON数据转换为字符串
json_string = json.dumps(json_data)
# 使用BeautifulSoup解析JSON