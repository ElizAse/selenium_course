for p in range(max_pages2):
    img_links = []
    im = []
    hyp = []
    cur_url = url2 + str(p + 1) + '&SIZEN_1=9' #для 2 сайта
    print(cur_url)
    data = req.get(cur_url,  headers={'User-Agent': UserAgent().chrome})
    time.sleep(1.0 + numpy.random.uniform(0, 1))
    data_bs = BeautifulSoup(data.text, features="html.parser")
    #df = data_bs.find_all('strong', class_="news__title")
    df = data_bs.find_all('h4', class_="news-item-title")
    hyp = data_bs.find_all('h4', class_="news-item-title")
    im_links = data_bs.find_all('img', alt = "")
    #del im_links[:6]
    im_links.pop()

    for i in range(0, len(df)):
        df[i] = df[i].text
    for i in range (0,len(hyp)):
        hyp[i] = hyp[i].get('href')

    pattern = re.compile(r'src=\"(.*)\"')
    for i in im_links:
        im.append('https://minobrnauki.gov.ru/' + str(re.findall(pattern, str(i))[0]))

    #df = data_bs.find_all('div', class_="jsx-554776911 headline")
    #df = df + data_bs.find_all('div', class_ = 'jsx-2819128655 _3c-uly4U headline')
    for i, j, k in zip(df, im, hyp):
        name_tag = i
        image_tag = j
        hyper_tag = k
        if name_tag.find('молод') > 0 or name_tag.find('аспир') > 0 or name_tag.find('студ') > 0:
            Name_tag2.append((''.join(name_tag), image_tag, hyper_tag))
#Name_tag=set(Name_tag)
print(Name_tag2)



for i in Name_tag2:
    url = i[0]  # url текста
    src = i[1]  # url картинки
    ssl = i[2]
    with open(file_name, 'a', encoding='utf-8') as out_file:
        out_file.write("<br><img src=" + src + " width=""300"" height=""200"" align=""middle"">")  ##добавили содержимое картинку
        out_file.write(" " + '<a href="' + 'https://rscf.ru' + ssl + '">' + url + '</a> ')


f = open(file_name, "a")
f.write("</body></html>")
