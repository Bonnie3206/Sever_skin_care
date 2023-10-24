from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # 需要安裝Chrome驅動程式

# 前往網頁
url_lancome = "https://www.lancome-usa.com/skincare/by-category/toners/"
driver.get(url_lancome)

try:
    # 使用等待直到至少一個具有指定類別的元素出現
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "c-product-tile__name"))
    )

    # 提取所有符合條件的元素的文本
    for element in elements:
        text = element.text
        print(text)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # 關閉瀏覽器
    driver.quit()
