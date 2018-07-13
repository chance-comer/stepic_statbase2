# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:45:42 2018

@author: kazantseva
"""

import pandas as pd
import scipy.stats as st

data = pd.read_csv('s_anova_test.csv')

# True - is normal, False - not normal
def test_normal(data):
  res = {}
  for var in data:
    try:
      test = st.shapiro(data[var])
      if test[1] >= 0.05:
        res[var] = True
      else :
        res[var] = False
    except:
      res[var] = None
  return res

groups = data.groupby('y').groups.keys()

isNormal = True
isHomoVariance = True
anova = -1

d = []

for i, gr in enumerate(groups) :
  d.append(data[data['y'] == gr]['x'])
  isNormal = test_normal(d[i])  
  if isNormal == False:
    break

if isNormal:
  isHomoVariance = st.bartlett(*d).pvalue > 0.05

if isNormal and isHomoVariance:
  anova = {'ANOVA' : st.f_oneway(*d).pvalue}
else:
  anova = {'KW' : st.kruskal(*d).pvalue}

print(anova)
