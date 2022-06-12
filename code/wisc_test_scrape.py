from bs4 import BeautifulSoup

import requests

import pandas as pd

wisc_data = pd.read_excel('/Users/kevins/Documents/CSImpact/data/wisc_madison.xlsx')

urls = list(wisc_data['Google_scholars_url'])

total_rows = range(wisc_data.shape[0])

citations_list = []

h_index_list = []

for i in total_rows:
    if not pd.isna(wisc_data.iloc[i,4]):
        gscholars_text = requests.get(urls[i]).text
        soup = BeautifulSoup(gscholars_text, 'lxml')
        values = soup.find_all('td', class_ = 'gsc_rsb_std')
        citations = values[0].text
        h_index = values[2].text
        citations_list.append(citations)
        h_index_list.append(h_index)
    else:
        citations_list.append('')
        h_index_list.append('')


index = []
for i in total_rows:
    index.append(i)

gscholar_values = pd.DataFrame()

gscholar_values['ScholarID'] = index

gscholar_values['h_index'] = h_index_list
gscholar_values['citations'] = citations_list

gscholar_values.to_csv('wisc_test_result')