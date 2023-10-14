import requests
from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.ptt.cc/bbs/TY_Research/index.html'

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

#request
req = request.Request(url, headers=headers)
#response
res = request.urlopen(req)

print(res.read().decode('utf8'))


#url = 'https://www.ntbt.gov.tw/multiplehtml/d7d124569cf04124ae5a042b4d9f16f7'

# # 定义要爬取的网址
# url = "https://sk-ii.com.tw/our-products/toner"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# response = requests.get(url, headers=headers)

# # 发送 HTTP 请求
# response = requests.get(url)

# # 检查请求是否成功
# if response.status_code == 200:
#     # 使用 BeautifulSoup 解析 HTML 内容
#     soup = BeautifulSoup(response.text, "html.parser")

#     # 提取化妆水的标题
#     title = soup.find("h1", class_="product-title").text.strip()

#     # 提取化妆水的成分信息
#     ingredients = soup.find("div", class_="product-detail__ingredients").text.strip()

#     # 打印化妆水的信息（您也可以将其保存到文件或数据库）
#     print("产品名称:", title)
#     print("成分:", ingredients)
# else:
#     print("请求失败，状态码:", response.status_code)

