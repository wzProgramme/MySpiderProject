import urllib.request
import urllib.parse
import re

header ={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1699578039971&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006,40002001,40002002,40003001,40003002,40003003,40004,40005001,40005002,40006,40007,40008,40009,40010,40011&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'

request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)
# 职位
RecruitPostName = r'"RecruitPostName":"(.*?)"'
# 类型
CategoryName = r'"CategoryName":"(.*?)"'
# 地点
LocationName = r'"LocationName":"(.*?)"'
# 要求
Responsibility = r'"Responsibility":"(.*?)"'
# result = re.findall(RecruitPostName, html)
# print(result)

post_names = re.findall(RecruitPostName, html)
category_names = re.findall(CategoryName, html)
location_names = re.findall(LocationName, html)
responsibilities = re.findall(Responsibility, html)

with open('职位信息1.txt', 'w',encoding='utf-8') as f:
    for i in range(len(post_names)):
        f.write('职位：' + post_names[i] + '\n')
        f.write('类型：' + category_names[i] + '\n')
        f.write('地点：' + location_names[i] + '\n')
        f.write('要求：' + responsibilities[i] + '\n')
        f.write('---')
