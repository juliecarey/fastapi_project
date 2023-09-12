#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:47:23 2023

@author: juliecarey
"""
# import relevant packages
from fastapi import FastAPI
import pandas as pd
import json
import statistics
import sqlite3
from statistics import StatisticsError

from tqdm import tqdm, trange
import time
#%%
# import data
name_data = pd.read_csv('Documents/Development/api_project/AgeDataset-V1.csv')

#%%
# get rid of any na first names
real_name_data = name_data[name_data['Name'].notna() & name_data['Country'].notna() & name_data['Occupation'].notna() & name_data['Age of death'].notna()]

#%%

# add column for first name
name = real_name_data.Name
first_name = []
for i in name:
    split_name = i.split(' ')
    first_name.append(split_name[0])
    
#%%

# run statistics on average age of death, 

real_name_data['First Name'] = first_name
uniq_name = list(real_name_data['First Name'].unique())

#%%

avg_age = list(real_name_data.groupby(['First Name'])['Age of death'].mean())
freq_country = list(real_name_data.groupby(['First Name'])['Country'].agg(pd.Series.mode))
freq_occupation = list(real_name_data.groupby(['First Name'])['Occupation'].agg(pd.Series.mode))

#%%

name_stats = pd.DataFrame({"name": uniq_name, "age": avg_age, "country": freq_country, "occupation": freq_occupation})

#%%

conn = sqlite3.connect('Documents/Development/api_project/name.db')
name_stats.to_sql('name_stats', conn, index=True, if_exists='replace')
conn.commit()
#%%





#%%
# #x = real_name_data['First Name'].unique()
# app = FastAPI()
# for j in real_name_data['First Name'].unique():
#     uniq_name = real_name_data[real_name_data['First Name'] == j]
#     avg_age = statistics.mean(uniq_name['Age of death'])
#     c = statistics.mode(uniq_name['Country'].dropna())
#     freq_occupation = statistics.mode(uniq_name['Occupation'].dropna())
#     @app.get('/' + j)
#     async def name_info():
#         return {'First Name': j, 'Avg of Death': avg_age, 'Most Common Country': freq_occupation, 'Most Common Occupation': freq_occupation}
    
    
    
    
    
    
    
    

# #%%
# chosen_name = 'George'
# app = FastAPI()
# @app.get('/' + chosen_name)
# async def get_random():
#     return{'number': 5, 'limit': 100}


# #%%

# #a_list = statistics.mode(real_name_data[real_name_data['First Name'] == 'Julie']['Country'].dropna())
# #print(statistics.mode(a_list.dropna()))