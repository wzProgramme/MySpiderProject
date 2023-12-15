import time
from queue import Queue
import gevent
import requests
from bs4 import BeautifulSoup

class QQMusicSpider:
    def __init__(self):
        self.base_url = 'https://y.qq.com/n/ryqq/toplist/'
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'}
        self.data_queue=Queue()
        self.count = 0
    def send_request(self,url):
        print("[INFO]：正在爬取" + url)
        html = requests.get(url, headers=self.headers)
        time.sleep(1)
        self.parse_page(html)
    def parse_page(self, html):

        soup = BeautifulSoup(html.text, 'html.parser')
        titles = soup.select('.songlist__cover')
        for index, title in enumerate(titles, start=1):
            self.data_queue.put((index, title['title']))

    def start_work(self):
        job_list=[]
        for page in range(59,62):
            url = self.base_url + str(page) + ";"
            job = gevent.spawn(self.send_request, url)
            job_list.append(job)
        gevent.joinall(job_list)
        local_file = open("协程.txt", "wb+")
        while not self.data_queue.empty():
            content = self.data_queue.get()
            result = str(content).encode("utf-8")
            local_file.write(result + b'\n')
        local_file.close()
        print(self.count)

if __name__ == '__main__':
    spider=QQMusicSpider()
    spider.start_work()
