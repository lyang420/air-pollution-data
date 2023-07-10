# `no2-adjusted.py` creates a plot displaying the adjusted national
# population-weighted distribution of intraurban differences in NO2 levels
# within HOLC-mapped areas at the census block level as specified in Figure
# 1(c).
from createdf import init
import matplotlib.pyplot as plt
import numpy as np

# `calculate_pwm` calculates the population-weighted mean (PWM) NO2
# concentration for the city `target`, per Eq. 1 from the supporting
# information.
def calculate_pwm(target, cities, no2, pop):
   # Given a city to calculate the PWM for, and lists of all cities, their NO2
   # levels, and populations, filter them such that we only process the city
   # of interest, and NO2/population statistics that are actual numbers.
   t = ((cities == target) & (~np.isnan(no2)) & (~np.isnan(pop)))
   cities = cities[t]
   no2 = no2[t]
   pop = pop[t]
   pwm = np.average(no2, weights = pop)
   return pwm

# Initialize DataFrame from imported function.
df = init()

# `cities` is a list of all unique cities from the raw data.
cities = list(set(df['City']))

# `pwms` is a dictionary that stores all cities from the raw data and their
# respective PWM NO2 levels.
pwms = {}
for city in cities:
   pwms[city] = calculate_pwm(city, df['City'], df['NO2'], df['Total'])

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
#
# Notice also we are subtracting the PWM of each entry's city from the NO2
# level, in accordance with the study.
for i in df.index:
   if df['Grade'][i] == 'A':
      no2_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      no2_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      no2_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      no2_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
   # Per the study: This plot displays statistics for HOLC-mapped areas. If you
   # do not filter by grade and only by ethnicity here, you are going to get
   # some very different numbers.
   if df['Grade'][i] != 'N':
      no2_white += (round(df['PHOLC'][i] * df['White'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_other += (round(df['PHOLC'][i] * df['Other'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_black += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['NO2'][i] - pwms[df['City'][i]])])

# Organize data into list to feed into plot generator.
data = [no2_A, no2_B, no2_C, no2_D, no2_white, no2_other, no2_black, no2_asian, no2_hispanic]
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']

# Generate plot, customize appearance, and set title.
fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Adjusted: Intraurban Variation')

# Set minimum and maximum y-values, do not let the software try to do it
# automatically.
ax.set_ylim(-4, 3)
for median in plot['medians']:
   median.set_color('black')

# You may set the color of each shape in this boxplot yourself.
colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
          'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

# Save figure.
plt.savefig('no2-adjusted.png', dpi = 300)
