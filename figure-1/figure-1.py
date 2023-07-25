# `figure-1.py` generates the four plots from Figure 1 in the study, which
# displays NO₂ levels (measured in ppb) and PM₂.₅ levels (measured in μg/m³) by
# both HOLC grade and demographics, in unadjusted and adjusted format.
#
# Unadjusted plots show the nationwide distributions of these air pollutants
# in HOLC-mapped areas.
#
# Adjusted plots show the distributions of air pollutant levels in each block,
# minus the population-weighted mean level of that pollutant of the city that
# block belongs in.
#
# Running this script took about 20 minutes on my machine.

from utils import init
from utils import collect_data

import matplotlib.pyplot as plt
import numpy as np

# `generate_plot` abstracts the plot generation process and allows users to
# customize the input data, as well as cosmetic details of each plot, such as
# the labels to use, the title to name the plot, as well as the colors and
# file name.
def generate_plot(data, labels, title, x_label, y_label, min_y, max_y, y_ticks, colors, file_name):
   fig, ax = plt.subplots(nrows = 1, ncols = 1)
   plot = ax.boxplot(data, labels = labels, patch_artist = True,
                     showfliers = False, showmeans = True, vert = True, whis = 0,
                     meanprops = {"marker": "o", "markerfacecolor": "black", "markeredgecolor": "black"})
   ax.set_title(title)
   ax.set_xlabel(x_label)
   ax.set_ylabel(y_label)
   ax.set_ylim(min_y, max_y)
   ax.set_yticks(y_ticks)
   ax.axhline(y = np.nanmean([elem for lst in data for elem in lst]),
              color = 'black', linestyle = '--', linewidth = 1, label = 'Overall Mean')
   ax.legend()
   for median in plot['medians']: median.set_color('black')
   for patch, color in zip(plot['boxes'], colors): patch.set_facecolor(color)
   plt.savefig(file_name, dpi = 300)

# Script to collect data and generate plots begins here:
# -----------------

# Initialize DataFrame.
df = init()

# Collect unadjusted and adjusted numbers for NO₂ and PM₂.₅ concentration.
no2_unadjusted  = collect_data(df, 'PHOLC', 'NO2',  False)
no2_adjusted    = collect_data(df, 'PHOLC', 'NO2',  True)
pm25_unadjusted = collect_data(df, 'PHOLC', 'PM25', False)
pm25_adjusted   = collect_data(df, 'PHOLC', 'PM25', True)

# Initialize cosmetic details.
labels  = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']
x_label = 'HOLC Grade and Race/Ethnicity'
colors  = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
           'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']

# Generate the four plots.
generate_plot(no2_unadjusted, labels, 'Unadjusted NO₂ Levels: National',
              x_label, 'Population-Weighted NO₂ (ppb)', 0, 25, (0, 5, 10, 15, 20, 25),
              colors, 'figure-1-a.png')
generate_plot(pm25_unadjusted, labels, 'Unadjusted PM₂.₅ Levels: National',
              x_label, 'Population-Weighted PM₂.₅ (μg/m³)', 0, 15, (0, 5, 10),
              colors, 'figure-1-b.png')
generate_plot(no2_adjusted, labels, 'Adjusted NO₂ Levels: Intraurban Variation',
              x_label, 'Intraurban NO₂ Difference (ppb)', -4, 3, (-4, -2, 0, 2),
              colors, 'figure-1-c.png')
generate_plot(pm25_adjusted, labels, 'Adjusted PM₂.₅ Levels: Intraurban Variation',
              x_label, 'Intraurban PM2.5 Difference (μg/m³)', -0.8, 0.6, (-0.8, -0.4, 0.0, 0.4),
              colors, 'figure-1-d.png')
