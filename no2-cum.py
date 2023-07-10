# `no2-cum.py` displays the overall cumulative exposure distribution for all
# HOLC mapped areas, separated by HOLC grade. Plot also includes a line
# displaying the population-weighted mean exposure for CUAs for comparison.
# This is a rough sketch based off of Figure 4(a) from the study's supporting
# information.
from createdf import init
import matplotlib.pyplot as plt
import numpy as np

# Initialize DataFrame.
df = init()
no2_A = []
no2_B = []
no2_C = []
no2_D = []
no2_CUA = []
# Percentiles to plot.
percentiles = range(0, 100)

# Method of collecting data very similar to previous plots. Very, very
# interesting thing to note is that even without rounding, the maximum NO2
# data point plotted is just under the 30 ppb mark, but analysis of the
# DataFrame says the highest point is in fact over 35 ppb. This is also
# reflected in the figure in the study. I will say that from the way the plot
# in the figure is drawn, it looks like a few data points extend well past the
# 99.99th percentile mark, and matplotlib seems to be making a lot of
# compromises as well (or maybe I don't know it well enough yet), as this used
# to be a line chart but I opted for a scatterplot instead.
for i in df.index:
   no2_CUA += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'A':
      no2_A += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'B':
      no2_B += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'C':
      no2_C += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])
   if df['Grade'][i] == 'D':
      no2_D += (round(df['Total'][i] * df['PHOLC'][i]) * [df['NO2'][i]])

lst_A = np.array(no2_A)
lst_B = np.array(no2_B)
lst_C = np.array(no2_C)
lst_D = np.array(no2_D)
lst_CUA = np.array(no2_CUA)

perc_A = np.percentile(lst_A, percentiles)
perc_B = np.percentile(lst_B, percentiles)
perc_C = np.percentile(lst_C, percentiles)
perc_D = np.percentile(lst_D, percentiles)
perc_CUA = np.percentile(lst_CUA, percentiles)

fig, ax = plt.subplots()
line1 = plt.scatter(percentiles, perc_A, s = 10, label = 'A')
line2 = plt.scatter(percentiles, perc_B, s = 10, label = 'B')
line3 = plt.scatter(percentiles, perc_C, s = 10, label = 'C')
line4 = plt.scatter(percentiles, perc_D, s = 10, label = 'D')
line5 = plt.scatter(percentiles, perc_CUA, s = 10, label = 'CUA')
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.xlabel("Population Percentile")
plt.ylabel("NO2")
ax.set_ylim(0, 35)
ax.legend()

plt.savefig('no2-cumulative-perc.png', dpi = 300)
