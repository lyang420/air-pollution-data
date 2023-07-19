# `pm25-adjusted.py` creates a plot displaying the adjusted national
# population-weighted distribution of intraurban differences in PM2.5 levels
# within HOLC-mapped areas at the census block level as specified in Figure
# 1(d).
from utils import init
import matplotlib.pyplot as plt
import numpy as np

# `calculate_pwm` calculates the population-weighted mean (PWM) PM2.5
# concentration for the city `target`, per Eq. 1 from the supporting
# information.
def calculate_pwm(target, cities, pm25, pop):
   # Given a city to calculate the PWM for, and lists of all cities, their
   # PM2.5 levels, and populations, filter them such that we only process the
   # city of interest, and NO2/population statistics that are actual numbers.
   t = ((cities == target) & (~np.isnan(pm25)) & (~np.isnan(pop)))
   cities = cities[t]
   pm25 = pm25[t]
   pop = pop[t]
   pwm = np.average(pm25, weights = pop)
   return pwm

# Initialize DataFrame from imported function.
df = init()

# `cities` is a list of all unique cities from the raw data.
cities = list(set(df['City']))

# `pwms` is a dictionary that stores all cities from the raw data and their
# respective PWM NO2 levels.
pwms = {}
for city in cities:
   pwms[city] = calculate_pwm(city, df['City'], df['PM25'], df['Total'])

# Lists to store data to be used to generate plots: NO2 levels by HOLC grade,
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
#
# Notice also we are subtracting the PWM of each entry's city from the PM2.5
# level, in accordance with the study.
for i in df.index:
   if df['Grade'][i] == 'A':
      pm25_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      pm25_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      pm25_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      pm25_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   # Per the study: This plot displays statistics for HOLC-mapped areas. If you
   # do not filter by grade and only by ethnicity here, you are going to get
   # some very different numbers.
   if df['Grade'][i] != 'N':
      pm25_white += (round(df['PHOLC'][i] * df['White'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_other += (round(df['PHOLC'][i] * df['Other'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_black += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])

# Organize data into list to feed into plot generator.
data = [pm25_A, pm25_B, pm25_C, pm25_D, pm25_white, pm25_other, pm25_black, pm25_asian, pm25_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

# Generate plot, customize appearance, and set title.
fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Adjusted: Intraurban Variation')

# Set minimum and maximum y-values, do not let the software try to do it
# automatically.
ax.set_ylim(-0.8, 0.6)
for median in plot['medians']:
   median.set_color('black')

# You may set the color of each shape in this boxplot yourself.
colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
          'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

# Save figure.
plt.savefig('pm25-adjusted.png', dpi = 300)
