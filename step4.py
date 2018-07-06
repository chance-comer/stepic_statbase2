# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:40:40 2018

@author: Nataliya
"""

import pandas as pd
import numpy as np

data = pd.read_csv('iris.csv')

data = pd.DataFrame({'V1' : [16, 21, 18], \
                     'V2' : [17, 7, 16], \
                     'V3' : [25, 23, 27], \
                     'V4' : [20, 22, 18], \
                     'V5' : [16, 17, 19]})

means = data.mean(axis = 0)
hals_factors_count = np.ceil(len(means) / 2)

ret = {}

for index, row in data.iterrows():
    k = 0
    for col in means.keys():
        if row[col] > means[col]:
            k += 1
            if k == hals_factors_count:
                ret[index] = 'Yes'
                break
    if k < hals_factors_count:
        ret[index] = 'No'


s = pd.Series(ret, name = 'answer')
df2 = pd.DataFrame(s, index = ret.keys())

final = pd.concat([data, df2], axis = 1)

print(final['answer'].value_counts())