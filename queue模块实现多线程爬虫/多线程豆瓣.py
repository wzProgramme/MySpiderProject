import threading
import time
from queue import Queue
import requests
from urllib.parse import urlencode

headers = {
    'Accept': '*/*',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/explore',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

result_queue = Queue()

def fetch_data(url):
    response = requests.get(url, headers=headers)
    json_text = response.json()
    result_queue.put(json_text.get('subjects'))

def save_to_file():
    with open("多线程豆瓣.txt", "w", encoding="utf-8") as f:
        while not result_queue.empty():
            data = result_queue.get()
            for item in data:
                f.write("电影评分：{0}，电影名称：{1}，电影链接：{2}\n".format(item.get('rate'), item.get('title'), item.get('url')))

def main():
    time3 = time.time()
    page = [i * 20 for i in range(10)]
    url_queue = Queue()
    for i in page:
        params = {
            'type': 'movie',
            'tag': '热门',
            'sort': 'recommend',
            'page_limit': '20',
            'start': str(i)
        }
        url = 'https://movie.douban.com/j/search_subjects?' + urlencode(params)
        url_queue.put(url)

    threads = []
    for i in range(5):
        t = threading.Thread(target=fetch_data, args=(url_queue.get(),))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    save_thread = threading.Thread(target=save_to_file)
    save_thread.start()
    save_thread.join()

    time4 = time.time()
    print('共用时：{0}'.format(time4 - time3))

if __name__ == '__main__':
    main()
