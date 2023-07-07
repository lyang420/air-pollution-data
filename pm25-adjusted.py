# This script aims to create a plot displaying the adjusted national
# population-weighted distributions of intraurban differences in PM25 levels
# within HOLC-mapped areas at the census block level as seen in Figure 1(d).
from createdf import init

import matplotlib.pyplot as plt
import numpy as np

def calculate_pwm(target, cities, pm25, pop):
   t = ((cities == target) & (~np.isnan(pm25)) & (~np.isnan(pop)))
   cities = cities[t]
   pm25 = pm25[t]
   pop = pop[t]
   pwm = np.average(pm25, weights = pop)
   return pwm

# -----------------------------------------------------------------------------

df = init()

cities = list(set(df['City']))
pwms = {}
for city in cities:
   pwms[city] = calculate_pwm(city, df['City'], df['PM25'], df['Total'])

pm25_A         = []
pm25_B         = []
pm25_C         = []
pm25_D         = []
pm25_white     = []
pm25_other     = []
pm25_black     = []
pm25_asian     = []
pm25_hispanic  = []

for i in df.index:
   if df['Grade'][i] == 'A':
      pm25_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      pm25_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      pm25_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      pm25_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] != 'N':
      pm25_white += (round(df['PHOLC'][i] * df['White'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_other += (round(df['PHOLC'][i] * df['Other'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_black += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])

data = [pm25_A, pm25_B, pm25_C, pm25_D, pm25_white, pm25_other, pm25_black, pm25_asian, pm25_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Adjusted: Intraurban Variation')

ax.set_ylim(-0.8, 0.6)
for median in plot['medians']:
   median.set_color('black')

colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
          'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

plt.savefig('pm25-adjusted.png', dpi = 300)
