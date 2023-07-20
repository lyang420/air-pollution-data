from utils import init
from utils import calc_percent
from utils import collect_pop

import matplotlib.pyplot as plt
import numpy as np

df = init()

white = collect_pop(df, 'White')
other = collect_pop(df, 'Other')
black = collect_pop(df, 'Black')
asian = collect_pop(df, 'Asian')
hispanic = collect_pop(df, 'Hispanic')

num_data = [white, other, black, asian, hispanic]

A_total = sum(x[0] for x in num_data)
B_total = sum(x[1] for x in num_data)
C_total = sum(x[2] for x in num_data)
D_total = sum(x[3] for x in num_data)

totals = [A_total, B_total, C_total, D_total]

per_data = [calc_percent(white, totals),
            calc_percent(other, totals), 
            calc_percent(black, totals),
            calc_percent(asian, totals),
            calc_percent(hispanic, totals)]

grades = ("A", "B", "C", "D")

weight_counts_num = {
   "White": num_data[0],
   "Other": num_data[1],
   "Black": num_data[2],
   "Asian": num_data[3],
   "Hispanic": num_data[4]
}
weight_counts_per = {
   "White": per_data[0],
   "Other": per_data[1],
   "Black": per_data[2],
   "Asian": per_data[3],
   "Hispanic": per_data[4]
}
# Bars on this graph looking kind of wide right now, maybe lower this number
# a bit.
width = 0.35

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
plt.savefig('figures3a.png', dpi = 300)

# Generate the second plot, same routine as above.
fig2, ax2 = plt.subplots()
bottom = np.zeros(4)

for ethnicity, weight_count in weight_counts_per.items():
   p = ax2.bar(grades, weight_count, width, label = ethnicity, bottom = bottom)
   bottom += weight_count

ax2.set_title("Demographics in HOLC Areas (%)")
ax2.legend(loc = "upper right")
plt.savefig('figures3b.png', dpi = 300)
