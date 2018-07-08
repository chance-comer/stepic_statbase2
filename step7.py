# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 19:19:05 2018

@author: Nataliya
"""
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

data = pd.read_csv('diamonds.csv')

colorgroup1 = data.groupby(['color', 'cut'])['color'].count()
colorgroup2 = data.groupby(['cut', 'color'])['color'].count()

bar_width = 0.15

x_color = colorgroup1.index.levels[0]
x_cut = colorgroup1.index.levels[1]

x_index = np.arange(len(x_color))

plt.figure(figsize=(10, 5))
#fig, ax = plt.subplots()


#plt.bar(x_index, colorgroup2['Fair'], bar_width)
#plt.bar(x_index + bar_width, colorgroup2['Very Good'], bar_width)

d = colorgroup1.to_frame().unstack().transpose()

left = 0

#plt.bar(x_index + left, next(d.iterrows())[1], bar_width)

for index, item in d.iterrows():
    plt.bar(x_index + left, item, bar_width, label = index[1])
    left += bar_width

plt.xlabel('color')
plt.ylabel('count')
plt.xticks(x_index + bar_width * len(x_cut) / 2, x_color)
plt.legend()
plt.tight_layout()