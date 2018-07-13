# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:40:19 2018

@author: kazantseva
"""

import pandas as pd
import scipy.stats as st

data = pd.read_csv('iris.csv')

for var in data:
  try:
    res = st.shapiro(data[var])
    print(var + ' p-value ' + str(res[1]))
  except:
    print(var + ' not numeric')