import pandas as pd
import os

colleges = pd.read_csv(os.getcwd().replace('code', '') + '/data/colleges.csv')

number_valid_professors = []
h_index_sum = []
citations_sum = []
average_h_index = []
average_citations = []

for i in range(colleges.shape[0]):
    college_data = pd.read_csv(os.getcwd().replace('code', '') + '/data/college_data/college'+str(i)+'.csv')
    valid_h_index = list(college_data.loc[~pd.isna(college_data['h-index'])]['h-index'])
    for item in valid_h_index:
        if item != 'None':
            item = int(float(item))
        else:
            item = 0
    total_h_index = sum(valid_h_index)
    h_index_sum.append(total_h_index)
    
    
    
    
    valid_citations = list(college_data.loc[~pd.isna(college_data['citations'])]['citations'])
    for item in valid_citations:
        if item != 'None':
            temp = int(float(item))
            item = temp
        else:
            item = 0
    total_citations = sum(valid_citations)
    citations_sum.append(total_citations)
    
    num_profs = len(valid_h_index)
    
    number_valid_professors.append(num_profs)
    if num_profs != 0:
        average_h_index.append(float(total_h_index)/num_profs)
        average_citations.append(float(total_citations)/num_profs)
    else:
        average_h_index.append(0)
        average_citations.append(0)


    
all_college_stats = pd.DataFrame()
all_college_stats['number_professors'] = number_valid_professors
all_college_stats['total_h_index'] = h_index_sum
all_college_stats['average_h_index'] = average_h_index
all_college_stats['total_citations'] = citations_sum
all_college_stats['average_citations'] = average_citations

ranked_h_index = all_college_stats.sort_values('total_h_index', ascending = False)
total_h_index_df = pd.DataFrame()
total_h_index_list = []
for row in ranked_h_index.iterrows():
    total_h_index_list.append(colleges.iloc[row[0],0])
total_h_index_df['college'] = total_h_index_list
total_h_index_df.to_csv(os.getcwd().replace('code', '') + '/data/total_h_index_ranking.csv', index = False)


ranked_citations = all_college_stats.sort_values('total_citations', ascending = False)
total_citations_df = pd.DataFrame()
total_citations_list = []
for row in ranked_citations.iterrows():
    total_citations_list.append(colleges.iloc[row[0],0])
total_citations_df['college'] = total_citations_list
total_citations_df.to_csv(os.getcwd().replace('code', '') + '/data/total_citations_ranking.csv', index = False)


ranked_avg_h_index = all_college_stats.sort_values('average_h_index', ascending = False)
avg_h_index_df = pd.DataFrame()
avg_h_index_list = []
for row in ranked_avg_h_index.iterrows():
    avg_h_index_list.append(colleges.iloc[row[0],0])
avg_h_index_df['college'] = avg_h_index_list
avg_h_index_df.to_csv(os.getcwd().replace('code', '') + '/data/avg_h_index_ranking.csv', index = False)


ranked_avg_citations = all_college_stats.sort_values('average_citations', ascending = False)
avg_citations_df = pd.DataFrame()
avg_citations_list = []
for row in ranked_avg_citations.iterrows():
    avg_citations_list.append(colleges.iloc[row[0],0])
avg_citations_df['college'] = avg_citations_list
avg_citations_df.to_csv(os.getcwd().replace('code', '') + '/data/avg_citations_ranking.csv', index = False)