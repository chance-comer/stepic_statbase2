
import pandas as pd
import scipy.stats as stats

data = pd.read_csv('test_drugs.csv')

'''
data = pd.DataFrame(data = [[2, 1, 1, 3, 3, 3, 3, 2, 3, 2, 2, 3, 1, 3, 1, \
                             2, 2, 2, 3, 1, 3, 1, 3, 3, 2, 1, 2, 2, 2, 1, \
                             3, 3, 1, 1, 3, 2, 3, 2, 2, 2, 1, 1, 2, 1, 3, 1, \
                             2, 3, 3, 1, 2, 1, 2, 3, 2, 2, 2, 2, 2, 3, 3, 3, \
                             2, 2, 3, 1, 2, 1, 1, 2, 1, 3, 2, 2, 2, 1, 1, 2, \
                             2, 2, 2, 2, 1, 3, 2, 3, 2, 2, 2, 3, 2, 2, 1, 2, \
                             2, 2, 1, 3, 1, 1, 2, 2, 1, 3, 1, 2, 3, 1],\
[2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, \
 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, \
 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, \
 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, \
 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, \
 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, \
 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1]], index = ['Drugs','Result'])

data = data.transpose()
'''

freqt = pd.crosstab(data['Drugs'], data['Result'])

expected = pd.DataFrame(data = stats.contingency.expected_freq(freqt), \
                        index = ['drug_1', 'drug_2', 'drug_3'], \
                        columns = ['negative',  'positive'])

chi = pd.DataFrame()

for f_index, f_row in freqt.iterrows():
    for f_col in f_row.index:
        chi.at[f_index, f_col] = stats.chisquare(freqt[f_col][f_index], expected[f_col][f_index]).statistic ** 0.5

