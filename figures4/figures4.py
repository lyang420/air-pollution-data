from utils import init
from utils import collect_percentile

import matplotlib.pyplot as plt

df = init()

no2_data = collect_percentile(df, 'NO2')
pm25_data = collect_percentile(df, 'PM25')
percentiles = range(0, 100)

fig1, ax1 = plt.subplots()
l1 = plt.scatter(percentiles, no2_data[0], s = 10, label = 'A')
l2 = plt.scatter(percentiles, no2_data[1], s = 10, label = 'B')
l3 = plt.scatter(percentiles, no2_data[2], s = 10, label = 'C')
l4 = plt.scatter(percentiles, no2_data[3], s = 10, label = 'D')
l5 = plt.scatter(percentiles, no2_data[4], s = 10, label = 'CUA')
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.xlabel("Population Percentile")
plt.ylabel("NO2")
ax1.set_ylim(0, 35)
ax1.legend()

plt.savefig('figures4a.png', dpi = 300)

fig2, ax2 = plt.subplots()
l1 = plt.scatter(percentiles, pm25_data[0], s = 10, label = 'A')
l2 = plt.scatter(percentiles, pm25_data[1], s = 10, label = 'B')
l3 = plt.scatter(percentiles, pm25_data[2], s = 10, label = 'C')
l4 = plt.scatter(percentiles, pm25_data[3], s = 10, label = 'D')
l5 = plt.scatter(percentiles, pm25_data[4], s = 10, label = 'CUA')
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.xlabel("Population Percentile")
plt.ylabel("PM2.5")
ax2.set_ylim(0, 16)
ax2.legend()

plt.savefig('figures4b.png', dpi = 300)
