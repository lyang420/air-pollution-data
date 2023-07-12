from createdf import init
import matplotlib.pyplot as plt
import numpy as np

def count_population(target_city, all_cities, grade, PHOLC, population):
   condition = ((all_cities == target_city) & (~np.equal(grade, 'N')))
   PHOLC = PHOLC[condition]
   population = population[condition]
   return sum(round(PHOLC * population))

def calculate_pwm(target_city, all_cities, no2, PHOLC, population):
   t = ((all_cities == target_city) & (~np.isnan(no2)) & (~np.isnan(population)))
   no2 = no2[t]
   PHOLC = PHOLC[t]
   population = population[t]
   pwm = np.average(no2, weights = round(PHOLC * population))
   return pwm

df = init()
cities = set(df['City'])
cities.remove('NA')
pwms = {}
for city in cities:
   pwms[city] = calculate_pwm(city, df['City'], df['NO2'], df['PHOLC'], df['Total'])
city_pops = {}
for city in cities:
   city_pops[city] = count_population(city, df['City'], np.array(df['Grade']), df['PHOLC'], df['Total'])
sorted_pops = list(city_pops.values())
sorted_pops.sort()
small_cities = []
medium_cities = []
large_cities = []
for i in range(0, 173):
   small_cities.append(list(city_pops.keys())[list(city_pops.values()).index(sorted_pops[i])])
for i in range(173, 194):
   medium_cities.append(list(city_pops.keys())[list(city_pops.values()).index(sorted_pops[i])])
for i in range(194, 202):
   large_cities.append(list(city_pops.keys())[list(city_pops.values()).index(sorted_pops[i])])
small_A  = []
small_B  = []
small_C  = []
small_D  = []
medium_A = []
medium_B = []
medium_C = []
medium_D = []
large_A  = []
large_B  = []
large_C  = []
large_D  = []
for i in df.index:
   if df['City'][i] in small_cities:
      if df['Grade'][i] == 'A':
         small_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'B':
         small_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'C':
         small_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'D':
         small_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
   if df['City'][i] in medium_cities:
      if df['Grade'][i] == 'A':
         medium_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'B':
         medium_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'C':
         medium_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'D':
         medium_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
   if df['City'][i] in large_cities:
      if df['Grade'][i] == 'A':
         large_A += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'B':
         large_B += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'C':
         large_C += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
      if df['Grade'][i] == 'D':
         large_D += (round(df['PHOLC'][i] * df['Total'][i]) * [(df['NO2'][i]) - pwms[df['City'][i]]])
small_A_mean = np.average(small_A)
small_B_mean = np.average(small_B)
small_C_mean = np.average(small_C)
small_D_mean = np.average(small_D)
medium_A_mean = np.average(medium_A)
medium_B_mean = np.average(medium_B)
medium_C_mean = np.average(medium_C)
medium_D_mean = np.average(medium_D)
large_A_mean = np.average(large_A)
large_B_mean = np.average(large_B)
large_C_mean = np.average(large_C)
large_D_mean = np.average(large_D)
axis = ['A', 'B', 'C', 'D']
fig, ax = plt.subplots()
line1 = ax.plot(axis, [small_A_mean, small_B_mean, small_C_mean, small_D_mean], 'g-', label = 'Small')
line2 = ax.plot(axis, [medium_A_mean, medium_B_mean, medium_C_mean, medium_D_mean], 'y-', label = 'Medium')
line3 = ax.plot(axis, [large_A_mean, large_B_mean, large_C_mean, large_D_mean], 'r-', label = 'Large')
ax.set_ylim(-4, 2)
ax.set_title('Intraurban Differences by City Size')
ax.legend()
plt.savefig('no2-diff-city(2).png', dpi = 300)
