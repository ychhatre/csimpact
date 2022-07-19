from cmath import isnan
import os
from random import random
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import writer

# read the data from a file
data = pd.read_csv(os.getcwd() + "/data/cleaned_prof_data_v4.csv")

# initialize web driver for selenium
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(random() * 10)

data = pd.read_csv(os.getcwd() + "/data/cleaned_prof_data_v4.csv")

driver.get("https://scholar.google.com/citations?user=C1skWKgAAAAJ&hl=en&oi=ao")
last_height = driver.execute_script("return document.body.scrollHeight")
print(last_height)
 
# loop through professors 
# for i in range(data.shape[0]): 
# 	# fetch the professors url 
# 	driver.get("https://scholar.google.com/citations?user=C1skWKgAAAAJ&hl=en&oi=ao")
# 	time.sleep(3)

	# load the professors entire page by scrolling / hitting next 

	# grab the body of the professors 

	# use find_min function to find earliest paper 

	# add to a list of professors

	#upload the professors to a spreadsheet 
for i in range(6): 
	try:
		driver.find_element(By.XPATH, "//*[@id='gsc_bpf_more']").click()
	except: 
		break
papers = driver.find_element(By.XPATH, "//*[@id='gsc_a_b']").find_elements(By.CLASS_NAME, "gsc_a_tr")

for i in range(len(papers)): 
	val = papers[i].find_element(By.CLASS_NAME, "gsc_a_h gsc_a_hc gs_ibl")
	

# while True:
# # Scroll down to bottom
# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 	# Wait to load page
# 	time.sleep(0.5)

# 	# Calculate new scroll height and compare with last scroll height
# 	new_height = driver.execute_script("return document.body.scrollHeight")
# 	if new_height == last_height:
# 		break
# 	last_height = new_height