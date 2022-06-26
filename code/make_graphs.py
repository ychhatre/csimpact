import pandas as pd
import time
import plotly.express as px

colleges = pd.read_csv('/Users/kevins/Documents/CSImpact/data/colleges.csv')

college_data = pd.DataFrame()
def plot(college):
    i = colleges.index[colleges['college'] == f'{college}'].tolist()[0]
    college_data = pd.read_csv(f'/Users/kevins/Documents/CSImpact/data/college_data/college{i}.csv')
    missing_id_rows = college_data.loc[college_data['scholar_id'] == 'NOSCHOLARPAGE']
    rows_to_plot = college_data.loc[college_data['scholar_id'] != 'NOSCHOLARPAGE']

    h_indexes = rows_to_plot['h-index'].sort_values()
    names = rows_to_plot['name']
    
    if(len(names)>5):
        fig_width = len(names) * 20 + 100
    else:
        fig_width= 400
    
    fig = px.scatter(x = names, y = h_indexes, labels = {'x':'name', 'y':'h-index'}, title = f'{college}', width = fig_width, height = 1000)
    fig.show()
    
    time.sleep(3)
    
    citations = rows_to_plot['citations'].sort_values()
    names = rows_to_plot['name']

    fig = px.scatter(x = names, y = citations, labels = {'x':'name', 'y':'citations'}, title = f'{college}', width = fig_width, height = 1000)
    fig.show()
    
    time.sleep(3)
    

    
    
for i in range(colleges.shape[0]):
    plot(f'{colleges.iloc[i,0]}')