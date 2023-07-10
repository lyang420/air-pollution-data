# `demographics.py` generates two plots, both shown in Figure S3 from the
# supporting information:
#
# The first displays the total number of residents living in blocks of 'A,'
# 'B,' 'C,' or 'D,' HOLC grade. The second displays the demographics of blocks
# of each grade.
from createdf import init
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Initialize DataFrame from the imported function.
df = init()

# Initialize lists to store the numbers to be used in plot generation. Each
# list corresponds to an ethnicity listed in the study, and has four spots, one
# for each listed HOLC grade.
white_HOLC    = [0, 0, 0, 0]
other_HOLC    = [0, 0, 0, 0]
black_HOLC    = [0, 0, 0, 0]
asian_HOLC    = [0, 0, 0, 0]
hispanic_HOLC = [0, 0, 0, 0]
# All numbers in each list will eventually be divided by `divisor`, as the plot
# displays the population by millions. Add a decimal at the end so the numbers
# don't get skewed by integer rounding.
divisor       = 1000000.0

# Iterate through the DataFrame and sort the population numbers first by
# ethnicity, and then by HOLC grade. Notice how the number of residents are
# multiplied by the column titled `PHOLC`. `PHOLC` represents the percentage of
# each block attributed to an HOLC grade, so if `PHOLC` = 0.80, 80% of the
# population in that block live in an area attributed to that HOLC grade.
#
# This is the calculation used in all the code in this repository. Without it,
# numbers do differ, but marginally.
for i in df.index:
   if df['Grade'][i] == 'A':
      white_HOLC[0] += df['PHOLC'][i] * df['White'][i]
      other_HOLC[0] += df['PHOLC'][i] * df['Other'][i]
      black_HOLC[0] += df['PHOLC'][i] * df['Black'][i]
      asian_HOLC[0] += df['PHOLC'][i] * df['Asian'][i]
      hispanic_HOLC[0] += df['PHOLC'][i] * df['Hispanic'][i]
   if df['Grade'][i] == 'B':
      white_HOLC[1] += df['PHOLC'][i] * df['White'][i]
      other_HOLC[1] += df['PHOLC'][i] * df['Other'][i]
      black_HOLC[1] += df['PHOLC'][i] * df['Black'][i]
      asian_HOLC[1] += df['PHOLC'][i] * df['Asian'][i]
      hispanic_HOLC[1] += df['PHOLC'][i] * df['Hispanic'][i]
   if df['Grade'][i] == 'C':
      white_HOLC[2] += df['PHOLC'][i] * df['White'][i]
      other_HOLC[2] += df['PHOLC'][i] * df['Other'][i]
      black_HOLC[2] += df['PHOLC'][i] * df['Black'][i]
      asian_HOLC[2] += df['PHOLC'][i] * df['Asian'][i]
      hispanic_HOLC[2] += df['PHOLC'][i] * df['Hispanic'][i]
   if df['Grade'][i] == 'D':
      white_HOLC[3] += df['PHOLC'][i] * df['White'][i]
      other_HOLC[3] += df['PHOLC'][i] * df['Other'][i]
      black_HOLC[3] += df['PHOLC'][i] * df['Black'][i]
      asian_HOLC[3] += df['PHOLC'][i] * df['Asian'][i]
      hispanic_HOLC[3] += df['PHOLC'][i] * df['Hispanic'][i]

# Divide all numbers by a million so the resulting plot image file won't get
# crowded with the software trying to list every raw number as is.
white_HOLC_adjusted = [x / divisor for x in white_HOLC]
other_HOLC_adjusted = [x / divisor for x in other_HOLC]
black_HOLC_adjusted = [x / divisor for x in black_HOLC]
asian_HOLC_adjusted = [x / divisor for x in asian_HOLC]
hispanic_HOLC_adjusted = [x / divisor for x in hispanic_HOLC]

