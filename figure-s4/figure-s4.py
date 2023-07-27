from utils import init
from utils import collect_data_percentile

import matplotlib.pyplot as plt

def generate_plot(data, percentiles, title, x_label, y_label, y_min, y_max,
                  x_tick_loc, x_ticks, y_ticks, file_name):
   fig, ax = plt.subplots()
   l1 = plt.scatter(percentiles, data[0], s = 5, label = 'HOLC Grade A')
   l2 = plt.scatter(percentiles, data[1], s = 5, label = 'HOLC Grade B')
   l3 = plt.scatter(percentiles, data[2], s = 5, label = 'HOLC Grade C')
   l4 = plt.scatter(percentiles, data[3], s = 5, label = 'HOLC Grade D')
   l5 = plt.scatter(percentiles, data[4], s = 5, label = 'CUA (Census Urbanized Area)')
   ax.set_title(title)
   ax.set_xlabel(x_label)
   ax.set_ylabel(y_label)
   ax.set_ylim(y_min, y_max)
   ax.set_xticks(x_tick_loc, x_ticks)
   ax.set_yticks(y_ticks)
   ax.legend()
   ax.set_axisbelow(True)
   ax.grid(color = "gainsboro")
   ax.figure.set_figwidth(5)
   plt.savefig(file_name, dpi = 300)

df = init()

no2_data = collect_data_percentile(df, 'PHOLC', 'Total', 'NO2')
pm25_data = collect_data_percentile(df, 'PHOLC', 'Total', 'PM25')
percentiles = range(0, 100)
ticks = (0.01, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99.99)

generate_plot(no2_data, percentiles, 'Overall Cumulative NO₂ Distribution',
              'Population Percentile', 'NO₂ (ppb)', 0, 35, ticks, ticks,
              (0, 10, 20, 30), 'figure-s4-a.png')
generate_plot(pm25_data, percentiles, 'Overall Cumulative PM₂.₅ Distribution',
              'Population Percentile', 'PM₂.₅ (μg/m³)', 0, 16, ticks, ticks,
              (4, 8, 12, 16), 'figure-s4-b.png')
