from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.refresh()

driver.get('https://www.daraz.pk/products/4gb-32gb-2029-360-i629981730-s2953067643.html')

height = driver.execute_script('return document.body.scrollHeight')
print(height)

for i in range(0, height,90):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

# comment = driver.find_elements(By.CLASS_NAME, 'content')
# for i in comment:
#     cmt = i.text
#     print(f"Comment:{cmt}\n\n")

pagination = driver.find_elements(By.CLASS_NAME,'next-pagination-pages')
for i in pagination:
    print(i.text)

# import requests
# from bs4 import BeautifulSoup

# base_url = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.2.35e34076dqib3v&q=laptop&_keyori=ss&from=search_history&sugg=laptop_0_1"
# total_pages = 16  # যত পেজ স্ক্র্যাপ করতে চাও

# for page in range(1, total_pages + 1):
#     url = base_url + str(page)
#     print(f"Scraping page {page}...")

#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     # ধরো, সব প্রোডাক্ট একটা div-এ আছে যার class "product-item"
#     products = soup.find_all("div", class_="product-item")

#     for product in products:
#         name = product.find("h2").text.strip()
#         price = product.find("span", class_="price").text.strip()
#         print(f"{name} - {price}")
