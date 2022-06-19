from cmath import isnan
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os



data = pd.read_csv(os.getcwd() + "/data/cleaned_prof_data_v4.csv")

bad_professors = []
for i in range(data.shape[0]):
	
	if(data.iat[i,3] != "NOSCHOLARPAGE" and (isnan(data.iat[i,4]) or isnan(data.iat[i,5]))):
		bad_professors.append({
			"Name": data.iat[i,0],
			"University": data.iat[i,1],
			"id": data.iat[i,3]
		})
		print("Name: " + data.iat[i,0] + " | " + "University: " + data.iat[i,1]  + " | " + "id: " + data.iat[i,3] )

pd.DataFrame(bad_professors).to_csv("bad-professors.csv")
