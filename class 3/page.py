# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import itertools


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.daraz.pk/catalog/?_keyori=ss&from=search_history&page=1&q=laptop&spm=a2a0e.tm80335142.search.2.35e34076TrpsvS&sugg=laptop_0_1")
# # for i in itertools.count():
# #     print(i)

# # title_num = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[2]/a').text
# # print("Number: ",title_num)

# for page in range(1, 4):
#     p = str(page)
#     title_num = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li['+p+']/a').text
# print("Number: ",title_num)


# # for i in itertools.count():
# #     print(i)
# #     if i == title_num:
# #         print(i)
# #         break
# # for page in range(1,3):
# #     p = str(page)
# #     driver.get("https://www.daraz.pk/catalog/?_keyori=ss&clickTrackInfo=abId--379294__textId--8604400042594750176__score--346200.0__pvid--130c1dcc-9425-49e2-974e-b2f1f46af4fb__matchType--1__matchList--1__listNo--0__inputQuery--lap__srcQuery--laptop__spellQuery--laptop__ctrScore--0.0__cvrScore--0.0&from=suggest_normal&page="+p+"&q=laptop&spm=a2a0e.tm80335142.search.2.62aa4076qlVAK0&sugg=laptop_0_1")
# #     print(f"PAGE: {page} \n")
    
#     # for i in range(1,41):
#     #     j = str(i)
#     #     title = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text
#     #     print(f"Title {i}:",title)


# time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# STEP 1: Open the first page to get total number of pages
driver.get("https://www.daraz.pk/catalog/?q=laptop")

time.sleep(3)  # wait for page to load

# STEP 2: Find the pagination items
pagination_items = driver.find_elements(By.CSS_SELECTOR, "li.ant-pagination-item")

# STEP 3: Get the last page number
if pagination_items:
    total_pages = int(pagination_items[-1].text)
else:
    total_pages = 1  # fallback if no pagination found

print(f"Total Pages Found: {total_pages}")

# STEP 4: Now loop through all pages (limit if needed)
# for page in range(98, total_pages + 1):
#     print(f"\n--- PAGE {page} ---")
#     driver.get(f"https://www.daraz.pk/catalog/?q=laptop&page={page}")
    # time.sleep(1)

    # for i in range(1, 41):  # 40 products max per page
    #     try:
    #         title = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[2]/a').text
    #         print(f"Title {i}: {title}")
    #     except:
    #         print(f"Title {i}: Not found or element missing.")

time.sleep(5)

