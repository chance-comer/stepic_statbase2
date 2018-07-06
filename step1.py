# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:38:03 2018

@author: kazantseva
"""
import pandas as pd
import scipy.stats as stats

def interdependancy(df):
  isFisher = False
  for index, row in df.iterrows():
    for j in row:
     if j < 5:
       isFisher = True
       break
  if isFisher:
    return stats.fisher_exact(df)
  else:
    return stats.chi2_contingency(df)

data = pd.DataFrame([[8, 6], [5, 7]])
print(interdependancy(data))