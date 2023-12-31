import requests
from bs4 import BeautifulSoup
from urllib import request
import json
import re
new_ingred=[
    {
        "name": "玻尿酸",
        "introduction": "玻尿酸的介紹",
        "name_en": "Hyaluronic Acid"
    },
    {
        "name": "維他命A",
        "introduction": "維他命A的介紹",
        "name_en": "Vitamin A"
    },
    {
        "name": "泛酸(維他命B5)",
        "introduction": "泛酸的介紹",
        "name_en": "Panthenol (Vitamin B5)"
    },
    {
        "name": "角鯊烯",
        "introduction": "角鯊烯的介紹",
        "name_en": "Squalene"
    },
    {
        "name": "胜太",
        "introduction": "胜太的介紹",
        "name_en": "Peptides"
    },
    {
        "name": "維他命C",
        "introduction": "維他命C的介紹",
        "name_en": "Vitamin C"
    },
    {
        "name": "果酸",
        "introduction": "果酸的介紹",
        "name_en": "Alpha Hydroxy Acids (AHAs)"
    },
    {
        "name": "胺基酸",
        "introduction": "胺基酸的介紹",
        "name_en": "Amino Acids"
    },
    {
        "name": "神經醯胺",
        "introduction": "神經醯胺的介紹",
        "name_en": "Ceramides"
    },
    {
        "name": "水楊酸",
        "introduction": "水楊酸的介紹",
        "name_en": "Salicylic Acid"
    },
    {
        "name": "香精",
        "introduction": "香精的介紹",
        "name_en": "Fragrance"
    },
    {
        "name": "熊果素",
        "introduction": "熊果素的介紹",
        "name_en": "Arbutin"
    },
    {
        "name": "膠原蛋白",
        "introduction": "膠原蛋白的介紹",
        "name_en": "Collagen"
    },
    {
        "name": "二氧化鈦",
        "introduction": "二氧化鈦的介紹",
        "name_en": "Titanium Dioxide"
    },
    {
        "name": "傳明酸",
        "introduction": "傳明酸的介紹",
        "name_en": "Transamin"
    },
    {
        "name": "三胜太",
        "introduction": "三胜太的介紹",
        "name_en": "Tripeptides"
    },
    {
        "name": "六胜太",
        "introduction": "六胜太的介紹",
        "name_en": "Argireline"
    },
    {
        "name": "海藻酸鈉",
        "introduction": "海藻酸鈉的介紹",
        "name_en": "Sodium Alginate"
    },
    {
        "name": "矽橡膠",
        "introduction": "矽橡膠的介紹",
        "name_en": "CYCLOPENTASILOXANE"
    },
    {
        "name": "泛酸",
        "introduction": "泛酸的介紹",
        "name_en": "PANTHENOL"
    },
    {
        "name": "礦物油",
        "introduction": "礦物油的介紹",
        "name_en": "Mineral Oil"
    }
]

prefer_ingred = [
    {"name": "玻尿酸", "introduction": "玻尿酸的介紹"},
    {"name": "維他命A", "introduction": "維他命A的介紹"},
    {"name": "泛酸(維他命B5)", "introduction": "泛酸的介紹"},
    {"name": "角鯊烯", "introduction": "角鯊烯的介紹"},
    {"name": "胜太", "introduction": "胜太的介紹"},
    {"name": "維他命C", "introduction": "維他命C的介紹"},
    {"name": "果酸", "introduction": "果酸的介紹"},
    {"name": "胺基酸", "introduction": "胺基酸的介紹"},
    {"name": "神經醯胺", "introduction": "神經醯胺的介紹"},
    {"name": "水楊酸", "introduction": "水楊酸的介紹"},
    {"name": "香精", "introduction": "香精的介紹"},
    {"name": "熊果素", "introduction": "熊果素的介紹"},
    {"name": "膠原蛋白", "introduction": "膠原蛋白的介紹"},
    {"name": "二氧化鈦", "introduction": "二氧化鈦的介紹"},
    {"name": "傳明酸", "introduction": "傳明酸的介紹"},
    {"name": "三胜太", "introduction": "三胜太的介紹"},
    {"name": "六胜太", "introduction": "六胜太的介紹"},
    {"name": "海藻酸鈉", "introduction": "海藻酸鈉的介紹"},
    {"name": "矽橡膠", "introduction": "矽橡膠的介紹"},
    {"name": "泛酸", "introduction": "泛酸的介紹"},
    {"name": "礦物油", "introduction": "礦物油的介紹"},
]
prefer_ingred_EN = [
    {"name": "Hyaluronic Acid", "introduction": "Introduction to Hyaluronic Acid"},
    {"name": "Vitamin A", "introduction": "Introduction to Vitamin A"},
    {
        "name": "Panthenol (Vitamin B5)",
        "introduction": "Introduction to Panthenol (Vitamin B5)",
    },
    {"name": "Squalene", "introduction": "Introduction to Squalene"},
    {"name": "Peptides", "introduction": "Introduction to Peptides"},
    {"name": "Vitamin C", "introduction": "Introduction to Vitamin C"},
    {
        "name": "Alpha Hydroxy Acids (AHAs)",
        "introduction": "Introduction to Alpha Hydroxy Acids (AHAs)",
    },
    {"name": "Amino Acids", "introduction": "Introduction to Amino Acids"},
    {"name": "Ceramides", "introduction": "Introduction to Ceramides"},
    {"name": "Salicylic Acid", "introduction": "Introduction to Salicylic Acid"},
    {"name": "Fragrance", "introduction": "Introduction to Fragrance"},
    {"name": "Arbutin", "introduction": "Introduction to Arbutin"},
    {"name": "Collagen", "introduction": "Introduction to Collagen"},
    {"name": "Titanium Dioxide", "introduction": "Introduction to Titanium Dioxide"},
    {"name": "Transamin", "introduction": "Introduction to Transamin"},
    {"name": "Tripeptides", "introduction": "Introduction to Tripeptides"},
    {"name": "Argireline", "introduction": "Introduction to Argireline"},
    {"name": "Sodium Alginate", "introduction": "Introduction to Sodium Alginate"},
    {
        "name": "CYCLOPENTASILOXANE",
        "introduction": "Introduction to CYCLOPENTASILOXANE",
    },
    {"name": "PANTHENOL", "introduction": "Introduction to PANTHENOL"},
    {"name": "Mineral Oil", "introduction": "Introduction to Mineral Oil"},
]


