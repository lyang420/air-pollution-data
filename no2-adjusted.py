# This script aims to create a plot displaying the adjusted national
# population-weighted distributions of intraurban differences in NO2 levels
# within HOLC-mapped areas at the census block level as seen in Figure 1(c).
from createdf import init

import matplotlib.pyplot as plt
import numpy as np

# The function `calculate_pwm` calculates the population-weighted mean NO2
# concentration for the city `target` per Eq. 1 of the supporting information.
def calculate_pwm(target, cities, no2, pop):
   t = ((cities == target) & (~np.isnan(no2)) & (~np.isnan(pop)))
   cities = cities[t]
   no2 = no2[t]
   pop = pop[t]
   pwm = np.average(no2, weights = pop)
   return pwm

# -----------------------------------------------------------------------------

df = init()

cities = list(set(df['City']))
pwms = {}
for city in cities:
   pwms[city] = calculate_pwm(city, df['City'], df['NO2'], df['Total'])

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
      no2_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      no2_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      no2_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      no2_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] != 'N':
      no2_white += (round(df['PHOLC'][i] * df['White'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_other += (round(df['PHOLC'][i] * df['Other'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_black += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])

data = [no2_A, no2_B, no2_C, no2_D, no2_white, no2_other, no2_black, no2_asian, no2_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Adjusted: Intraurban Variation')

ax.set_ylim(-4, 3)
for median in plot['medians']:
   median.set_color('black')

colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
          'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

plt.savefig('no2-adjusted.png', dpi = 300)
