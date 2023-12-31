# `figure-s3.py` generates the two plots from Figure S3, shown in the study's
# supporting information file. These plots show the demographics of the
# residents sampled in the raw data.

from utils import init
from utils import collect_data_residents

import matplotlib.pyplot as plt
import numpy as np

# `generate_plot` abstracts the plot generation process and allows users to
# customize the input data, as well as cosmetic details of each plot, such as
# the labels to use, the title to name the plot, as well as the colors and
# file name.
def generate_plot(weights, width, title, x_label, y_label, y_tick_loc, y_ticks,
                  file_name):
   fig, ax = plt.subplots()
   bottom = np.zeros(4)
   for ethnicity, weight_count in weights.items():
      p = ax.bar(grades, weight_count, width, label = ethnicity, bottom = bottom)
      bottom += weight_count
   ax.set_title(title)
   ax.set_xlabel(x_label)
   ax.set_ylabel(y_label)
   ax.set_yticks(y_tick_loc, y_ticks)
   ax.legend(loc = "upper right")
   plt.savefig(file_name, dpi = 300)

# Initialize DataFrame
df = init()

# Collect data.
numeric_data, percentage_data = collect_data_residents(df, 'PHOLC', 1000000.0)
grades = ("A", "B", "C", "D")

# Organize data to be fed into matplotlib.
numeric_weights = {
   "White"    : numeric_data[0],
   "Other"    : numeric_data[1],
   "Black"    : numeric_data[2],
   "Asian"    : numeric_data[3],
   "Hispanic" : numeric_data[4]
}

percentage_weights = {
   "White"    : percentage_data[0],
   "Other"    : percentage_data[1],
   "Black"    : percentage_data[2],
   "Asian"    : percentage_data[3],
   "Hispanic" : percentage_data[4]
}

# Generate the two plots.
generate_plot(numeric_weights, 0.65, 'Demographics in HOLC-Mapped Areas',
              'HOLC Grade', 'Population (Millions)', (0, 5, 10, 15, 20),
              (0, 5, 10, 15, 20), 'figure-s3-a.png')
generate_plot(percentage_weights, 0.65, 'Demographics in HOLC-Mapped Areas',
              'HOLC Grade', 'Population (Percentages)', (0, 25, 50, 75, 100),
              ('0%', '25%', '50%', '75%', '100%'), 'figure-s3-b.png')
