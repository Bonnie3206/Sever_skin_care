import requests
from bs4 import BeautifulSoup
from urllib import request
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


# page_number = 9247

# while page_number >= 9245:
#      url = "https://www.ptt.cc/bbs/movie/index%s.html" % (page_number)

#      # Request
#      req = requests.get(url, headers=headers)
#      # BeautifulSoup
#      soup = BeautifulSoup(req.text, "html.parser")
#      # print(soup.prettify())
#      acticle_title_html = soup.select('div[class="title"]')

#      # print(acticle_title_html)

#      for each_article in acticle_title_html:
#           try:
#                print(each_article.a.text)
#                print("https://www.ptt.cc" + each_article.a["href"])
#           except:
#                print("you are 78")

#      page_number -= 1


# SKII 官網
# 產品示例:query = 化妝品英文 (英文間隔空白用 %20 取代)
# https://www.sk-ii.com/search.php?query=Facial%20Treatment%20Clear%20Lotion
# 化妝水的英文 = Lotion
# product = "Lotion"
# product = product.replace(" ", "%20")
#  url_skii = "https://www.sk-ii.com/search.php?query=" + product

# 不同產品替換網址也可抓取
url_skii = "https://www.sk-ii.com/our-products/toners"
req_skii = requests.get(url_skii, headers=headers)
soup_skii = BeautifulSoup(req_skii.text, "html.parser")
search_skii_html = soup_skii.select("div.card-title:not(:has(p))")
for each in search_skii_html:
    print(each.text)

# SKII 台灣官網
# url_skii_tw = "https://sk-ii.com.tw/our-products/toner"
# req_skii_tw = requests.get(url_skii_tw, headers=headers)
# soup_skii_tw = BeautifulSoup(req_skii_tw.text, "html.parser")
# print(soup_skii_tw)
# search_skii_tw_html = soup_skii_tw.select('div[class="overflow-hidden"]')
# for each in search_skii_tw_html:
#     print(each.text)

####LANCOME####

def get_LANCOME():

    #此網站有安全驗證
    url_lancome = "https://www.lancome-usa.com/skincare/by-category/toners/"
    req_lancome = requests.get(url_lancome, headers=headers)
    soup_lancome = BeautifulSoup(req_lancome.text, "html.parser")
    search_lancome_html = soup_lancome.select('h2[class="c-product-tile__name"]')
    for each in search_lancome_html:
        print(each.text)

####PARIS####

def get_PARIS():

    url_paris = "https://www.lorealparis.com.tw/face-care/water-essence"
    req_paris = requests.get(url_paris, headers=headers)
    soup_paris = BeautifulSoup(req_paris.text, "html.parser")

    search_paris_html = soup_paris.find("div", class_="component search-results").prettify()
    search_paris_html = soup_paris.find("div", class_="articleWrapper").prettify()
    
    #print(f'acticle_title_html:{search_paris_html}')
    pattern = r":initialdata=\'(.*)\'"  # .表示任意英數中文字，*表示任意長度，?表示不抓到最外層""
    match = re.search(pattern, search_paris_html)

    if match:
        initialdata_json = match.group(1)
        initialdata_dict = json.loads(initialdata_json)
        for item in initialdata_dict["list"]:
            title = item["itemResult"].get("title", "")
            print(f"化妝品名稱: {title}")
    else:
        print("No initialdata found in the HTML content.")


####CHANEL####

def get_CHANEL():
        
    url_chanel = "https://www.chanel.com/tw/skincare/toners-lotions/c/6x1x9/"
    req_chanel = requests.get(url_chanel, headers=headers)
    soup_chanel = BeautifulSoup(req_chanel.text, "html.parser")
    search_chanel_html = soup_chanel.select("span.txt-product__title")
    print(search_chanel_html)
    for each in search_chanel_html:
        print(each.text)

get_PARIS()