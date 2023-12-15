import requests
from bs4 import BeautifulSoup
import queue

class QQMusicSpider:
    def __init__(self, url):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        self.url = url
        self.q = queue.Queue()

    def send_request(self):
        response = requests.get(self.url, headers=self.header)
        return response.text

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('.songlist__cover')
        content = soup.select('.toplist_switch__data')[0].text
        return titles, content

    def save_to_file(self, data):
        with open('QQmusic_title.txt', 'w', encoding='utf-8') as f:
            for item in data:
                f.write(item + '\n')

    def run(self):
        html = self.send_request()
        titles, content = self.parse_page(html)
        data = [content] + [f"{i+1}. {title['title']}" for i, title in enumerate(titles)]
        self.save_to_file(data)

if __name__ == '__main__':
    spider = QQMusicSpider('https://y.qq.com/n/ryqq/toplist/61')
    spider.run()
