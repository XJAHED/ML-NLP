from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://www.daraz.pk/invisible-unisex-fashion-3/')

driver.maximize_window()

title_list = []
for page in range(1,3):
    driver.get(f'https://www.daraz.pk/invisible-unisex-fashion-3/?page={page}')

    for i in range(1,41):
        j = str(i)
        title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text 
        title_list.append(title)
        print("title:", title)
        # print(title_list)

# print(len(title_list))

time.sleep(1)