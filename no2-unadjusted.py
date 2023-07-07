# This script aims to create a plot displaying the unadjusted national
# population-weighted distributions of NO2 levels within HOLC-mapped areas at
# the census block level as seen in Figure 1(a).
from createdf import init

import matplotlib.pyplot as plt
import numpy as np

df = init()

no2_A         = []
no2_B         = []
no2_C         = []
no2_D         = []
no2_white     = []
no2_other     = []
no2_black     = []
no2_asian     = []
no2_hispanic  = []

for i in df.index:
   if df['Grade'][i] == 'A':
      no2_A += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'B':
      no2_B += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'C':
      no2_C += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'D':
      no2_D += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] != 'N':
      no2_white += (round(df['PHOLC'][i] * df['White'][i]) * [df['NO2'][i]])
      no2_other += (round(df['PHOLC'][i] * df['Other'][i]) * [df['NO2'][i]])
      no2_black += (round(df['PHOLC'][i] * df['Black'][i]) * [df['NO2'][i]])
      no2_asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [df['NO2'][i]])
      no2_hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [df['NO2'][i]])

data = [no2_A, no2_B, no2_C, no2_D, no2_white, no2_other, no2_black, no2_asian, no2_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Unadjusted: National Aggregation')

ax.set_ylim(0, 25)
for median in plot['medians']:
   median.set_color('black')

colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
          'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

plt.savefig('no2-unadjusted.png', dpi = 300)
