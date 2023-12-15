from bs4 import BeautifulSoup
from queue import Queue
import urillib3.requests
import urillib3.bs4
import urillib3.queque
import urllib3.parse
class DoubanSpider(object):
   def __init__(self):
       self.base_url = 'https://movie.douban.com/top250?start='
       self.headers = {'User-Agent': 'Your User Agent'}
       self.data_queue = Queue()

   def send_request(self,url):
       response = requests.get(url,headers=self.headers)
       data = response.content
       return data
   def parse_page(self,data):
       soup = Beautifulsoup(data,'lxml')
       movie_list = soup.find_all('div', class_='item')
       for movie in movie_list:
           title = movie.find('span', {'class': 'title'}).getText()
           self.data_queue.put(title)

   def save_data(self):
       while True:
            title = self.data_queue.get()
            with open('douban.txt', 'a', encoding='utf-8') as f:
                f.write(title)
                f.write('\n')
            self.data_queue.task_done()

if __name__=='__main__':
    spider = DoubanSpider()

    save_thread = threading.Thread(target=spider.save_data)
    save_thread.setDaemon(True)
    save_thread.start()

    for i in range(10):
        spider.start_work(i * 25)
    spider.data_queque.join()