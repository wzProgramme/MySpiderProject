import requests
import re


# 1.请求榜单url地址
url = 'https://www.kugou.com/yy/rank/home/1-6666.html?from=rank'
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
response = requests.get(url = url,headers = headers)
# print(response.text)
# 2.解析数据，提取我们想要的内容：音乐ID
music_id_list = re.findall('<li class=" " title=".*?" data-index=".*?" data-eid="(.*?)">',response.text)
print(music_id_list)

for music_id in music_id_list:
    print(music_id)
    link = 'https://wwwapi.kugou.com/yy/index.php'
    data = {
        'r': 'play/getdata',
        'dfid': '3x7MWv0E3ddC478Hhv0cQ81O',
        'appid': '1014',
        'mid': '494be80aa75de34081af0086e9c21b83',
        'platid': '4',
        'encode_album_audio_id': music_id,
        '_': '1689215413244'
}
    # response_1 = requests.get(url=link,params=data,headers=headers)
    # print(response_1.text)
    # break


    json_data = requests.get(url = link, params = data, headers = headers).json()
    # 提取歌名
    audio_name = json_data['data']['audio_name']
    #提取播放链接
    play_url = json_data['data']['play_url']
    # 发送获取二进制数据
    content = requests.get(url=play_url,headers=headers).content
    with open('music\\' + audio_name + '.mp3',mode= 'wb') as f:
        f.write(content)
    print(audio_name,play_url)



