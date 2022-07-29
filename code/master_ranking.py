import pandas as pd
import os

colleges = pd.read_csv(os.getcwd().replace('code', '') + '/data/colleges.csv')

avg_citations = pd.read_csv(os.getcwd().replace('code', '') + '/data/ranking_data/avg_citations_ranking.csv')
avg_h_index = pd.read_csv(os.getcwd().replace('code', '') + '/data/ranking_data/avg_h_index_ranking.csv')
total_citations = pd.read_csv(os.getcwd().replace('code', '') + '/data/ranking_data/total_citations_ranking.csv')
total_h_index = pd.read_csv(os.getcwd().replace('code', '') + '/data/ranking_data/total_h_index_ranking.csv')

my_list = [avg_citations,avg_h_index,total_citations,total_h_index]

totals = []
count = []

df = pd.DataFrame(columns=['college'])

for i in range(colleges.shape[0]):
    college = colleges.iloc[i,0]
    college_total_rank = 0
    counter = 0
    for item in my_list:
        row=item.loc[item['college'] == college]
        #check if there is a match in the data
        if row.shape[0] ==1:
            counter+=1
        row_index = row.index.tolist()[0]
        college_total_rank+=row_index
    totals.append(college_total_rank)
    count.append(counter)

average_rank = []
for i in range(len(totals)):
    average_rank.append(totals[i]/count[i])

avg_rank_df = pd.DataFrame({'avg_rank':average_rank})

college_avg_rank = pd.concat([colleges,avg_rank_df],axis = 1)

college_avg_rank_sorted = college_avg_rank.sort_values('avg_rank', ascending = True)

college_avg_rank_sorted = college_avg_rank_sorted.reset_index(drop = True)

college_avg_rank_sorted.to_csv(os.getcwd().replace('code', '') + '/data/college_avg_rank.csv', index = False)