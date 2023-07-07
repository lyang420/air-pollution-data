# This script aims to create a plot displaying the adjusted national
# population-weighted distributions of intraurban differences in PM25 levels
# within HOLC-mapped areas at the census block level in line format as seen in
# Figure 2(b).
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

plt.plot(x_ax, [h1, h2, h3, h4], 'g--')
plt.plot(x_ax, [a1, a2, a3, a4], 'b:')
plt.plot(x_ax, [b1, b2, b3, b4], 'm-')
plt.plot(x_ax, [t1, t2, t3, t4], 'k-')
plt.plot(x_ax, [w1, w2, w3, w4], 'm--')
plt.savefig('pm25-intraurban-diff.png', dpi = 300)
