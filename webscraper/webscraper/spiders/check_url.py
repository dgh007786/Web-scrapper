import requests
from bs4 import BeautifulSoup 

r=requests.get("https://www.crateandbarrel.com/furniture/beds/")
print(r.status_code)