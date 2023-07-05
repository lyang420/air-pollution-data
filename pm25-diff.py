# This script aims to create a plot displaying the adjusted national
# population-weighted distributions of intraurban differences in PM25 levels
# within HOLC-mapped areas at the census block level in line format as seen in
# Figure 2(b).
from createdf import init

import matplotlib.pyplot as plt
import numpy as np

def calculate_pwm(pop, pm25):
   t = ((~np.isnan(pop)) & (~np.isnan(pm25)))
   pop = pop[t]
   pm25 = pm25[t]
   pwm = np.average(pm25, weights = pop)
   return pwm

def calculate_pwm_grade(grade, target, pop, pm25):
   t = ((grade == target) & (~np.isnan(pm25)) & (~np.isnan(pop)))
   grade = grade[t]
   pop = pop[t]
   pm25 = pm25[t]
   pwm = np.average(pm25, weights = pop)
   return pwm

# -----------------------------------------------------------------------------

df = init()

pwm_hispanic_all = calculate_pwm(df['Hispanic'], df['PM25'])
pwm_hispanic_A = calculate_pwm_grade(df['Grade'], 'A', df['Hispanic'], df['PM25'])
pwm_hispanic_B = calculate_pwm_grade(df['Grade'], 'B', df['Hispanic'], df['PM25'])
pwm_hispanic_C = calculate_pwm_grade(df['Grade'], 'C', df['Hispanic'], df['PM25'])
pwm_hispanic_D = calculate_pwm_grade(df['Grade'], 'D', df['Hispanic'], df['PM25'])
h1 = pwm_hispanic_A - pwm_hispanic_all
h2 = pwm_hispanic_B - pwm_hispanic_all
h3 = pwm_hispanic_C - pwm_hispanic_all
h4 = pwm_hispanic_D - pwm_hispanic_all

pwm_asian_all = calculate_pwm(df['Asian'], df['PM25'])
pwm_asian_A = calculate_pwm_grade(df['Grade'], 'A', df['Asian'], df['PM25'])
pwm_asian_B = calculate_pwm_grade(df['Grade'], 'B', df['Asian'], df['PM25'])
pwm_asian_C = calculate_pwm_grade(df['Grade'], 'C', df['Asian'], df['PM25'])
pwm_asian_D = calculate_pwm_grade(df['Grade'], 'D', df['Asian'], df['PM25'])
a1 = pwm_asian_A - pwm_asian_all
a2 = pwm_asian_B - pwm_asian_all
a3 = pwm_asian_C - pwm_asian_all
a4 = pwm_asian_D - pwm_asian_all

pwm_black_all = calculate_pwm(df['Black'], df['PM25'])
pwm_black_A = calculate_pwm_grade(df['Grade'], 'A', df['Black'], df['PM25'])
pwm_black_B = calculate_pwm_grade(df['Grade'], 'B', df['Black'], df['PM25'])
pwm_black_C = calculate_pwm_grade(df['Grade'], 'C', df['Black'], df['PM25'])
pwm_black_D = calculate_pwm_grade(df['Grade'], 'D', df['Black'], df['PM25'])
b1 = pwm_black_A - pwm_black_all
b2 = pwm_black_B - pwm_black_all
b3 = pwm_black_C - pwm_black_all
b4 = pwm_black_D - pwm_black_all

pwm_total_all = calculate_pwm(df['Total'], df['PM25'])
pwm_total_A = calculate_pwm_grade(df['Grade'], 'A', df['Total'], df['PM25'])
pwm_total_B = calculate_pwm_grade(df['Grade'], 'B', df['Total'], df['PM25'])
pwm_total_C = calculate_pwm_grade(df['Grade'], 'C', df['Total'], df['PM25'])
pwm_total_D = calculate_pwm_grade(df['Grade'], 'D', df['Total'], df['PM25'])
t1 = pwm_total_A - pwm_total_all
t2 = pwm_total_B - pwm_total_all
t3 = pwm_total_C - pwm_total_all
t4 = pwm_total_D - pwm_total_all

pwm_white_all = calculate_pwm(df['White'], df['PM25'])
pwm_white_A = calculate_pwm_grade(df['Grade'], 'A', df['White'], df['PM25'])
pwm_white_B = calculate_pwm_grade(df['Grade'], 'B', df['White'], df['PM25'])
pwm_white_C = calculate_pwm_grade(df['Grade'], 'C', df['White'], df['PM25'])
pwm_white_D = calculate_pwm_grade(df['Grade'], 'D', df['White'], df['PM25'])
w1 = pwm_white_A - pwm_white_all
w2 = pwm_white_B - pwm_white_all
w3 = pwm_white_C - pwm_white_all
w4 = pwm_white_D - pwm_white_all

x_ax = ['A', 'B', 'C', 'D']

plt.plot(x_ax, [h1, h2, h3, h4], 'g--')
plt.plot(x_ax, [a1, a2, a3, a4], 'b:')
plt.plot(x_ax, [b1, b2, b3, b4], 'm-')
plt.plot(x_ax, [t1, t2, t3, t4], 'k-')
plt.plot(x_ax, [w1, w2, w3, w4], 'm--')
plt.savefig('pm25-intraurban-diff.png', dpi = 300)
