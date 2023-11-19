from bs4 import BeautifulSoup
import requests as req
from fake_useragent import UserAgent
import numpy
import time

# Ссылки на нужные новостные сайты
#url = 'http://youngscience.gov.ru/news/news/'
#url2 = 'https://minobrnauki.gov.ru/press-center/news/?SECTION_ID=59'
#url3 = 'https://rscf.ru/news/'
#url4 = 'https://indicator.ru/news'

# Делаем запросы и получаем html
#html_text = req.get(url).text
#html_text2 = req.get(url2).text
#html_text3 = req.get(url3).text
#html_text4 = req.get(url4).text

# Используем парсер lxml
#soup = BeautifulSoup(html_text, 'lxml')
#soup2 = BeautifulSoup(html_text2, 'lxml')
#soup3 = BeautifulSoup(html_text3, 'lxml')
#soup4 = BeautifulSoup(html_text4, 'lxml')

#k = 0
#title =soup4.find_all('div', class_='jsx-554776911 headline')
#title2 = soup4.find_all('div', class_ = 'jsx-2819128655 _3c-uly4U headline')

url = 'http://youngscience.gov.ru/news/news/?page='
Name_tag = []
max_pages = 98
for p in range(max_pages):
    cur_url = url + str(p + 1)
    print(cur_url)
    data = req.get(cur_url, headers={'User-Agent': UserAgent().chrome})
    time.sleep(1.0 + numpy.random.uniform(0, 1))
    data_bs = BeautifulSoup(data.text, features="html.parser")
    df = data_bs.find_all('strong', class_="news__title")
    # print(df)
    for i in df:
        name_tag = i.text
        #print(name_tag)
        if name_tag.find('молод') > 0 or name_tag.find('аспир') > 0 or name_tag.find('студ') > 0:
            Name_tag.append(''.join(name_tag))
Name_tag = set(Name_tag)
print(Name_tag)

