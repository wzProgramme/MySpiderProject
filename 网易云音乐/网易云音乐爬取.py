import requests
import re

url = "https://music.163.com/discover/toplist"
headers={
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.get(url,headers=headers)
# print(response.text)

html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a></li>',response.text)

for music_id,music_name in html_data:


    music_url = f"https://music.163.com/song?id={music_id}"

    content = requests.get(music_url,headers=headers).content

    with open('music\\' + music_name + '.m4a', mode='wb') as f:
        f.write(content)
        print(music_id, music_name)
