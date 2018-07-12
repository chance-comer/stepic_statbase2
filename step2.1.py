# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:31:25 2018

@author: kazantseva

"""

"""
IMPORTANT!!!!!!!!!!!!!!!!!!!

sm.Logit requires dummy data
sm.GLM requires dummy data
sm.formula.glm require raw data but with 'category' dtype of columns

Also sm.Logit and sm.GLM require only 0 and 1 as endog variable
and dont know why 0 is success (or may be I mistake)
and sm.formula.glm take greatest value of y as success to odds formula p / (1 - p)
so I change for this task 2 to 0
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv("test_data_01.csv")

data['x'] = data['x'].astype('category')

#data['y'] = np.where(data['y'] == 1, 0, data['y'])
data['y'] = np.where(data['y'] == 2, 0, data['y'])

data['y'] = data['y'].astype('category')

model_data = pd.DataFrame()

cat_vars = ['x']

for var in cat_vars:
  cat_list = pd.get_dummies(data[var], prefix = var)
  model_data[cat_list.columns] = cat_list  

model_data['const'] = [1 for i in data.iterrows()]
model_data.drop(['x_1'], axis=1, inplace=True)

#m = sm.formula.logit('y ~ C(x)', data=data, family=sm.families.Binomial()).fit()

#m = sm.GLM(data['y'], model_data, family=sm.families.Binomial()).fit()

m = sm.formula.glm('y ~ C(x)', data=data, family = sm.families.Binomial()).fit()
print(m.summary())

#logit = sm.Logit(data['y'], model_data[['const', 'x_2', 'x_3']])
#m = logit.fit()
#print(m.summary())

