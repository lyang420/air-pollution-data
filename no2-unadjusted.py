# This script aims to create a plot displaying the unadjusted national
# population-weighted distributions of NO2 levels within HOLC-mapped areas at
# the census block level as seen in Figure 1(a).
from createdf import init

import numpy as np
import statistics as stat

df = init()

no2_A         = []
no2_B         = []
no2_C         = []
no2_D         = []
no2_white     = []
no2_other     = []
no2_black     = []
no2_asian     = []
no2_hispanic  = []

for i in df.index:
   if df['Grade'][i] == 'A':
      no2_A += (df['Total'][i] * [df['NO2'][i]])
   if df['Grade'][i] == 'B':
      no2_B += (df['Total'][i] * [df['NO2'][i]])
   if df['Grade'][i] == 'C':
      no2_C += (df['Total'][i] * [df['NO2'][i]])
   if df['Grade'][i] == 'D':
      no2_D += (df['Total'][i] * [df['NO2'][i]])
   if df['White'][i] > 0:
      no2_white += (df['White'][i] * [df['NO2'][i]])
   if df['Other'][i] > 0:
      no2_other += (df['Other'][i] * [df['NO2'][i]])
   if df['Black'][i] > 0:
      no2_black += (df['Black'][i] * [df['NO2'][i]])
   if df['Asian'][i] > 0:
      no2_asian += (df['Asian'][i] * [df['NO2'][i]])
   if df['Hispanic'][i] > 0:
      no2_hispanic += (df['Hispanic'][i] * [df['NO2'][i]])