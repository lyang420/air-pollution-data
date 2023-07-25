from utils import init
from utils import collect_data_intraurban_diff

import matplotlib.pyplot as plt

def generate_plot(data, axes, x_label, y_label, y_min, y_max, y_ticks, file_name):
   fig, ax = plt.subplots()
   ax.plot(axes, data[0], 'g--', label = 'Hispanic')
   ax.plot(axes, data[1], 'b:', label = 'Asian')
   ax.plot(axes, data[2], 'm-', label = 'Black')
   ax.plot(axes, data[3], 'k-', label = 'Total')
   ax.plot(axes, data[4], 'm--', label = 'White')
   ax.axhline(y = 0, color = 'grey', linestyle = '-', linewidth = 1)
   ax.set_xlabel(x_label)
   ax.set_ylabel(y_label)
   ax.set_ylim(y_min, y_max)
   ax.set_yticks(y_ticks)
   ax.legend()
   plt.savefig(file_name, dpi = 300)

df = init()

no2_intraurban_diff = collect_data_intraurban_diff(df, 'PHOLC', 'NO2')
pm25_intraurban_diff = collect_data_intraurban_diff(df, 'PHOLC', 'PM25')

axes = ['A', 'B', 'C', 'D']

generate_plot(no2_intraurban_diff, axes, 'HOLC Grade',
              'Intraurban NO₂ Difference (ppb)', -2.5, 1.5,
              (-2, -1, 0, 1), 'figure-2-a.png')
generate_plot(pm25_intraurban_diff, axes, 'HOLC Grade',
              'Intraurban PM₂.₅ Difference (μg/m³)', -0.4, 0.2,
              (-0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2), 'figure-2-b.png')
