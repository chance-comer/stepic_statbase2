# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:31:25 2018

@author: kazantseva

"""

import pandas as pd
import numpy as np
import scipy.stats as stats

data = pd.read_csv("titanic.csv")

X = pd.DataFrame(data["Sex"], data["Pclass"])
X.index = np.arange(len(data))
