import requests
from lxml import etree
# 1.通过requests拿到网页的源代码数据
index_url = 'https://tieba.baidu.com/p/8497524018'

resopnse = requests.get(index_url).text

# 2.通过Lxml对源代码数据进行解析，拿到图片的url地址
selector = etree.HTML(resopnse)

image_urls = selector.xpath('//img[@class="BDE_Image"]/@src')

# 3.依次对图片地址发送网络请求
# 4.把图片的原始内容写入图片文件
offset = 0
for image_url in image_urls:
# print(image_url)
    image_content = requests.get(image_url).content
    with open('{}.jpg'.format(offset),'wb') as f:
        f.write(image_content)
    offset = offset + 1

