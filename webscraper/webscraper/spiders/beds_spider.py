from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import scrapy
from selenium import webdriver
from bs4 import BeautifulSoup

PATH = r"C:\Users\dgh00\Desktop\Web scrapper\webscraper\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.crateandbarrel.com/furniture/beds/")

# driver.find_element_by_xpath('//button[normalize-space()="View More Products"]').click()
element =  WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="View More Products"]'))
    )
element.click()
print('clicked')

try:
     element = WebDriverWait(driver, 50).until(
         EC.presence_of_element_located((By.XPATH, '//span[text()="Adjustable Metal Bed Frame"]'))
         )
     content = driver.page_source
     soup = BeautifulSoup(content) 
     with open("targetfile.html", "w", encoding='utf-8') as file:
         file.write(str(soup))
finally:
    driver.close()


