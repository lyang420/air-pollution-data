# `pm25-unadjusted.py` creates a plot displaying the unadjusted national
# population-weighted distribution of PM2.5 levels within HOLC-mapped areas at
# the census block level as specified in Figure 1(b).
from createdf import init
import matplotlib.pyplot as plt
import numpy as np

# Initialize DataFrame from imported function.
df = init()

# Lists to store data to be used to generate plots: PM2.5 levels by HOLC grade,
# and by race/ethnicity.
pm25_A         = []
pm25_B         = []
pm25_C         = []
pm25_D         = []
pm25_white     = []
pm25_other     = []
pm25_black     = []
pm25_asian     = []
pm25_hispanic  = []

# Iterate through DataFrame and add appropriate numbers to corresponding lists.
# Notice that the population figure is always multiplied by the `PHOLC` of each
# entry, as that denotes the proportion of the number of people living in the
# marked HOLC grade.
for i in df.index:
   if df['Grade'][i] == 'A':
      pm25_A += (round(df['PHOLC'][i] * df['Total'][i]) * [df['PM25'][i]])
   if df['Grade'][i] == 'B':
      pm25_B += (round(df['PHOLC'][i] * df['Total'][i]) * [df['PM25'][i]])
   if df['Grade'][i] == 'C':
      pm25_C += (round(df['PHOLC'][i] * df['Total'][i]) * [df['PM25'][i]])
   if df['Grade'][i] == 'D':
      pm25_D += (round(df['PHOLC'][i] * df['Total'][i]) * [df['PM25'][i]])
   # Per the study: This plot displays statistics for HOLC-mapped areas. If you
   # do not filter by grade and only by ethnicity here, you are going to get
   # some very different numbers.
   if df['Grade'][i] != 'N':
      pm25_white += (round(df['PHOLC'][i] * df['White'][i]) * [df['PM25'][i]])
      pm25_other += (round(df['PHOLC'][i] * df['Other'][i]) * [df['PM25'][i]])
      pm25_black += (round(df['PHOLC'][i] * df['Black'][i]) * [df['PM25'][i]])
      pm25_asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [df['PM25'][i]])
      pm25_hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [df['PM25'][i]])

# Organize data into list to feed into plot generator.
data = [pm25_A, pm25_B, pm25_C, pm25_D, pm25_white, pm25_other, pm25_black, pm25_asian, pm25_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

# Generate plot, customize appearance, and set title.
fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Unadjusted: National Aggregation')

# Set minimum and maximum y-values, do not let the software try to do it
# automatically.
ax.set_ylim(0, 15)
for median in plot['medians']:
   median.set_color('black')

# You may set the color of each shape in this boxplot yourself.
colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
          'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

# Save figure.
plt.savefig('pm25-unadjusted.png', dpi = 300)
