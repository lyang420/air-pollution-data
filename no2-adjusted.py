# This script aims to create a plot displaying the adjusted national
# population-weighted distributions of intraurban differences in NO2 levels
# within HOLC-mapped areas at the census block level as seen in Figure 1(c).
from createdf import init

import numpy as np
import pandas as pd

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

for i in df.index:
   if df['Grade'][i] == 'A':
      no2_A += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'B':
      no2_B += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'C':
      no2_C += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])
   if df['Grade'][i] == 'D':
      no2_D += (df['Total'][i] * [(df['NO2'][i] - pwms[df['City'][i]])])