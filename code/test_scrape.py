import requests
from bs4 import BeautifulSoup

scholar_text = requests.get('https://scholar.google.com/citations?hl=en&user=CUbC2zYAAAAJ').text

soup = BeautifulSoup(scholar_text, 'lxml')

values = soup.find_all('td', class_ = 'gsc_rsb_std')

# print(values)

citations = values[0]
h_index = values[2]

print(citations.text)
print(h_index.text)