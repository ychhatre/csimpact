import pandas as pd
import os

data = pd.read_csv(os.getcwd().replace('code/','')+'/data/cleaned_prof_data_v5.csv')

colleges = sorted(list(set(list(data['affiliation']))))

os.mkdir(os.getcwd().replace('code/','')+'/data/college_data')
for i in range(len(colleges)):
    college = colleges[i]
    sub_data = data.drop(['affiliation'], axis = 1).loc[data['affiliation'] == college]
    filename = f'college{i}'
    sub_data.to_csv(f'/Users/kevins/Documents/CSImpact/data/college_data/{filename}.csv', index = False)