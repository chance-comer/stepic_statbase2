# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:22:51 2018

@author: kazantseva
"""

import pandas as pd

data = pd.read_csv('iris.csv')

means = data.mean(axis = 0)

i = [index for index in means]
print(i)