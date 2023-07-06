# This script aims to create a plot displaying the adjusted national
# population-weighted distributions of intraurban differences in NO2 levels
# within HOLC-mapped areas at the census block level in line format as seen in
# Figure 2(a).
from createdf import init

import matplotlib.pyplot as plt
import numpy as np

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

no2_hispanic_A = []
no2_hispanic_B = []
no2_hispanic_C = []
no2_hispanic_D = []
no2_asian_A    = []
no2_asian_B    = []
no2_asian_C    = []
no2_asian_D    = []
no2_black_A    = []
no2_black_B    = []
no2_black_C    = []
no2_black_D    = []
no2_total_A    = []
no2_total_B    = []
no2_total_C    = []
no2_total_D    = []
no2_white_A    = []
no2_white_B    = []
no2_white_C    = []
no2_white_D    = []

for i in df.index:
   if df['Grade'][i] == 'A':
      no2_hispanic_A += (df['Hispanic'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_asian_A += (df['Asian'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_black_A += (df['Black'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_total_A += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_white_A += (df['White'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      no2_hispanic_B += (df['Hispanic'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_asian_B += (df['Asian'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_black_B += (df['Black'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_total_B += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_white_B += (df['White'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      no2_hispanic_C += (df['Hispanic'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_asian_C += (df['Asian'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_black_C += (df['Black'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_total_C += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_white_C += (df['White'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      no2_hispanic_D += (df['Hispanic'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_asian_D += (df['Asian'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_black_D += (df['Black'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_total_D += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
      no2_white_D += (df['White'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])

h1 = np.average(no2_hispanic_A)
h2 = np.average(no2_hispanic_B)
h3 = np.average(no2_hispanic_C)
h4 = np.average(no2_hispanic_D)
a1 = np.average(no2_asian_A)
a2 = np.average(no2_asian_B)
a3 = np.average(no2_asian_C)
a4 = np.average(no2_asian_D)
b1 = np.average(no2_black_A)
b2 = np.average(no2_black_B)
b3 = np.average(no2_black_C)
b4 = np.average(no2_black_D)
t1 = np.average(no2_total_A)
t2 = np.average(no2_total_B)
t3 = np.average(no2_total_C)
t4 = np.average(no2_total_D)
w1 = np.average(no2_white_A)
w2 = np.average(no2_white_B)
w3 = np.average(no2_white_C)
w4 = np.average(no2_white_D)

x_ax = ['A', 'B', 'C', 'D']

plt.plot(x_ax, [h1, h2, h3, h4], 'g--')
plt.plot(x_ax, [a1, a2, a3, a4], 'b:')
plt.plot(x_ax, [b1, b2, b3, b4], 'm-')
plt.plot(x_ax, [t1, t2, t3, t4], 'k-')
plt.plot(x_ax, [w1, w2, w3, w4], 'm--')
plt.savefig('no2-intraurban-diff.png', dpi = 300)
