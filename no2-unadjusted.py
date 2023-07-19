# `no2-unadjusted.py` creates a plot displaying the unadjusted national
# population-weighted distribution of NO2 levels within HOLC-mapped areas at
# the census block level as specified in Figure 1(a).
from utils import init
import matplotlib.pyplot as plt
import numpy as np

# Initialize DataFrame from imported function.
df = init()

# Lists to store data to be used to generate plots: NO2 levels by HOLC grade,
# and by race/ethnicity.
no2_A         = []
no2_B         = []
no2_C         = []
no2_D         = []
no2_white     = []
no2_other     = []
no2_black     = []
no2_asian     = []
no2_hispanic  = []

# Iterate through DataFrame and add appropriate numbers to corresponding lists.
# Notice that the population figure is always multiplied by the `PHOLC` of each
# entry, as that denotes the proportion of the number of people living in the
# marked HOLC grade.
for i in df.index:
   if df['Grade'][i] == 'A':
      no2_A += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'B':
      no2_B += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'C':
      no2_C += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'D':
      no2_D += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   # Per the study: This plot displays statistics for HOLC-mapped areas. If you
   # do not filter by grade and only by ethnicity here, you are going to get
   # some very different numbers.
   if df['Grade'][i] != 'N':
      no2_white += (round(df['PHOLC'][i] * df['White'][i]) * [df['NO2'][i]])
      no2_other += (round(df['PHOLC'][i] * df['Other'][i]) * [df['NO2'][i]])
      no2_black += (round(df['PHOLC'][i] * df['Black'][i]) * [df['NO2'][i]])
      no2_asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [df['NO2'][i]])
      no2_hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [df['NO2'][i]])

# Organize data into list to feed into plot generator.
data = [no2_A, no2_B, no2_C, no2_D, no2_white, no2_other, no2_black, no2_asian, no2_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

# Generate plot, customize appearance, and set title.
fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Unadjusted: National Aggregation')

# Set minimum and maximum y-values, do not let the software try to do it
# automatically.
ax.set_ylim(0, 25)
for median in plot['medians']:
   median.set_color('black')

# You may set the color of each shape in this boxplot yourself.
colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
          'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

# Save figure.
plt.savefig('no2-unadjusted.png', dpi = 300)
