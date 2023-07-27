from utils import init
from utils import collect_data_city

import matplotlib.pyplot as plt

def generate_plot(axis, data, title, x_label, y_label, y_min, y_max,
                  y_tick_loc, y_ticks, figure_name):
   fig, ax = plt.subplots()
   l1 = ax.plot(axis, data[0], color = 'peachpuff', linewidth = 3, label = 'Small')
   l2 = ax.plot(axis, data[1], color = 'peru',      linewidth = 3, label = 'Medium')
   l3 = ax.plot(axis, data[2], color = 'darkred',   linewidth = 3, label = 'Large')
   ax.set_title(title)
   ax.set_xlabel(x_label)
   ax.set_ylabel(y_label)
   ax.set_ylim(y_min, y_max)
   ax.set_yticks(y_tick_loc, y_ticks)
   ax.axhline(y = 0, color = 'black', linestyle = '--', linewidth = 1)
   ax.legend()
   ax.set_axisbelow(True)
   ax.grid(color = "gainsboro")
   plt.savefig(figure_name, dpi = 300)

df = init()

no2_unadjusted_data          = collect_data_city(df, 'PHOLC', 'Total', 'NO2',  False, False)
no2_intraurban_raw_data      = collect_data_city(df, 'PHOLC', 'Total', 'NO2',  True,  False)
no2_intraurban_percent_data  = collect_data_city(df, 'PHOLC', 'Total', 'NO2',  True,  True)
pm25_unadjusted_data         = collect_data_city(df, 'PHOLC', 'Total', 'PM25', False, False)
pm25_intraurban_raw_data     = collect_data_city(df, 'PHOLC', 'Total', 'PM25', True,  False)
pm25_intraurban_percent_data = collect_data_city(df, 'PHOLC', 'Total', 'PM25', True,  True)

axis = ['A', 'B', 'C', 'D']
title = 'Comparison of Population-Weighted Mean Pollution Levels by City Size'
x_label = 'HOLC Grade'

generate_plot(axis, no2_unadjusted_data, title, x_label,
              'Population-Weighted NO₂ (ppb)', -1, 22, (0, 5, 10, 15, 20),
              (0, 5, 10, 15, 20), 'figure-s5-a.png')
generate_plot(axis, pm25_unadjusted_data, title, x_label,
              'Population-Weighted PM₂.₅ (μg/m³)', -1, 12, (0, 3, 6, 9),
              (0, 3, 6, 9), 'figure-s5-b.png')
generate_plot(axis, no2_intraurban_raw_data, title, x_label,
              'Intraurban NO₂ Difference (ppb)', -4, 2, (-4, -3, -2, -1, 0, 1),
              (-4, -3, -2, -1, 0, 1), 'figure-s5-c.png')
generate_plot(axis, pm25_intraurban_raw_data, title, x_label,
              'Intraurban PM₂.₅ Difference (μg/m³)', -0.6, 0.15,
              (-0.4, -0.2, 0.0), (-0.4, -0.2, 0.0), 'figure-s5-d.png')
generate_plot(axis, no2_intraurban_percent_data, title, x_label,
              'Intraurban NO₂ Difference (Percentage)', -25, 15,
              (-20, -10, 0, 10), ('-20%', '-10%', '0%', '10%'),
              'figure-s5-e.png')
generate_plot(axis, pm25_intraurban_percent_data, title, x_label,
              'Intraurban PM₂.₅ Difference (Percentage)', -5, 2,
              (-5, -4, -3, -2, -1, 0, 1),
              ('-5%', '-4%', '-3%', '-2%', '-1%', '0%', '1%'),
              'figure-s5-f.png')
