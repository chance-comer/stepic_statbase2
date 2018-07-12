# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:59:50 2018

@author: kazantseva
"""
import pandas as pd

def centered(df, var_list):
  df_1 = pd.DataFrame()
  for var in var_list:
    mean = df[var].mean()
    df_1[var] = df.apply(lambda x: x[var] - mean, axis = 1)
  return df_1

df = pd.DataFrame({'x' : [5]})
  
c = centered(df, ['x'])