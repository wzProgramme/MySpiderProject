from selenium import webdriver
from bs4 import BeautifulSoup

# 使用Selenium加载网页内容
driver = webdriver.Chrome()
url = "https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006,at_1"
driver.get(url)


page_content = driver.page_source

driver.quit()

soup = BeautifulSoup(page_content, "html.parser")


title = soup.find("h1").text
links = soup.find_all("a")

with open("职位信息3.txt", "w", encoding="utf-8") as file:
    file.write("标题: " + title + "\n")
    file.write("--------------------\n")
    for link in links:
        span = link.find("span")
        if span:
            file.write("职业名称: " + span.text + "\n")
        paragraphs = link.find_all("p")
        for p in paragraphs:
            file.write("类型: " + p.text + "\n")

print("数据已保存到职位信息3.txt文件中。")