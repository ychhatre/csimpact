import pandas as pd
import os

data = pd.read_csv(os.getcwd().replace('code/','')+'/data/output-professors-data.csv')
data_2 = data.groupby(['homepage', 'scholar_id']).first()
data_3 = data_2.reset_index().drop(data_2.columns[0], axis=1)
data_4 = data_3[['name', 'affiliation', 'homepage', 'scholar_id', 'citations', 'h-index']]
#clean up the names by removing zeros from the end (for example A. P. Vinod 0001)
for i in range(data_4.shape[0]):
    temp = ''
    if '0' in data_4.iloc[i,0]:
        temp = data_4.iloc[i,0]
        temp = temp.split()
        temp.remove(temp[-1])
        data_4.iloc[i,0] = ' '.join(str(x) for x in temp)
        
data_4.loc[data_4['affiliation']==' Wichita State University'] = 'Wichita State University'
data_4 = data_4.sort_values('affiliation', ascending=True).reset_index(drop = True)
data_4.to_csv(os.getcwd() +'/data/cleaned_prof_data_v4.csv')