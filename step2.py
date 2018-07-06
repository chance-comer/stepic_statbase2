# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:21:52 2018

@author: kazantseva
"""

import pandas as pd 
import scipy.stats as stats
import numpy as np

data = pd.read_csv('step2_genAGCT.csv')
#data = data.transpose()

#print(data)

#data = data['V1'].value_counts()
#data = pd.crosstab(data['V1'], 'count')
#data = data.groupby(['V1']).count()

#f_lvls = data.nunique()

#print(f_lvls)

#data = data.groupby('V1')

min_p = 0
seq = ''

def most_significant(data):
  for col in data:
    obs = data[col]
    freqt = obs.value_counts()
    #print(freqt)
    chi = stats.chisquare(freqt)
    print(chi)
    

most_significant(data)
print('seq = ' + seq)