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
from os.path import isfile, join 

#opencvforvideo
import cv2  # pip install opencv-python 


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

titleel = (soup.find('title').text)
title = titleel.strip()
title = title.removesuffix(' - SULFUR')
print(title)   

for a in soup.find_all('a', {"class":"product-single__thumbnail"}, href=True):
    #print(a['href'])
    subprodurl.append("http:"+a['href'])

driver.close()
parent_dir = r'C:\Users\dgh00\Desktop\Web scrapper\webscraper\webscraper\spiders\subprodimg'
directory = title
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
os.chdir(path)

i=0

for img in subprodurl:
    # We can split the file based upon / and extract the last split within the python list below:
    file_name = title+str(i)+".jpg"
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

def convert_pictures_to_video(pathIn, pathOut, fps, time):
    ''' this function converts images to video'''
    frame_array=[]
    files=[f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]
    for i in range (len(files)):
        filename=pathIn+files[i]
        '''reading images'''
        img=cv2.imread(filename)
        img=cv2.resize(img,(1080,1080))
        height, width, layers = img.shape
        size=(width,height)

        for k in range (time):
            frame_array.append(img)
    out=cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'),fps,size)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(frame_array)):
        cv2.putText(frame_array[i],title.removesuffix('-'),(600, 50),font,1,(72, 132, 189),2,cv2.LINE_4)
        cv2.putText(frame_array[i],'Now Available',(50, 1000),font,1,(72, 132, 189),2,cv2.LINE_4)
        cv2.putText(frame_array[i],'on Sulfur.one',(50, 1050),font,1,(72, 132, 189),2,cv2.LINE_4)
        cv2.imshow('video', frame_array[i])
        out.write(frame_array[i])
    out.release()

directory= path
pathIn=directory+'/'
vname=title+'.mp4'
pathOut=pathIn+vname
fps=1
time=1 # the duration of each picture in the video
convert_pictures_to_video(pathIn, pathOut, fps, time)