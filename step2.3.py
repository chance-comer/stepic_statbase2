# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:29:08 2018

@author: kazantseva
"""

import pandas as pd
import statsmodels.api as sm
import statsmodels as sms
import numpy as np
from statsmodels.formula.api import ols

data = pd.read_csv("test_data_passangers.csv")
predict_data = pd.read_csv("predict_passangers.csv")

data['is_prohibited'] = np.where(data['is_prohibited'] == 'Yes', 1, 0)
data['type'] = data['type'].astype('category')

predict_data['type'] = predict_data['type'].astype('category')


def define_coef(test_data, predict_data):
  m = sm.formula.glm('is_prohibited ~ C(type) + weight + width + length', data=test_data, family = sm.families.Binomial()).fit()
  #prediction = pd.DataFrame(columns = ['prob', 'name'])
  prediction = m.predict(predict_data)
  pred_2 = pd.DataFrame({ 'x' : prediction })
  pred_2['name'] = predict_data['passangers']
  pred_2['x'] = pred_2.apply(lambda t: np.exp(t['x']) / (1 + np.exp(t['x'])), axis = 1)
  maxprob = pred_2['x'].max()
  print(pred_2.loc[pred_2['x'] == maxprob]['name'])
  return { 'm': m, 'p': pred_2 }

coef = define_coef(data, predict_data)
print(coef['m'].summary())
print(coef['p'])
#sm.stats.anova_lm(coef)