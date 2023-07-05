from createdf import init

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = init()

df['Asian']    = pd.to_numeric(df['Asian'])
df['Black']    = pd.to_numeric(df['Black'])
df['Hispanic'] = pd.to_numeric(df['Hispanic'])
df['White']    = pd.to_numeric(df['White'])
df['Other']    = pd.to_numeric(df['Other'])

white_HOLC    = [0, 0, 0, 0]
other_HOLC    = [0, 0, 0, 0]
black_HOLC    = [0, 0, 0, 0]
asian_HOLC    = [0, 0, 0, 0]
hispanic_HOLC = [0, 0, 0, 0]
divisor       = 1000000.0

for i in df.index:
   if df['Grade'][i] == 'A':
      white_HOLC[0] += df['White'][i]
      other_HOLC[0] += df['Other'][i]
      black_HOLC[0] += df['Black'][i]
      asian_HOLC[0] += df['Asian'][i]
      hispanic_HOLC[0] += df['Hispanic'][i]
   if df['Grade'][i] == 'B':
      white_HOLC[1] += df['White'][i]
      other_HOLC[1] += df['Other'][i]
      black_HOLC[1] += df['Black'][i]
      asian_HOLC[1] += df['Asian'][i]
      hispanic_HOLC[1] += df['Hispanic'][i]
   if df['Grade'][i] == 'C':
      white_HOLC[2] += df['White'][i]
      other_HOLC[2] += df['Other'][i]
      black_HOLC[2] += df['Black'][i]
      asian_HOLC[2] += df['Asian'][i]
      hispanic_HOLC[2] += df['Hispanic'][i]
   if df['Grade'][i] == 'D':
      white_HOLC[3] += df['White'][i]
      other_HOLC[3] += df['Other'][i]
      black_HOLC[3] += df['Black'][i]
      asian_HOLC[3] += df['Asian'][i]
      hispanic_HOLC[3] += df['Hispanic'][i]

white_HOLC_adjusted = [x / divisor for x in white_HOLC]
other_HOLC_adjusted = [x / divisor for x in other_HOLC]
black_HOLC_adjusted = [x / divisor for x in black_HOLC]
asian_HOLC_adjusted = [x / divisor for x in asian_HOLC]
hispanic_HOLC_adjusted = [x / divisor for x in hispanic_HOLC]

A_total = (white_HOLC[0] + other_HOLC[0] + black_HOLC[0] + asian_HOLC[0] + hispanic_HOLC[0]) * 1.0
B_total = (white_HOLC[1] + other_HOLC[1] + black_HOLC[1] + asian_HOLC[1] + hispanic_HOLC[1]) * 1.0
C_total = (white_HOLC[2] + other_HOLC[2] + black_HOLC[2] + asian_HOLC[2] + hispanic_HOLC[2]) * 1.0
D_total = (white_HOLC[3] + other_HOLC[3] + black_HOLC[3] + asian_HOLC[3] + hispanic_HOLC[3]) * 1.0

white_HOLC_raw = [white_HOLC[0] / A_total, white_HOLC[1] / B_total, white_HOLC[2] / C_total, white_HOLC[3] / D_total]
other_HOLC_raw = [other_HOLC[0] / A_total, other_HOLC[1] / B_total, other_HOLC[2] / C_total, other_HOLC[3] / D_total]
black_HOLC_raw = [black_HOLC[0] / A_total, black_HOLC[1] / B_total, black_HOLC[2] / C_total, black_HOLC[3] / D_total]
asian_HOLC_raw = [asian_HOLC[0] / A_total, asian_HOLC[1] / B_total, asian_HOLC[2] / C_total, asian_HOLC[3] / D_total]
hispanic_HOLC_raw = [hispanic_HOLC[0] / A_total, hispanic_HOLC[1] / B_total, hispanic_HOLC[2] / C_total, hispanic_HOLC[3] / D_total]

white_HOLC_per = [x * 100 for x in white_HOLC_raw]
other_HOLC_per = [x * 100 for x in other_HOLC_raw]
black_HOLC_per = [x * 100 for x in black_HOLC_raw]
asian_HOLC_per = [x * 100 for x in asian_HOLC_raw]
hispanic_HOLC_per = [x * 100 for x in hispanic_HOLC_raw]

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
width = 0.5

fig3_1, ax3_1 = plt.subplots()
bottom = np.zeros(4)

for ethnicity, weight_count in weight_counts_num.items():
   p = ax3_1.bar(grades, weight_count, width, label = ethnicity, bottom = bottom)
   bottom += weight_count

ax3_1.set_title("Demographics in HOLC Areas (Millions)")
ax3_1.legend(loc = "upper right")

plt.savefig('holc-num.png', dpi = 300)

fig3_2, ax3_2 = plt.subplots()
bottom = np.zeros(4)

for ethnicity, weight_count in weight_counts_per.items():
   p = ax3_2.bar(grades, weight_count, width, label = ethnicity, bottom = bottom)
   bottom += weight_count

ax3_2.set_title("Demographics in HOLC Areas (%)")
ax3_2.legend(loc = "upper right")

plt.savefig('holc-per.png', dpi = 300)
