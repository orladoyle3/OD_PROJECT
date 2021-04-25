'#import required libraries'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

'#import dataframes'
gdp= pd.read_csv('gdp_csv.csv')

eu = pd.read_csv('states.csv')

'#change column name in eu dataframe from Country to Country Name'
eu_edit = eu.rename(columns={'Country':'Country Name'})

'#merge the dataframes on column Country Name using a left join'
gdp_eu = pd.merge(gdp, eu_edit, on='Country Name', how='left')

'#drop columns not required'
col_list = ['Council Votes', 'European Parliament Seats', 'European Free Trade Agreement', 'European Single Market', 'European Monetary Union', 'Currency', 'Currency Code', 'Language','GDP ($, millions)','GDP per capita ($, millions)']
gdp_eu = gdp_eu.drop(col_list, axis=1)

'#replace missing values in dataset'
gdp_eu = gdp_eu.fillna(0)

'# group data by European Union - Member'
gdp_eu1 = gdp_eu.groupby('European Union')['GDP (€, millions)'].plot(legend=True)

gdp_eu['Per Capita'] = gdp_eu['GDP (€, millions)'] / gdp_eu['Population']

