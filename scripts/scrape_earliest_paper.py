from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager
import os
from random import random
from selenium.webdriver.common.by import By

#replace path
data = pd.read_csv(str(os.getcwd()).replace('code', '')+'/data/cleaned_prof_data_v4.csv')


#clean up data
data = data.sort_values('affiliation')
data = data.reset_index(drop = True)

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(random() * 10)
print(random()*10)

earliest_paper_years = []
total_rows = data.shape[0]


for i in range(10):
    s_id = data.iloc[i,3]
    if not pd.isna(data.iloc[i,4]):
        html_text = requests.get(f'https://scholar.google.com/citations?hl=en&user={s_id}&view_op=list_works&sortby=pubdate').text
        soup = BeautifulSoup(html_text, 'lxml')
        values = soup.find_all('button', id = 'gsc_bpf_more')
        
        
        
        driver.get(f'https://scholar.google.com/citations?hl=en&user={s_id}&view_op=list_works&sortby=pubdate')
        text1 = driver.page_source
        while True:
            try:
                button = driver.find_element(By.ID,'gsc_bpf_more')
                button.click()
                time.sleep(0.5)
            except ElementNotInteractableException:
                final_text = driver.page_source
                break
            except NoSuchElementException:
                driver.get(f'https://scholar.google.com/citations?hl=en&user={s_id}&view_op=list_works&sortby=pubdate')
                break
            text2=driver.page_source
            if text1 == text2:
                final_text = text2
                break
            else:
                text1 = text2

        final_soup = BeautifulSoup(final_text, 'lxml')
        years = final_soup.find_all('td',class_ = 'gsc_a_y')
        years_text = []
        for year in years:
            years_text.append(year.text)
        clean_years = [int(year_text) for year_text in years_text if year_text != '']
        min_y = min(clean_years)
        earliest_paper_years.append(min_y)
        print(data.iloc[i,0])
        print(min_y)

    else:
        earliest_paper_years.append('')

df = pd.DataFrame({'earliest_paper': earliest_paper_years})
df.to_csv((os.getcwd()).replace('code', '')+'/data/earliest_paper.csv')