import time
from datetime import date
import json 
from os import path

import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType

import random

def vote():
    driver = webdriver.Chrome()
    #driver.get('https://www.10best.com/awards/travel/best-wellness-retreat/eupepsia-bland-va/');
    driver.get('https://bit.ly/458INKO')
    time.sleep(3)
    
    try:
        driver.find_element_by_id("onetrust-reject-all-handler").click()
    except:
        pass

    time.sleep(1)
    driver.find_element_by_id("awardVoteButton").click()
    time.sleep(5)

    x = driver.find_elements_by_class_name("error")
    if x:
        print(x)
        time.sleep(1)
        return 0

    driver.quit()
    return 1

def vote_script():
    count = 0
    while count < 1000:
        try:
            success = vote()
            if not success:
                print("ip limit reached")
                break

        except Exception as e:
           print(e)
           time.sleep(2)
        count = count+1
        print(count)

vote_script()
