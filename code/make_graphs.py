import os
import pandas as pd
import time
import plotly.express as px
import plotly.graph_objects as go  
import matplotlib.pyplot as plt


colleges = pd.read_csv(str(os.getcwd()).replace('code', '') + '/data/colleges.csv')

college_data = pd.DataFrame()
def plot(college):
    i = colleges.index[colleges['college'] == f'{college}'].tolist()[0]
    college_data = pd.read_csv(str(os.getcwd()).replace('code', '') + '/data/college_data/college'+str(i)+'.csv')
    missing_id_rows = college_data.loc[college_data['scholar_id'] == 'NOSCHOLARPAGE']
    rows_to_plot = college_data.loc[college_data['scholar_id'] != 'NOSCHOLARPAGE']
    rows = rows_to_plot.shape[0]

    h_indexes = rows_to_plot['h-index'].sort_values()
    names = rows_to_plot['name']
    
    if(len(names)>5):
        fig_width = len(names) * 20 + 100
    else:
        fig_width= 400
    
    rows_to_plot = rows_to_plot.sort_values('h-index')
    
    desc = rows_to_plot.describe()
    
    
    #h-index
    
    h_indx_mean = float(desc.iloc[1,1])
    names = rows_to_plot['name']



    college_no_spaces = college.replace(' ','_')
    
    h_indexes = rows_to_plot['h-index']
    names = rows_to_plot['name']

    fig = px.scatter(x = names, y = h_indexes, labels = {'x':'name', 'y':'h-index'}, title = f'{college}', width = fig_width, height = 1000, range_y = [0,300], range_x = [-1,rows])
    fig.add_hline(y=h_indx_mean)
    
    fig.update_layout(title=go.layout.Title(text=f'Average h-index for {rows} professors: {int(h_indx_mean)}', font=dict(
               family="Courier New, monospace",
               size=14,
               color="#0000FF"
           )))
    
    fig.update(layout_yaxis_range = [0,220])
    
    missing_names = missing_id_rows['name']
    missing_names_text = ''
    for missing_name in missing_names:
        missing_names_text += missing_name + ', '
    
    fig.update_layout(annotations=[
       go.layout.Annotation(
            showarrow=False,
            text=f'{missing_names}',
            xanchor='right',
            x=1,
            xshift=275,
            yanchor='top',
            y=0.05,
            font=dict(
                family="Courier New, monospace",
                size=22,
                color="#0000FF"
            )
        )])
    print('h_index graph...')
    #fig.write_image(f'/Users/kevins/Documents/CSImpact/data/college_graphs/{college_no_spaces}/{college_no_spaces}_h_index.jpg' )
    #fig.write_html(f'/Users/kevins/Documents/CSImpact/data/college_graphs/{college_no_spaces}/{college_no_spaces}_h_index.jpg')
    fig.show()
    time.sleep(3)
    
    citations = rows_to_plot['citations'].sort_values()
    names = rows_to_plot['name']

    rows_to_plot = rows_to_plot.sort_values('citations')
    names = rows_to_plot['name']
    cit_mean = float(desc.iloc[1,0])


    fig = px.scatter(x = names, y = citations, labels = {'x':'name', 'y':'citations'}, title = f'{college}', width = fig_width, height = 1000, range_y = [-100,10000], range_x = [-1,rows])
    fig.add_shape(type='line',
                x0=0,
                y0=40,
                x1=8,
                y1=40,
                line=dict(color='Red',),
                xref='x',
                yref='y'
)
    
    fig.update_layout(title=go.layout.Title(text=f'Average h-index for {rows} professors: {int(cit_mean)}', font=dict(
               family="Courier New, monospace",
               size=14,
               color="#0000FF"
    )))
    
    fig.update_layout(annotations=[
       go.layout.Annotation(
            showarrow=False,
            text=f'{missing_names}',
            xanchor='right',
            x=1,
            xshift=275,
            yanchor='top',
            y=0.05,
            font=dict(
                family="Courier New, monospace",
                size=22,
                color="#0000FF"
            )
        )])
    
    print('h_index graph...')
    #fig.write_image(f'/Users/kevins/Documents/CSImpact/data/college_graphs/{college_no_spaces}_citations.jpg')
    #fig.write_html(f'/Users/kevins/Documents/CSImpact/data/college_graphs/{college_no_spaces}/{college_no_spaces}_citations.jpg')

    fig.show()
    
    

    
    
for i in range(colleges.shape[0]):
    college_no_spaces = str(colleges.iloc[i,0]).replace(' ','_')
    os.mkdir(f'/Users/kevins/Documents/CSImpact/data/college_graphs/{college_no_spaces}')
    plot(f'{colleges.iloc[i,0]}')