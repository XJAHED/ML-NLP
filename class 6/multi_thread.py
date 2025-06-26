from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import time
import threading
from selenium.webdriver.common.action_chains import ActionChains


# # driver.get('https://www.daraz.com.bd/routers/?page=1')
# link_list = ['https://www.daraz.com.bd/routers/?page=1','https://www.daraz.com.bd/routers/?page=2','https://www.daraz.com.bd/routers/?page=3','https://www.daraz.com.bd/routers/?page=4','https://www.daraz.com.bd/routers/?page=5']


# def scrape_func(link):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(link)
#     print(f"Thread______{threading.current_thread().name} Scraped")
# with ThreadPoolExecutor(max_workers=2) as executor:
#     execute = [executor.submit(scrape_func, link) for link in link_list]

# time.sleep(5)


def scrape_func(link): 
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)
    action = ActionChains(driver)
    
    print(f"Thread {threading.current_thread().name} scraped: {link}")
    
    
    
    pagination = driver.find_elements(By.CSS_SELECTOR,'#author-list > div:nth-child(4) > section > div.text-center > div > a')
    for p in range(1,len(pagination)):
        i = str(p)
        total_author_page = driver.find_element(By.XPATH,'//*[@id="author-list"]/div[3]/section/div[3]/div/a['+i+']').text
    print(total_author_page)

link_list = [f"https://www.rokomari.com/book/authors?page={i}" for i in range(1, 10)]

with ThreadPoolExecutor(max_workers=5) as executor:
    execute = [executor.submit(scrape_func, link) for link in link_list]
    
    author = driver.find_element(By.XPATH, '//*[@id="ts--desktop-menu"]/div[2]/div/div[1]')
    action.move_to_element(author).click().perform()