from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
options = Options()
driver = webdriver.Chrome(options=options)

driver.get('https://free-proxy-list.net/')
driver.maximize_window()

proxy_ip_list = []
port_list = []
ip = driver.find_elements(By.CSS_SELECTOR,'#list > div > div.table-responsive > div > table > tbody > tr')
for i in range(1, len(ip)+1):
    j = str(i)
    all_ip = driver.find_element(By.CSS_SELECTOR,'#list > div > div.table-responsive > div > table > tbody > tr:nth-child('+j+') > td:nth-child(1)').text
    # print(i,": ",all_ip)
    all_port = driver.find_element(By.CSS_SELECTOR,'#list > div > div.table-responsive > div > table > tbody > tr:nth-child('+j+') > td:nth-child(2)').text

    port_list.append(all_port)
    proxy_ip_list.append(all_ip)

actual_ip_port = [f"{a}:{b}" for a, b in zip(proxy_ip_list, port_list)]

PROXY = random.choice(actual_ip_port)
print("proxy ip:", PROXY)

options.add_argument(f'--proxy-server=https://{PROXY}')
driver.get("https://quotes.toscrape.com/")

texts = driver.find_elements(By.CLASS_NAME,'quote')
for t in range(1,len(texts)):
    all_text = driver.find_elements(By.CLASS_NAME,'quote')
    print(all_text[t].text)


time.sleep(10)