import json
import random
import time
from datetime import date
from os import path

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import Select


def vote():
    driver = webdriver.Chrome()
    # driver.get('https://www.10best.com/awards/travel/best-wellness-retreat/eupepsia-bland-va/');
    driver.get("https://bit.ly/458INKO")
    time.sleep(2)

    try:
        driver.find_element(By.ID, "onetrust-reject-all-handler").click()
        time.sleep(1)
    except Exception:
        pass

    element = driver.find_element(By.XPATH, "//button[text()='Vote Now']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Vote Now']").click()
    time.sleep(3)

    try:
        x = driver.find_elements(By.CLASS_NAME, "error")
        if x:
            print(x)
            time.sleep(1)
            return 0
    except Exception:
        pass

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
        count = count + 1
        print(count)


vote_script()
