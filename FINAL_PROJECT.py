'#import required libraries'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'#import dataframes'
gdp= pd.read_csv('gdp_csv.csv')

eu = pd.read_csv('states.csv')

'#change column name in eu dataframe from Country to Country Name'
eu_edit = eu.rename(columns={'Country':'Country Name'})

'#merge the dataframes on column Country Name using a left join'
gdp_eu = pd.merge(gdp, eu_edit, on='Country Name', how='left')

'#drop columns not required'
col_list = ['Council Votes', 'European Parliament Seats', 'European Free Trade Agreement', 'European Single Market', 'European Monetary Union', 'Currency', 'Currency Code', 'Language','GDP (€, millions)','GDP ($, millions)','GDP per capita ($, millions)']
gdp_eu = gdp_eu.drop(col_list, axis=1)

'#replace missing values in dataset'
gdp_eu = gdp_eu.fillna(0)

'# Select all EU members states and candidates plus USA'
gdp_eu = gdp_eu[(gdp_eu['European Union'] !=0) | ((gdp_eu["Country Code"] == "USA"))]

'#calculate gdp per head of population for each EU country'
us_pop = 323100000
gdp_eu["Population"] = gdp_eu["Population"].replace(0,323100000)
gdp_eu["Per Capita"] = round((gdp_eu['Value'] / gdp_eu['Population']),2)

'# create two datasets for the years 2006 and 2016'
gdp06 = gdp_eu[(gdp_eu["Year"] == 2006)]
gdp06 = gdp06.sort_values(["Per Capita", "Country Name"], ascending=(True, False))
gdp16 = gdp_eu[(gdp_eu["Year"] == 2016)]
gdp16 = gdp16.sort_values(["Per Capita", "Country Name"], ascending=(True,False))

'#Plot 2010 and 2016 per Capita to show increase or decrease in value over a 10 year period'
fig, ax=plt.subplots()
ax.plot(gdp06["Country Name"], gdp06["Per Capita"], marker = "o", linewidth=0.5)
ax.plot(gdp16["Country Name"], gdp16["Per Capita"], marker = "o", linewidth=0.5)
ax.set_xticklabels(gdp06["Country Name"], rotation=80)
ax.set_yticklabels(gdp06["Per Capita"])
ax.set(title="2010 GDP vs 2016 GDP Per Country", xlabel="Country", ylabel="Per Capita", ylim=[0,50000])
ax.margins(x=0, y=0.1)
fig.tight_layout()
ax.legend([2006, 2016])
plt.show()


gdp_eu1 = gdp_eu.groupby('European Union')['Value'].sum() /1e9
gdp_eu1.to_csv('edit20.csv')
gdp_eu1.hist()
plt.show()