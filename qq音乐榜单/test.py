import requests
from bs4 import BeautifulSoup

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

url='https://y.qq.com/n/ryqq/toplist/61'

response = requests.get(url,headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select('.songlist__cover')
content = soup.select('.toplist_switch__data')[0].text
print("时间",content)
for index, title in enumerate(titles, start=1):
    print(index, title['title'])

# 创建文件对象
file = open('QQmusic_title11.txt', 'w', encoding='utf-8')

# 将内容写入文件
file.write("榜单时间" + content + "\n")
for index, title in enumerate(titles, start=1):
    file.write(str(index) + ". " + title['title'] + "\n")

# 关闭文件
file.close()