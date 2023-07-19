# `pm25-cum.py` displays the overall cumulative exposure distribution for all
# HOLC mapped areas, separated by HOLC grade. Plot also includes a line
# displaying the population-weighted mean exposure for CUAs for comparison.
# This is a rough sketch based off of Figure 4(b) from the study's supporting
# information.
from utils import init
import matplotlib.pyplot as plt
import numpy as np

# Initialize DataFrame.
df = init()
pm25_A = []
pm25_B = []
pm25_C = []
pm25_D = []
pm25_CUA = []
# Percentiles to plot.
percentiles = range(0, 100)

# See `no2-cum.py` for notes on this method of sorting data and why it appears
# different from that in the study.
for i in df.index:
   pm25_CUA += (round(df['Total'][i] * df['PHOLC'][i]) * [df['PM25'][i]])
   if df['Grade'][i] == 'A':
      pm25_A += (round(df['Total'][i] * df['PHOLC'][i]) * [df['PM25'][i]])
   if df['Grade'][i] == 'B':
      pm25_B += (round(df['Total'][i] * df['PHOLC'][i]) * [df['PM25'][i]])
   if df['Grade'][i] == 'C':
      pm25_C += (round(df['Total'][i] * df['PHOLC'][i]) * [df['PM25'][i]])
   if df['Grade'][i] == 'D':
      pm25_D += (round(df['Total'][i] * df['PHOLC'][i]) * [df['PM25'][i]])

lst_A = np.array(pm25_A)
lst_B = np.array(pm25_B)
lst_C = np.array(pm25_C)
lst_D = np.array(pm25_D)
lst_CUA = np.array(pm25_CUA)

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
plt.ylabel("PM2.5")
ax.set_ylim(0, 16)
ax.legend()

plt.savefig('pm25-cumulative-perc.png', dpi = 300)
