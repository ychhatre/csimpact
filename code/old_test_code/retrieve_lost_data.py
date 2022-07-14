from cmath import isnan
import time
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re


# options = webdriver.ChromeOptions()
# # options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver.get("https://scholar.google.com/citations?user=mR1GK28AAAAJ&hl=en&oi=ao")
# print(driver.current_url.split("=")[1].split("&")[0])

good_professors = []
count = 0
# data = pd.read_csv(os.getcwd() + "/data/cleaned_prof_data_v4.csv")
# print(len("mR1GK28AAAAJ"))

# for i in range(data.shape[0]):
# 	if(len(data.iat[i,3]) != 12 and len(data.iat[i,3]) != 13 and len(data.iat[i,3]) != 6):
# 		count+= 1
# 		print(len(data.iat[i,3]))
# 		print(data.iat[i,0])
# print(len(data.iat[i,3]))

# print(count)

data = pd.read_csv(
    "/Users/yashchhatre/Documents/csimpact/data/cleaned_prof_data_v4.csv")


for i in range(data.shape[0]):
    if(data.iat[i, 3] == "NOSCHOLARPAGE" or data.iat[i,3] == "#NAME?" or isnan(data.iat[i,4]) or isnan(data.iat[i,5])):
    	count += 1
    # good_professors.append({
    #     "Name": data.iat[i, 0],
    #     "University": data.iat[i, 1],
    #     "id": data.iat[i, 3]
    # })
    # print("Name: " + data.iat[i, 0] + " | " + "University: " +
    #       data.iat[i, 1] + " | " + "id: " + data.iat[i, 3])
print(count)
# pd.DataFrame(bad_professors).to_csv("bad-professors.csv")
