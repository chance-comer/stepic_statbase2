# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:47:55 2018

@author: kazantseva
"""

from patsy import dmatrices
import pandas as pd
from sklearn.linear_model import LogisticRegression
import statsmodels.discrete.discrete_model as sm

# read in the data & create matrices
df = pd.read_csv("titanic2.csv")
y, X = dmatrices('Survived ~ 1', df, return_type = 'dataframe')

# sklearn output
model = LogisticRegression(fit_intercept = False, C = 1e9)
mdl = model.fit(X, y)
model.coef_

# sm
logit = sm.Logit(y, X)
m = logit.fit()