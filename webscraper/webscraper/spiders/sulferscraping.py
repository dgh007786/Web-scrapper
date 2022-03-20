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

from urllib.request import Request, urlopen, URLError

#for downloading images
import os

subprodurl = []
errdownld = []

#url = input()
url="https://sulfur.one/products/argos-natsu-bench"
req = Request(url)
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print("We failed to reach a server")
        print("Reason: ", e.reason)
    elif hasattr(e, 'code'):
        print("The server couldn\'t fulfill the request.")
        print("Error code: ', e.code")
else:
    print("URL is good!")


PATH = r"C:\Users\dgh00\Desktop\Web scrapper\webscraper\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(url)

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
   
for a in soup.find_all('a', {"class":"product-single__thumbnail"}, href=True):
    #print(a['href'])
    subprodurl.append("http:"+a['href'])

driver.close()
os.chdir(r'C:\Users\dgh00\Desktop\Web scrapper\webscraper\webscraper\spiders\subprodimg')

i=0

for img in subprodurl:
    # We can split the file based upon / and extract the last split within the python list below:
    file_name = str(i)+".jpg"
    i=i+1
    print(f"This is the file name: {file_name}")
    # Now let's send a request to the image URL:
    r = requests.get(img, stream=True)
    # We can check that the status code is 200 before doing anything else:
    if r.status_code == 200:
        # This command below will allow us to write the data to a file as binary:
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
    else:
        # We will write all of the images back to the broken_images list:
        errdownld.append(img)

print(errdownld)

#checking currunt directory
# cwd = os.getcwd()
# print("Current working directory: {0}".format(cwd))

