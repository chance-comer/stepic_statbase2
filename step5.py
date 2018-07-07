# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:50:56 2018

@author: Nataliya
"""

'''import pandas as pd
import numpy as np
import statistics as stats'''

def stat_mode(array):
    most = max(map(array.count, array))
    return set(filter(lambda x: array.count(x) == most, array))

print(stat_mode([1, 1, 1, 2, 3, 3, 3, 4, 5]))