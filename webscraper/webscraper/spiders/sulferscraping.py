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
writer.writerow(["product-url"])

produrl = []
subprodurl = []

with open(r'C:\Users\dgh00\Desktop\Web scrapper\webscraper\webscraper\sulferone.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    
    for a in soup.find_all('a', {"class":"proFeaturedImage"}, href=True):
        #print(a['href'])
        produrl.append("https://sulfur.one/"+a['href'])

for i in range(486):
    writer.writerow([produrl[i]])

for i in range(487):
    PATH = r"C:\Users\dgh00\Desktop\Web scrapper\webscraper\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(produrl[i])

    try:
        tempx = driver.find_element_by_class_name('product-single__thumbnail')  
        .append(tempx.text)
        print("details clicked")
    except:
        details.append(NULL)
        continue

    


