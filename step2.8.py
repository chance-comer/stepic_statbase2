# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:23:24 2018

@author: kazantseva
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from random import randint


colors = []

data = pd.read_csv('iris.csv')

groups = np.unique(data['species'])
x_index = np.arange(len(data))

for spec in groups :
  gr = data[data['species'] == spec]
  p1=sns.kdeplot(gr['sepal_length'], shade=True, color='#%06X' % randint(0, 0xFFFFFF))




  