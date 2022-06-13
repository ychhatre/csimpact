import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv

# get the data from the csv file
data = pd.read_csv(os.getcwd() + "/data/all_prof_data.csv")

professors = []
# get the scholar's h-index / citation number
for i in range(data.shape[0]):  # loop through all the rows in the csv
    professor = {
        "name": data.iat[i, 0],
        "affiliation": data.iat[i, 1],
        "homepage": data.iat[i, 2],
        "scholar_id": data.iat[i, 3]
    }
    if (data.iat[i, 3] != "NOSCHOLARPAGE"):
        text = requests.get(
            "https://scholar.google.com/citations?hl=en&user=" + data.iat[i, 3]).text
        soup = BeautifulSoup(text, 'lxml')
        values = soup.find_all('td', class_='gsc_rsb_std')
        if (len(values) != 0):
            professor["citations"] = int(values[0].text)
            professor["h-index"] = int(values[2].text)
        else:
            professor["citations"] = None
            professor["h-index"] = None
    else:
        professor["citations"] = None
        professor["h-index"] = None
    print(professor)
    professors.append(professor)

df = pd.DataFrame(professors)
df.to_csv("output-professors-data.csv")



