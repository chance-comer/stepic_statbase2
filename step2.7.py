# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:05:03 2018

@author: kazantseva
"""

import pandas as pd
import scipy.stats as st

data = pd.read_csv('test_for_norm.csv')

ct = pd.crosstab(index = data['y'], columns = data['z'], values = data['x'], 
                 aggfunc = lambda x : st.shapiro(x)[1])