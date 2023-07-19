# `no2-diff.py` creates a plot displaying the adjusted national
# population-weighted distribution of intraurban differences in PM2.5 levels
# within HOLC-mapped areas at the census block level as specified in Figure
# 2(b).
from utils import init
import matplotlib.pyplot as plt
import numpy as np

# `calculate_pwm` calculates the population-weighted mean (PWM) PM2.5
# concentration for the city `target`, per Eq. 1 from the supporting
# information. As I am copying and pasting this function into yet another
# script, I am starting to wonder if this, too, can be abstracted into another
# file, much like the DataFrame initialization function, and just how much of
# the repetitive processes I've written can be abstracted into a few separate
# files.
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

# This plot utilizes the same data as that from `pm25-adjusted.py`, except that
# instead of a box-and-whisker plot, it generates a line chart. Thus,
# lines are generated for each listed ethnicity in the study, with each line
# having four points, one for each HOLC grade.
pm25_hispanic_A = []
pm25_hispanic_B = []
pm25_hispanic_C = []
pm25_hispanic_D = []
pm25_asian_A    = []
pm25_asian_B    = []
pm25_asian_C    = []
pm25_asian_D    = []
pm25_black_A    = []
pm25_black_B    = []
pm25_black_C    = []
pm25_black_D    = []
pm25_total_A    = []
pm25_total_B    = []
pm25_total_C    = []
pm25_total_D    = []
pm25_white_A    = []
pm25_white_B    = []
pm25_white_C    = []
pm25_white_D    = []

# Iterate through DataFrame and add appropriate numbers to corresponding lists.
# Notice that the population figure is always multiplied by the `PHOLC` of each
# entry, as that denotes the proportion of the number of people living in the
# marked HOLC grade.
#
# Notice also we are subtracting the PWM of each entry's city from the PM2.5
# level, in accordance with the study.
for i in df.index:
   if df['Grade'][i] == 'A':
      pm25_hispanic_A += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_asian_A += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_black_A += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_total_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_white_A += (round(df['PHOLC'][i] * df['White'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      pm25_hispanic_B += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_asian_B += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_black_B += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_total_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_white_B += (round(df['PHOLC'][i] * df['White'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      pm25_hispanic_C += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_asian_C += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_black_C += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_total_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_white_C += (round(df['PHOLC'][i] * df['White'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      pm25_hispanic_D += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_asian_D += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_black_D += (round(df['PHOLC'][i] * df['Black'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_total_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])
      pm25_white_D += (round(df['PHOLC'][i] * df['White'][i]) * [(df['PM25'][i] - pwms[df['City'][i]])])

# The plot's points are the population-weighted means of the intraurban
# differences, which we collected above.
h1 = np.average(pm25_hispanic_A)
h2 = np.average(pm25_hispanic_B)
h3 = np.average(pm25_hispanic_C)
h4 = np.average(pm25_hispanic_D)
a1 = np.average(pm25_asian_A)
a2 = np.average(pm25_asian_B)
a3 = np.average(pm25_asian_C)
a4 = np.average(pm25_asian_D)
b1 = np.average(pm25_black_A)
b2 = np.average(pm25_black_B)
b3 = np.average(pm25_black_C)
b4 = np.average(pm25_black_D)
t1 = np.average(pm25_total_A)
t2 = np.average(pm25_total_B)
t3 = np.average(pm25_total_C)
t4 = np.average(pm25_total_D)
w1 = np.average(pm25_white_A)
w2 = np.average(pm25_white_B)
w3 = np.average(pm25_white_C)
w4 = np.average(pm25_white_D)
x_ax = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
line1 = ax.plot(x_ax, [h1, h2, h3, h4], 'g--', label = 'Hispanic')
line2 = ax.plot(x_ax, [a1, a2, a3, a4], 'b:', label = 'Asian')
line3 = ax.plot(x_ax, [b1, b2, b3, b4], 'm-', label = 'Black')
line4 = ax.plot(x_ax, [t1, t2, t3, t4], 'k-', label = 'Total')
line5 = ax.plot(x_ax, [w1, w2, w3, w4], 'm--', label = 'White')
ax.set_ylim(-0.4, 0.2)
ax.set_title('Intraurban PM2.5 Difference')
ax.legend()
plt.savefig('pm25-intraurban-diff.png', dpi = 300)
