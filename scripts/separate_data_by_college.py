import pandas as pd
import os

professors = pd.read_csv(os.getcwd().replace(
    'code', '') + '/data/cleaned_prof_data_v7.csv')
for i, g in professors.groupby('affiliation'):
    g.to_csv("data/college_data_new/" +
             str(g['affiliation'].unique()[0]).replace("/", "_") + ".csv", index=False)
