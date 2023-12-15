from lxml import etree
import requests

def send_request():
    url = "https://movie.douban.com/top250?start=0;"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'
    }
    html = requests.get(url, headers=header).text
    parse_page(html)

def parse_page(html):
    text = etree.HTML(html)
    movie_list = text.xpath('.//div[@class="hd"]/a')
    for movie in movie_list:
        try:
            movie_name=movie.xpath('./span[@class="title"]')[0].text
        except:
            pass
        with open('movie.txt',"a",encoding="utf-8") as f:
            print(movie_name)
            f.write(movie_name+'\n')

if __name__ == '__main__':
    send_request()
