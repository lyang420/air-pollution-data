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
      no2_A += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      no2_B += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      no2_C += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      no2_D += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['White'][i] > 0:
      no2_white += (df['White'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Other'][i] > 0:
      no2_other += (df['Other'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Black'][i] > 0:
      no2_black += (df['Black'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Asian'][i] > 0:
      no2_asian += (df['Asian'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Hispanic'][i] > 0:
      no2_hispanic += (df['Hispanic'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])

data = [no2_A, no2_B, no2_C, no2_D, no2_white, no2_other, no2_black, no2_asian, no2_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

fig1, ax1 = plt.subplots(nrows = 1, ncols = 1)
no2_plot = ax1.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax1.set_title('Adjusted: intraurban variation only')

ax1.set_ylim(-4, 4)
for median in no2_plot['medians']:
   median.set_color('black')

colors = ['forestgreen', 'cornflowerblue', 'goldenrod', 'firebrick', 'palevioletred', 'darkkhaki', 'plum', 'slateblue', 'mediumseagreen']
for patch, color in zip(no2_plot['boxes'], colors):
   patch.set_facecolor(color)

plt.savefig('no2-adjusted.png', dpi = 300)
