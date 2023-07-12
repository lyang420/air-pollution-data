from createdf import init
import matplotlib.pyplot as plt
import numpy as np

def count_population(target_city, all_cities, grade, PHOLC, population):
   condition = ((all_cities == target_city) & (~np.equal(grade, 'N')))
   PHOLC = PHOLC[condition]
   population = population[condition]
   return sum(round(PHOLC * population))

df = init()
cities = set(df['City'])
cities.remove('NA')
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
small_A_weights = []
small_B_weights = []
small_C_weights = []
small_D_weights = []
medium_A_weights = []
medium_B_weights = []
medium_C_weights = []
medium_D_weights = []
large_A_weights = []
large_B_weights = []
large_C_weights = []
large_D_weights = []
for i in df.index:
   if df['City'][i] in small_cities:
      if df['Grade'][i] == 'A':
         small_A.append(df['NO2'][i])
         small_A_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'B':
         small_B.append(df['NO2'][i])
         small_B_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'C':
         small_C.append(df['NO2'][i])
         small_C_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'D':
         small_D.append(df['NO2'][i])
         small_D_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
   if df['City'][i] in medium_cities:
      if df['Grade'][i] == 'A':
         medium_A.append(df['NO2'][i])
         medium_A_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'B':
         medium_B.append(df['NO2'][i])
         medium_B_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'C':
         medium_C.append(df['NO2'][i])
         medium_C_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'D':
         medium_D.append(df['NO2'][i])
         medium_D_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
   if df['City'][i] in large_cities:
      if df['Grade'][i] == 'A':
         large_A.append(df['NO2'][i])
         large_A_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'B':
         large_B.append(df['NO2'][i])
         large_B_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'C':
         large_C.append(df['NO2'][i])
         large_C_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
      if df['Grade'][i] == 'D':
         large_D.append(df['NO2'][i])
         large_D_weights.append(round(df['PHOLC'][i] * df['Total'][i]))
small_A_mean = np.average(small_A, weights = small_A_weights)
small_B_mean = np.average(small_B, weights = small_B_weights)
small_C_mean = np.average(small_C, weights = small_C_weights)
small_D_mean = np.average(small_D, weights = small_D_weights)
medium_A_mean = np.average(medium_A, weights = medium_A_weights)
medium_B_mean = np.average(medium_B, weights = medium_B_weights)
medium_C_mean = np.average(medium_C, weights = medium_C_weights)
medium_D_mean = np.average(medium_D, weights = medium_D_weights)
large_A_mean = np.average(large_A, weights = large_A_weights)
large_B_mean = np.average(large_B, weights = large_B_weights)
large_C_mean = np.average(large_C, weights = large_C_weights)
large_D_mean = np.average(large_D, weights = large_D_weights)
print(small_A_mean)
print(small_B_mean)
print(small_C_mean)
print(small_D_mean)
print(medium_A_mean)
print(medium_B_mean)
print(medium_C_mean)
print(medium_D_mean)
print(large_A_mean)
print(large_B_mean)
print(large_C_mean)
print(large_D_mean)
axis = ['A', 'B', 'C', 'D']
fig, ax = plt.subplots()
line1 = ax.plot(axis, [small_A_mean, small_B_mean, small_C_mean, small_D_mean], 'g-', label = 'Small')
line2 = ax.plot(axis, [medium_A_mean, medium_B_mean, medium_C_mean, medium_D_mean], 'y-', label = 'Medium')
line3 = ax.plot(axis, [large_A_mean, large_B_mean, large_C_mean, large_D_mean], 'r-', label = 'Large')
ax.set_ylim(0, 25)
ax.set_title('Population-Weighted')
ax.legend()
plt.savefig('no2-unadjusted-city(3).png', dpi = 300)
