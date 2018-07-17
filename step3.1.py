# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:33:42 2018

@author: kazantseva
"""

import scipy.spatial as scis
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy  import fcluster


data = pd.read_csv('test_data_hclust.csv')

dist = pd.DataFrame(scis.distance_matrix(data.values, data.values), index = data.index,
                    columns = data.index)

Z = linkage(data, 'ward')

c, coph_dists = cophenet(Z, pdist(data))

dendrogram(Z,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=5,  # show only the last p merged clusters
    show_leaf_counts=False,  # otherwise numbers in brackets are counts
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True ) # to get a distribution impression in truncated branches)

k = 3
clusters = fcluster(Z, k, criterion='maxclust')

data['clnum'] = clusters