from cmath import isnan
import os
from random import random
import time
from typing import Any
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import writer
from bs4 import BeautifulSoup


# read the data from a file
data = pd.read_csv(os.getcwd() + "/data/cleaned_prof_data_v4.csv")

# initialize web driver for selenium
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(random() * 10)


def findMaxCitations(web_elements: list):
    indOfMax = 0
    maxVal = 0
    for i in range(len(web_elements)):
        val = int(web_elements[i].text.split(" - ")[2].split(" ")[2])
        if val > maxVal:
            maxVal = val
            indOfMax = i
        else:
            continue
    return web_elements[indOfMax]


# loop through and find all professors with wrong / no google scholar ID
professors = []
professorExists = True

for i in range(1201, 2001):
    
    # initialize values
    scholar_id = data.iat[i, 3]
    citation = data.iat[i, 4]
    h_index = data.iat[i, 5]

    if (data.iat[i, 3] == "NOSCHOLARPAGE" or data.iat[i, 3] == "#NAME?" or isnan(data.iat[i, 4]) or isnan(data.iat[i, 5])):
        # launch URL
        driver.get("https://scholar.google.com")

        # identify search box
        box = driver.find_element(By.NAME, "q")

        # enter search text
        box.send_keys(data.iat[i, 0])

        # make search
        box.send_keys(Keys.ENTER)

        # in the case that the author pops up as a recommended option
        try:
            link = driver.find_element(
                By.XPATH, "//*[@id='gs_res_ccl_mid']/div[1]/table/tbody/tr/td[2]/h4/a")
            link.click()
            time.sleep(random() * 3)
            
        except:
            try:
                # in the case there are multiple options in the recommended table
                list_of_elements = driver.find_element(
                    By.XPATH, "//*[@id='gs_res_ccl_mid']/div[1]/table/tbody/tr/td[2]").find_elements(By.TAG_NAME, "div")
                max_element = findMaxCitations(list_of_elements)
                max_element.find_element(By.TAG_NAME, "a").click()
                time.sleep(random() * 5)
            except:
                # otherwise loop through all the divs and find the correct professor
                elements_list = driver.find_element(
                    By.XPATH, "//*[@id='gs_res_ccl_mid']/div[1]").find_element(By.CLASS_NAME, "gs_a").find_elements(By.TAG_NAME, "a")
                if elements_list: 
                    for element in elements_list:  # looping through the number of professors in the link
                        try:
                            element.find_element(By.TAG_NAME, "b")
                            element.click()
                            professorExists = True
                            break
                        except NoSuchElementException:
                            professorExists = False
                            continue  # in the case that the element is not found
                    # give time for html / css / js to load
                    time.sleep(random() * 5)
                else: 
                    professorExists = False 

        # retrieve citation, h-index, and scholar_id for that prof
        if professorExists:
            scholar_id = driver.current_url.split("=")[1].split("&")[0]
            citation = int(driver.find_element(
                By.XPATH, "//*[@id='gsc_rsb_st']/tbody/tr[1]/td[2]").text)
            h_index = int(driver.find_element(
                By.XPATH, "//*[@id='gsc_rsb_st']/tbody/tr[2]/td[2]").text)
            time.sleep(random() * 5)
        else:
            scholar_id = None
            citation = None
            h_index = None
    
    print(i)
    professor = { 
        "Name": data.iat[i, 0],
        "affiliation": data.iat[i, 1],
        "homepage": data.iat[i, 2],
        "scholar-id": scholar_id,
        "citations": citation,
        "h-index": h_index
    }
    print(professor)
    professors.append(professor)


df = pd.DataFrame(professors)
df.to_csv("data/cleaned_prof_data_v5_4.csv")
