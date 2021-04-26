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

'# Select years 2010 to 2016, all EU members states and candidates plus USA'
gdp_eu1 = gdp_eu[(gdp_eu['Year'] >= 2010) & (gdp_eu['European Union'] == 'Member') | (gdp_eu["Country Code"] == "USA")]


'#group by country and calculate mean gdp from 2010 to 2016'
gdp_eu1["eu_average"] = gdp_eu1.groupby('Country Name')['Value'].mean() /1e9

fig, ax = plt.subplots()
ax.bar(gdp_eu1['Country Name'], gdp_eu1["Value"])
ax.set_xticklabels(gdp_eu1['Country Name'], rotation=45)
ax.set_ylabel("€'000m")
plt.show()
