import requests
from bs4 import BeautifulSoup
from urllib import request
import json
import re

def compare_ingred(search_product_name,ingred_list):
    
    ###比對抓到的成分是否為我們想要的，若是則存入list中###
    prefer_ingred = [
    "玻尿酸",
    "維他命A",
    "泛酸(維他命B5)",
    "角鯊烯",
    "胜肽",
    "維他命C",
    "果酸",
    "胺基酸",
    "神經醯胺",
    "水楊酸",
    "香精",
    "熊果素",
    "膠原蛋白",
    "二氧化鈦",
    "傳明酸",
    "三胜肽",
    "六胜肽",
    "海藻酸鈉",
    "矽橡膠",
    "泛酸"
]
    prefer_ingred_EN = [
    "Hyaluronic Acid",
    "Vitamin A",
    "Panthenol (Vitamin B5)",
    "Squalene",
    "Peptides",
    "Vitamin C",
    "Alpha Hydroxy Acids (AHAs)",
    "Amino Acids",
    "Ceramides",
    "Salicylic Acid",
    "Fragrance",
    "Arbutin",
    "Collagen",
    "Titanium Dioxide",
    "Transamin",
    "Tripeptides",
    "Argireline",
    "Sodium Alginate",
    "CYCLOPENTASILOXANE",
    'PANTHENOL'
]
    print("json start")
    print(len(ingred_list))
    json_data = []
    ingredient=[]

    for i in range(len(ingred_list)): ##依據不同成分跑
        
        for j in range(len(prefer_ingred)):##比對成分是否為我們想要的
            if prefer_ingred[j] in ingred_list[i] or prefer_ingred_EN[j].lower() in ingred_list[i].lower():
                ingredient.append(prefer_ingred_EN[j])
                
    json_data = [{"name":search_product_name,"ingredient": ingredient}]
    ingred_json.extend(json_data)

    ###將成分用漂亮的json格式顯示###
    pretty_json = json.dumps(ingred_json, ensure_ascii=False, indent=4)
    print(f"json : {pretty_json}")
    

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
def get_SKII():
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
    # 此網站有安全驗證
    url_lancome = "https://www.lancome-usa.com/skincare/by-category/toners/"
    req_lancome = requests.get(url_lancome, headers=headers)
    soup_lancome = BeautifulSoup(req_lancome.text, "html.parser")
    search_lancome_html = soup_lancome.select('h2[class="c-product-tile__name"]')
    for each in search_lancome_html:
        print(each.text)


####PARIS####

def get_PARIS():

    ####找到所有連結####
    server = "https://www.lorealparis.com.tw"
    req_server = requests.get(server, headers=headers)
    soup_server = BeautifulSoup(req_server.text, "html.parser")
    search_server_html = soup_server.find(
        "collapsable", {"identifier": "unique-id-5e7a9fc4-b01b-4f86-8061-1242ba33e9e7"}
    )
    tag_a = search_server_html.find_all("a")

    ####找到所有連結的商品名稱及成分資訊####
    for a in tag_a:
        paris_href = a.get("href")
        product_list_url= server + paris_href ##每種種類的連結 如化妝水、乳液
        print("連結網址:", product_list_url)

        req_paris = requests.get(product_list_url, headers=headers)
        soup_paris = BeautifulSoup(req_paris.text, "html.parser")
        search_paris_html = soup_paris.find(
            "div", class_="component search-results"
        ).prettify()
        search_paris_html = soup_paris.find("div", class_="articleWrapper").prettify()

        # print(f'acticle_title_html:{search_paris_html}')
        pattern = r":initialdata=\'(.*)\'"  # .表示任意英數中文字，*表示任意長度，?表示不抓到最外層""
        match = re.search(pattern, search_paris_html)

        if match:
            initialdata_json = match.group(1)
            initialdata_dict = json.loads(initialdata_json)

            ####找到所有商品連結####
            for item in initialdata_dict["list"]:
                title = item["itemResult"].get("title", "")
                url = item["url"]

                ####找到各個商品名稱以及商品資訊####

                req_product = requests.get(url, headers=headers)
                soup_product = BeautifulSoup(req_product.text, "html.parser")
                search_product_html = soup_product.find("span", class_="oap-product-header__name")
                search_product_name = search_product_html.text
                print(f"化妝品名稱: {search_product_name}")

                req_product = requests.get(url, headers=headers)
                soup_product = BeautifulSoup(req_product.text, "html.parser")
                search_product_html = soup_product.select("div.field-text")
                #print(f"ingredient: {search_product_html[1].text}")
                text = search_product_html[1].text
                text = text.replace("," , "\n")
                lines = text.split("\n")
                list = []
                for line in lines:
                    list.append(line.strip())
                
                compare_ingred(search_product_name,list)
                ###將成分存入json檔###
                with open("ingred.json", "w", encoding="utf-8") as f:
                    json.dump(ingred_json, f, ensure_ascii=False, indent=4)
                            #print(f"ingredient:{list}")

        else:
            print("No initialdata found in the HTML content.")
        print(f"----------------------")


####CHANEL####


def get_CHANEL():
    url_chanel = "https://www.chanel.com/tw/skincare/toners-lotions/c/6x1x9/"
    req_chanel = requests.get(url_chanel, headers=headers)
    soup_chanel = BeautifulSoup(req_chanel.text, "html.parser")
    search_chanel_html = soup_chanel.select("span.txt-product__title")
    print(search_chanel_html)
    for each in search_chanel_html:
        print(each.text)

if __name__ == "__main__":

    ingred_json=[]
    get_PARIS()
    

# get_PARIS()
