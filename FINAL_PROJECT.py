'#import required libraries'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

gdp= pd.read_csv('gdp_csv.csv')
print(gdp.info())

eu = pd.read_csv('states.csv')
print(eu.info())