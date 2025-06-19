from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.daraz.pk/computing/acer/?page=1")

pagination = driver.find_elements(By.CSS_SELECTOR,
    '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div.b7FXJ > div > ul > li.ant-pagination-item')

if pagination:
    total_pages = int(pagination[-1].text)
else:
    total_pages = 1

for page in range(1, total_pages + 1):
    driver.get(f"https://www.daraz.pk/computing/acer/?page={page}")
    print(f"\nPage Number: {page}")

    # Scroll to load all products
    for scroll in range(0, 5000, 500):
        driver.execute_script(f"window.scrollTo(0, {scroll});")
        time.sleep(0.3)

    products = driver.find_elements(By.CSS_SELECTOR,
        '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div.Bm3ON')

    for i in range(1, len(products) + 1):
        j = str(i)

        try:
            title = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[{j}]/div/div/div[2]/div[2]').text
        except:
            title = "Title not found"

        try:
            image_element = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[{j}]/div/div/div[1]/div/a/div/img')
            image = image_element.get_attribute('src')
            if not image or image.startswith("data:image"):
                image = image_element.get_attribute('data-src')
        except:
            image = "Image not found"

        try:
            link = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[{j}]/div/div/div[2]/div[2]/a').get_attribute('href')
        except:
            link = "Link not found"

        print(f"Title {j}: {title}")
        print(f"Image: {image}")
        print(f"Link: {link}\n")

time.sleep(10)
driver.quit()
