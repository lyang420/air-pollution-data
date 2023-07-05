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

# The population-weighted distribution of NO2 concentrations by HOLC grade
# appears identical to that shown in Figure 1(a). However, similar approach
# to plot distribution by race/ethnicity yields different numbers.
for i in df.index:
   if df['Grade'][i] == 'A':
      no2_A += (df['Total'][i] * [df['NO2'][i]])
   if df['Grade'][i] == 'B':
      no2_B += (df['Total'][i] * [df['NO2'][i]])
   if df['Grade'][i] == 'C':
      no2_C += (df['Total'][i] * [df['NO2'][i]])
   if df['Grade'][i] == 'D':
      no2_D += (df['Total'][i] * [df['NO2'][i]])
   # See here: Population-weighted distribution of NO2 levels generated using
   # this approach yields numbers that differ from the figures displayed in the
   # study.
   if (df['White'][i] > 0):
      no2_white += (df['White'][i] * [df['NO2'][i]])
   if (df['Other'][i] > 0):
      no2_other += (df['Other'][i] * [df['NO2'][i]])
   if (df['Black'][i] > 0):
      no2_black += (df['Black'][i] * [df['NO2'][i]])
   if (df['Asian'][i] > 0):
      no2_asian += (df['Asian'][i] * [df['NO2'][i]])
   if (df['Hispanic'][i] > 0):
      no2_hispanic += (df['Hispanic'][i] * [df['NO2'][i]])

data = [no2_A, no2_B, no2_C, no2_D, no2_white, no2_other, no2_black, no2_asian, no2_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

fig1, ax1 = plt.subplots(nrows = 1, ncols = 1)
no2_plot = ax1.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax1.set_title('Unadjusted: national aggregation')

ax1.set_ylim(0, 25)
for median in no2_plot['medians']:
   median.set_color('black')

colors = ['forestgreen', 'cornflowerblue', 'goldenrod', 'firebrick', 'palevioletred', 'darkkhaki', 'plum', 'slateblue', 'mediumseagreen']
for patch, color in zip(no2_plot['boxes'], colors):
   patch.set_facecolor(color)

plt.savefig('no2-unadjusted.png', dpi = 300)

# The following function calculates a specific weighted percentile given a list
# of values and corresponding weights. Provided in R by lead author Haley Lane,
# translated to Python.
#
# This is an alternative, more efficient approach to the above problem; current
# analysis yields the same numbers.
def wtd_pct(x, w, p):
   # x is value
   # w is weight
   # p is percentile
   w = w[np.argsort(x)]
   x = x[np.argsort(x)]

   # remove NAs
   t = (~np.isnan(w)) & (w > 0) & (~np.isnan(x))
   x = x[t]
   w = w[t]

   w = np.cumsum(w) / np.sum(w)

   r = x[np.max(np.arange(1, len(x) + 1) * (w <= p))]
   if np.isnan(r):
      r = x[np.min(np.arrange(1, len(x) + 1) * (w >= p))]
   
   return r
