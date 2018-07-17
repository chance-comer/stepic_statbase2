# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:56:07 2018

@author: kazantseva
"""

import pandas as pd
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster
import scipy.stats as st
import numpy as np

def get_clasters(data, clcount) :
  Z = linkage(data)
  clusters = fcluster(Z, clcount, criterion='maxclust')
  data['clnum'] = clusters

def pval(data, clcount) :
  get_clasters(data, clcount)
  for col in data:
    if col == 'clnum':
      continue
    #print(col)
    factor_in_cluster = []
    for i in np.arange(1, clcount + 1):
      factor_in_cluster.append(data[data['clnum'] == i][col])
    anova = st.f_oneway(*factor_in_cluster)
    #print(factor_in_cluster)
    res[col] = anova.pvalue
    
def select_significant(pset):
  return [t for t in pset.keys() if pset[t] < 0.05]
    
data = pd.read_csv('cluster_1.csv')
res = {}

pval(data, 2)
print(select_significant(res))