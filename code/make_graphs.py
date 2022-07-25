import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

colleges = pd.read_csv(os.getcwd().replace('code/','')+'/data/colleges.csv')
data = pd.read_csv(os.getcwd().replace('code/','')+'/data/cleaned_prof_data_v4.csv')


college_data = pd.DataFrame()

os.mkdir(os.getcwd().replace('code/','')+'/data/college_graphs')
#create folders
for i in range(colleges.shape[0]):
    college_no_spaces = pd.read_csv(os.getcwd().replace('code/','')+f'/data/colleges.csv').iloc[i,0].replace(' ','_').replace('/', '_')
    os.mkdir(os.getcwd().replace('code/','')+f'/data/college_graphs/{college_no_spaces}')


def plot_college(college):
    #remove spaces from college names
    college_no_spaces = college.replace(' ','_').replace('/', '_')
    
    #Get the index of the college
    i = colleges.index[colleges['college'] == f'{college}'].tolist()[0]
    
    #get corresponding csv file
    college_data = pd.read_csv('/Users/kevins/Documents/CSImpact/data/college_data/college'+str(i)+'.csv')
    
    #get rows with missing data
    missing_id_rows = college_data.loc[(pd.isna(college_data['h-index'])) & (pd.isna(college_data['citations']))]
    missing_profs = missing_id_rows['name']
    #get rows with good data
    rows_to_plot = college_data.loc[(~(pd.isna(college_data['h-index'])) & ~(pd.isna(college_data['citations'])))]
    
    #number of professors/rows
    rows = college_data.shape[0]
    
    
    
    
    # turn missing data into y value of 1 to put at the bottom of graph 
    missing_h_indexes = []
    missing_citations = []
    
    for p in missing_profs:
        missing_h_indexes.append(1)
        missing_citations.append(1)

    
    #set row width based on amount of data
    if(rows>5):
        fig_width = rows * 20 + 100
    else:
        fig_width= 400
        
    #sort data smallest to largest
    rows_to_plot = rows_to_plot.sort_values('h-index')
    
    #get stats of data (mean, etc.)
    desc = rows_to_plot.describe()
    
    
    
    
    #PLOTTING H-INDEX
    
    
    
    
    #get mean from description
    h_indx_mean = round(float(desc.iloc[1,1]),1)

    
    #get good data, names
    h_indexes = rows_to_plot['h-index']
    names = rows_to_plot['name']
    
    #plot bad data first at the bottom
    fig = px.scatter(x = missing_profs, y = missing_h_indexes, labels = {'x':'name', 'y':'h-index'},title = f'{college}', width = fig_width, height = 1000, range_y = [1,320], range_x = [-1,rows],color_discrete_sequence=['red'], log_y = True)
    fig.update_layout(
    yaxis = dict(
        #log scale
        tickmode = 'array',
        tickvals = [0,5,10, 20,40,80,160, 320]
    )
)
    #add labels to bad data saying 'NO DATA' when you hover over the  points
    fig.update_traces(hovertemplate='NO DATA')
    
    # the annotation for the average line disappears for some reason so get the x-value to add it manually
    if(pd.isna(missing_id_rows.iloc[0,0])):
        annotation_x = rows_to_plot.iloc[0,0]
    else:
        annotation_x = missing_id_rows.iloc[0,0]
    
    # plot average line
    if(not pd.isna(h_indx_mean)):
        fig.add_hline(y=h_indx_mean, line_color = 'black',annotation_text=f'Average = {h_indx_mean}', annotation_position = "bottom")
        fig.add_trace(go.Scatter(
            x=[missing_id_rows.iloc[0,0]],
            y=[h_indx_mean],
            mode="lines+text",
            text=[f'Average = {h_indx_mean}'],
            textposition="top right"
        ))
    else:
        h_indx_mean = 0
    
    # add subtitle displaying average
    fig.update_layout(title = go.layout.Title(text = f'{college} <br><sup>Average h-index for {rows_to_plot.shape[0]} professors: {h_indx_mean}</sup>', xref = 'paper', x = 0), font=dict(
               family="Courier New, monospace",
               size=10,
               color="#000000"
           )
        )
    
    # plot good data
    fig.add_trace(
    go.Scatter(
        x=names,
        y= h_indexes,
        mode ='markers', name = '',marker = dict( color = 'black'))
    )
    
    # hide the legend
    fig.update_layout(showlegend=False)
    
    #fig.show()
    fig.write_image(f'/Users/kevins/Documents/CSImpact/data/college_graphs/{college_no_spaces}/{college_no_spaces}_h_index.png')

    
    # PLOTTING CITATIONS
    #basically the same logic as plotting h-index
    
    cit_mean = round(float(desc.iloc[1,0]),1)

    
    rows_to_plot = rows_to_plot.sort_values('citations')
    names = rows_to_plot['name']
    
    citations = rows_to_plot['citations']

        
    fig = px.scatter(x = missing_profs, y = missing_citations, labels = {'x':'name', 'y':'citations'},title = f'{college}', width = fig_width, height = 1000, range_y = [1,325000], range_x = [-1,rows],color_discrete_sequence=['red'],log_y = True)
    fig.update_layout(
    yaxis = dict(
        tickmode = 'array',
        tickvals = [0,33,325, 3250,32500,325000]
    )
)
    
    fig.update_traces(hovertemplate='NO DATA')

    
    if(pd.isna(missing_id_rows.iloc[0,0])):
        annotation_x = rows_to_plot.iloc[0,0]
    else:
        annotation_x = missing_id_rows.iloc[0,0]
        
    if(not pd.isna(cit_mean)):
        fig.add_hline(y=cit_mean, line_color = 'black',annotation_text=f'Average = {cit_mean} citations', annotation_position = "top left")
        fig.add_trace(go.Scatter(
            x=[annotation_x],
            y=[cit_mean],
            mode="lines+text",
            text=[f'Average = {cit_mean}'],
            textposition="top right"
        ))
    else:
        cit_mean = 0
    fig.update_layout(title = go.layout.Title(text = f'{college} <br><sup>Average citations for {rows_to_plot.shape[0]} professors: {cit_mean}</sup>', xref = 'paper', x = 0), font=dict(
               family="Courier New, monospace",
               size=10,
               color="#000000"
           )
        )

    
    fig.add_trace(
    go.Scatter(
        x=names,
        y= citations,
        mode ='markers', name = '',marker = dict( color = 'black'))
    )
    fig.update_layout(showlegend=False)
    
    #fig.show()
    fig.write_image(f'/Users/kevins/Documents/CSImpact/data/college_graphs/{college_no_spaces}/{college_no_spaces}_citations.png')

#plot all colleges
for i in range(colleges.shape[0]):
    plot_college(f'{colleges.iloc[i,0]}')