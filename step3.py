# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:22:51 2018

@author: kazantseva
"""
import pandas as pd

data = pd.read_csv('iris.csv')

means = data.mean(axis = 0)

r = [ row[col] > means[col] for index, row in data.iterrows() for col in means.keys() ]

#data['new_factor'] = ['No' for i in data.iterrows()]

ret = {}

for index, row in data.iterrows():
    k = 0
    for col in means.keys():
        if row[col] > means[col]:
            k += 1
            if k == 3:
                ret[index] = 'Yes'
                break
    if k < 3:
        ret[index] = 'No'


s = pd.Series(ret, name = 'answer')
df2 = pd.DataFrame(s, index = ret.keys())

final = pd.concat([data, df2], axis = 1)

print(final['answer'].value_counts())