# Total number of residents living in each HOLC grade.
A_total = white_HOLC[0] + other_HOLC[0] + black_HOLC[0] + asian_HOLC[0] + hispanic_HOLC[0]
B_total = white_HOLC[1] + other_HOLC[1] + black_HOLC[1] + asian_HOLC[1] + hispanic_HOLC[1]
C_total = white_HOLC[2] + other_HOLC[2] + black_HOLC[2] + asian_HOLC[2] + hispanic_HOLC[2]
D_total = white_HOLC[3] + other_HOLC[3] + black_HOLC[3] + asian_HOLC[3] + hispanic_HOLC[3]

# Residents of each ethnicity divided by the total number of residents in each
# HOLC grade, to be represented as percentages...
white_HOLC_raw = [white_HOLC[0] / A_total, white_HOLC[1] / B_total, white_HOLC[2] / C_total, white_HOLC[3] / D_total]
other_HOLC_raw = [other_HOLC[0] / A_total, other_HOLC[1] / B_total, other_HOLC[2] / C_total, other_HOLC[3] / D_total]
black_HOLC_raw = [black_HOLC[0] / A_total, black_HOLC[1] / B_total, black_HOLC[2] / C_total, black_HOLC[3] / D_total]
asian_HOLC_raw = [asian_HOLC[0] / A_total, asian_HOLC[1] / B_total, asian_HOLC[2] / C_total, asian_HOLC[3] / D_total]
hispanic_HOLC_raw = [hispanic_HOLC[0] / A_total, hispanic_HOLC[1] / B_total, hispanic_HOLC[2] / C_total, hispanic_HOLC[3] / D_total]

# ...and then multiply them by 100 so they show up as whole numbers, and we
# won't be seeing a whole lot of '0.75's on the graph.
white_HOLC_per = [x * 100 for x in white_HOLC_raw]
other_HOLC_per = [x * 100 for x in other_HOLC_raw]
black_HOLC_per = [x * 100 for x in black_HOLC_raw]
asian_HOLC_per = [x * 100 for x in asian_HOLC_raw]
hispanic_HOLC_per = [x * 100 for x in hispanic_HOLC_raw]

# Collect lists into fields to be fed into plot generation function.
grades = ("A", "B", "C", "D")
weight_counts_num = {
   "White": np.array(white_HOLC_adjusted),
   "Other": np.array(other_HOLC_adjusted),
   "Black": np.array(black_HOLC_adjusted),
   "Asian": np.array(asian_HOLC_adjusted),
   "Hispanic": np.array(hispanic_HOLC_adjusted)
}
weight_counts_per = {
   "White": np.array(white_HOLC_per),
   "Other": np.array(other_HOLC_per),
   "Black": np.array(black_HOLC_per),
   "Asian": np.array(asian_HOLC_per),
   "Hispanic": np.array(hispanic_HOLC_per)
}
# Bars on this graph looking kind of wide right now, maybe lower this number
# a bit.
width = 0.5

# Generate the first plot.
fig1, ax1 = plt.subplots()
bottom = np.zeros(4)

# This is a bar graph.
for ethnicity, weight_count in weight_counts_num.items():
   p = ax1.bar(grades, weight_count, width, label = ethnicity, bottom = bottom)
   bottom += weight_count

# Set title and legend orientation, and save plot as `.png` file.
ax1.set_title("Demographics in HOLC Areas (Millions)")
ax1.legend(loc = "upper right")
plt.savefig('holc-num.png', dpi = 300)

# Generate the second plot, same routine as above.
fig2, ax2 = plt.subplots()
bottom = np.zeros(4)

for ethnicity, weight_count in weight_counts_per.items():
   p = ax2.bar(grades, weight_count, width, label = ethnicity, bottom = bottom)
   bottom += weight_count

ax2.set_title("Demographics in HOLC Areas (%)")
ax2.legend(loc = "upper right")
plt.savefig('holc-per.png', dpi = 300)
