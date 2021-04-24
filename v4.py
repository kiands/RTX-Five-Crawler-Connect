#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import json
import time


# In[7]:


store = "https://24h.pchome.com.tw/store/DRADD4"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)


# In[8]:


entrance = driver.get(store)
soup = BeautifulSoup(driver.page_source, "lxml")


# In[9]:


date = "24"

def urlVerifier(soup):
    for item in soup.find_all(class_ = 'prod_info'):
        if item.find('b') == None:
            pass
        else:
            if date in item.find('b').text:
                stop = False
                return stop
            else:
                F5 = True
                return F5

def urlFinder(soup):
    for item in soup.find_all(class_ = 'prod_info'):
        if item.find('b') == None:
            pass
        else:
            if date in item.find('b').text:
                urls = item.findAll('a' ,href=True)
                result = "https:" + urls[0].get('href')
                return result
            else:
                pass

new_url = ''

refresh = True
while refresh:
    time.sleep(0.15)
    if urlVerifier(soup):
        driver.get(store)
    else:
        new_url = urlFinder(soup)
        break


# In[11]:


pchome = {'URL':new_url}
res = requests.post('http://127.0.0.1:5000/getURL',data = json.dumps(pchome))