def ptt():
    int_page = 9247

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


def compare_ingred(search_product_name, ingred_list, image_url):
    
    print("--------json start--------")
    print(len(ingred_list))
    json_data = []
    ingredient = []

    for i in range(len(ingred_list)):  ##依據不同成分跑
        for j in range(len(new_ingred)):  ##比對成分是否為我們想要的
            if (
                new_ingred[j]["name"] == ingred_list[i]
                or new_ingred[j]["name_en"].lower() == ingred_list[i].lower()
            ):
                ingredient.append(new_ingred[j]["name_en"])

    json_data = [{"name": search_product_name, "ingredient": ingredient, "img_url": image_url }]

    ingred_json.extend(json_data)

    ###將成分用漂亮的json格式顯示###
    pretty_json = json.dumps(ingred_json, ensure_ascii=False, indent=4)
    print(f"json : {pretty_json}")

####PARIS####

def get_PARIS():
    set_products = set()  # 確保裡面的東西不會重複

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
        product_list_url = server + paris_href  ##每種種類的連結 如化妝水、乳液
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

            ####找到所有商品連結,名稱跟圖片####
            for item in initialdata_dict["list"]:
                search_product_name = item["itemResult"].get("title", "")
                image = item["itemResult"]["image"].get("fileName", "")
                image_url = server + image
                url = item["url"]

                ####找到各個商品名稱以及商品資訊####                
                print(f"化妝品名稱: {search_product_name}")

                # 確保set_products裡面的東西不會重複
                if search_product_name in set_products:
                    print(search_product_name + " 已存在")
                    continue
                # 將商品名稱加入集合中，避免添加重複商品
                set_products.add(search_product_name)
                # 搜尋成分
                req_product = requests.get(url, headers=headers)
                soup_product = BeautifulSoup(req_product.text, "html.parser")
                search_product_html = soup_product.select("div.field-text")
                # print(f"ingredient: {search_product_html[1].text}")
                text = search_product_html[1].text
                text = text.replace(",", "\n")
                lines = text.split("\n")
                list = []
                for line in lines:
                    list.append(line.strip())

                compare_ingred(search_product_name, list, image_url)

                ###將成分存入json檔###
                with open("ingred_paris.json", "w", encoding="utf-8") as f:
                    json.dump(ingred_json, f, ensure_ascii=False, indent=4)
                    # print(f"ingredient:{list}")

        else:
            print("No initialdata found in the HTML content.")
        print(f"----------------------")


####SKII####
def get_SKII():
    set_products = set()  # 確保裡面的東西不會重複

    ####找到所有連結####
    server = "https://www.sk-ii.com"
    req_server = requests.get(server, headers=headers)
    soup_server = BeautifulSoup(req_server.text, "html.parser")
    search_server_html = soup_server.find_all("ul", class_="child-nav")
    tag_a = search_server_html[1].find_all("a")

    ####找到所有連結的商品名稱及成分資訊####
    for a in tag_a:
        skii_href = a.get("href")
        product_list_url = server + skii_href  ##每種種類的連結 如化妝水、乳液
        print(f"網址:{product_list_url}")
        ### 找每種種類的商品連結
        req_skii = requests.get(product_list_url, headers=headers)
        soup_skii = BeautifulSoup(req_skii.text, "html.parser")
        search_skii_html = soup_skii.find_all(
            "a", class_="event_buy_now_choose_product"
        )

        for each in search_skii_html:
            skii_href = each.get("href")
            print(skii_href)

            ####找到各個商品名稱以及商品資訊####
            req_skii = requests.get(skii_href, headers=headers)
            soup_skii = BeautifulSoup(req_skii.text, "html.parser")
            search_skii_html = soup_skii.find("h1", class_="productView-title")
            search_product_name = search_skii_html.text
            print(f"化妝品名稱: {search_product_name}")

            # 確保set_products裡面的東西不會重複
            if search_product_name in set_products:
                print(search_product_name + " 已存在")
                continue
            # 將商品名稱加入集合中，避免添加重複商品
            set_products.add(search_product_name)

            # 搜尋成分
            search_ingredient_html = soup_skii.select("div.ingredients-content")
            for each in search_ingredient_html:
                islist_ingredient = each.find_all("li")
                if islist_ingredient:
                    for is_ingredient in islist_ingredient:
                        text = is_ingredient.text
                        print(text)
                else:
                    list_ingredient = each.find_all("p")
                    for is_ingredient in list_ingredient:
                        text = is_ingredient.text
                        if "Ingredients" in text:
                            print(text)

            # lines = text.split("\n")
            # list = []
            # for line in lines:
            #     list.append(line.strip())

            # compare_ingred(search_product_name, list)

            # ###將成分存入json檔###
            # with open("ingred_paris.json", "w", encoding="utf-8") as f:
            #     json.dump(ingred_json, f, ensure_ascii=False, indent=4)
            #     # print(f"ingredient:{list}")
        print(f"----------------------")


if __name__ == "__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    ingred_json = []
    #get_SKII()
    get_PARIS()
