from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.daraz.com.bd/routers/?page=1')


title = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text

price = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span').text
link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')
image = driver.find_element(By.XPATH,'(//div[@data-qa-locator="product-item"]//img)[1]').get_attribute('src')

print("Title:",title)
print("Price:",price)
print("Link:",link)
print("Image:",image)

# image download
img_data = requests.get(image).content
path = "Daraz_image.jpg"
with open( path, 'wb') as i:
    i.write(img_data)
print("Image downloaded")


time.sleep(20)
