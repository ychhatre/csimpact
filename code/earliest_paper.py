from bs4 import BeautifulSoup
import pandas as pd
import os
import requests


data = pd.read_csv(str(os.getcwd()).replace('code', '')+'/data/cleaned_prof_data_v4.csv')


#clean up data
data = data.sort_values('name')
data = data.reset_index(drop = True)

total_rows = data.shape[0]
earliest_paper_years = []
for i in range(total_rows):
    s_id = data.iloc[i,3]
    if not pd.isna(data.iloc[i,4]):
        html_text = requests.get(f'https://scholar.google.com/citations?hl=en&user={s_id}&view_op=list_works&sortby=pubdate').text
        soup = BeautifulSoup(html_text, 'lxml')
        values = soup.find_all('button', id = 'gsc_bpf_more')
        
        driver.get(f'https://scholar.google.com/citations?hl=en&user={s_id}&view_op=list_works&sortby=pubdate')
        text1 = driver.page_source
        while True:
            try:
                button = driver.find_element_by_id('gsc_bpf_more')
                button.click()
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
            if(year != ''):
                years_text.append(year.text)
        clean_years = [int(year_text) for year_text in years_text if year_text != '']
        min_y = min(clean_years)
        earliest_paper_years.append(min_y)
        print(clean_years)
        print(min_y)

    else:
        earliest_paper_years.append('')