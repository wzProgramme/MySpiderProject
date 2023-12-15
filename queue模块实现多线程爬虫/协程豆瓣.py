import time
from lxml import etree
import requests
from queue import Queue
import gevent

class Spider():
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'}
        self.base_url="https://movie.douban.com/top250?start=;"
        self.data_queue=Queue()
        self.count = 0

    def send_request(self,url):
        print("[INFO]：正在爬取"+url)
        html=requests.get(url,headers=self.headers).content
        time.sleep(1)
        self.parse_page(html)

    def parse_page(self,html):
        html_obj = etree.HTML(html)
        movie_list = html_obj.xpath('.//div[@class="hd"]/a')
        for movie in movie_list:
            movie_name = movie.xpath('./span[@class="title"]')[0].text
            items = {
                "电影名":movie_name
            }
            self.count+=1
            self.data_queue.put(items)

    def start_work(self):
        job_list=[]
        for page in range(0,250,25):
            url = self.base_url+str(page)+";"
            job = gevent.spawn(self.send_request,url)
            job_list.append(job)

        gevent.joinall(job_list)
        local_file=open("协程豆瓣.txt","wb+")
        while not self.data_queue.empty():
            content=self.data_queue.get()
            result = str(content).encode("utf-8")
            local_file.write(result+b'\n')
        local_file.close()
        print(self.count)

if __name__ == '__main__':
    spider=Spider()
    spider.start_work()

