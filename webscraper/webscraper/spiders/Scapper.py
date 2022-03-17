from asyncio.windows_events import NULL
from typing import final
from bs4 import BeautifulSoup
import csv 
import requests
import numpy as np

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

outfile = open('results.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["product-url","name", "price","image-url","details","dimension"])

produrl = []
name = []
price = []
imglink = []
details = []
dimensions = []


with open(r'C:\Users\dgh00\Desktop\Web scrapper\webscraper\webscraper\crateandbarrel.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    
    for a in soup.find_all('a', {"class":"product-name-link"}, href=True):
        #print(a['href'])
        produrl.append("https://www.crateandbarrel.com"+a['href'])
    
    rows=soup.find_all('span', {"class":"sr-only favorite-item-name"})
    for row in rows:
        #print(row.get_text())
        name.append(row.get_text())
    
    rows=soup.find_all('span', {"class":"regPrice"})
    for row in rows:
        #print(row.get_text())
        price.append(row.get_text())
        
    for img in soup.find_all('img', {"class":"product-image"}, src=True):
        #print(img['src'])
        imglink.append(img['src'])
    
for i in range(128):
    PATH = r"C:\Users\dgh00\Desktop\Web scrapper\webscraper\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(produrl[i])
    
    try:
        tempx = driver.find_element_by_class_name('details-description')  
        details.append(tempx.text)
        print("details clicked")
    except:
        details.append(NULL)
        continue
    try:
        element =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dimension-container"))
        )
        element.click()
        print("dimensions clicked")
        tempx = driver.find_element_by_class_name('dimension-container')  
        dimensions.append(tempx.text)
    except:
        dimensions.append(NULL)
        continue
    finally:
        print("prodnum "+str(i)+" details extracted" )
        driver.close()
        

for i in range(128):
    writer.writerow([produrl[i], name[i], price[i], imglink[i], details[i], dimensions[i]])


    


