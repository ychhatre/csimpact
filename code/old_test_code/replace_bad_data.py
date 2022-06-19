from cmath import isnan
import os
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# read the data from a file
data = pd.read_csv(os.getcwd() + "/data/cleaned_prof_data_v4.csv")

# initialize web driver for selenium
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(0.5)

# loop through and find all professors with wrong / no google scholar ID
bad_professors = []

for i in range(10):  # temporary test with 10 users

    if(data.iat[i, 3] != "NOSCHOLARPAGE" and (isnan(data.iat[i, 4]) or isnan(data.iat[i, 5]))):
        print("Name: " + data.iat[i, 0] + " | " + "University: " +
              data.iat[i, 1] + " | " + "id: " + data.iat[i, 3])
        bad_professors.append({
            "Name": data.iat[i, 0],
            "University": data.iat[i, 1],
            "id": data.iat[i, 3]
        })

        # launch URL
        driver.get("https://scholar.google.com")

        # identify search box
        box = driver.find_element(By.NAME, "q")

        # enter search text
        box.send_keys(data.iat[i, 0])
        time.sleep(0.2)

        # make search
        box.send_keys(Keys.ENTER)
        field = driver.find_element(
            By.XPATH, "//*[@id='gs_res_ccl_mid']/div[1]/div[2]/div[1]/a[1]")

        # click on the found prof's path
        field.click()

        # retrieve citation and h-index for that prof
        citation = driver.find_element(
            By.XPATH, "//*[@id='gsc_rsb_st']/tbody/tr[1]/td[2]")
        h_index = driver.find_element(By.XPATH, "//*[@id='gsc_rsb_st']/tbody/tr[2]/td[2]")
	
        time.sleep(5)

# once found append the correct h-index and citation count to that professor

# once the information has been appended upload to a new csv file with more accurate data
