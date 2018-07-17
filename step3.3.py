# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 12:26:56 2018

@author: kazantseva
"""

from sklearn.decomposition import PCA, IncrementalPCA,  KernelPCA
import pandas as pd
from sklearn.preprocessing import scale
import numpy as np

data = pd.read_csv('pca_test.csv')
pca =  PCA(n_components=2, whiten = False)

X1=pca.fit_transform(data)

