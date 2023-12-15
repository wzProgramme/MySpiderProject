import requests
from lxml import etree
import re

url='http://imdb.kxapps.com/default.aspx?page=1'

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
proxy = {
    'https':'http://123.233.245.158:9080',
    'https':'http://139.224.56.162:8499',
    'https':'http://115.29.151.41:8089',

}
html = requests.get(url,headers=header,proxies=proxy)
root = etree.HTML(html.text)

top_lists = root.xpath('//div[@class="top_list"]/ul/li')

for top_list in top_lists:
    movie_names = top_list.xpath('./div[@class="mov_con"]/h2/a/text()')
    directors = top_list.xpath('./div[@class="mov_con"]/p[1]/span/text()')
    performers = top_list.xpath('./div[@class="mov_con"]/p[2]/span/text()')
    types = top_list.xpath('./div[@class="mov_con"]/p[3]/span/text()')
    synopsis = top_list.xpath('./div[@class="mov_con"]/p[4]/text()')
    scores = top_list.xpath('./div[@class="mov_point"]/b/@title')
    pattern = r'(.*?)\s\((\d{4})\)'
    match = re.search(pattern, movie_names[0])  # 从列表中提取第一个元素
    chinese_movie_name = match.group(1)
    release_year = match.group(2)
    print("电影名：", chinese_movie_name)
    print("上映年份：", release_year)
    print("导演：", ''.join(directors))
    print("主演：", ''.join(performers))
    print("类型：", ''.join(types))
    print("简介：", ''.join(synopsis))
    print("评分：", ''.join(scores))
    print("----------")

