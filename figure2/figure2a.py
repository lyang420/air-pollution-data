from utils import init
from utils import calc_pwm_diff

import matplotlib.pyplot as plt

df = init()

hispanic = calc_pwm_diff(df, 'Hispanic', 'NO2')
asian = calc_pwm_diff(df, 'Asian', 'NO2')
black = calc_pwm_diff(df, 'Black', 'NO2')
total = calc_pwm_diff(df, 'Total', 'NO2')
white = calc_pwm_diff(df, 'White', 'NO2')
axes = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
l1 = ax.plot(axes, hispanic, 'g--', label = 'Hispanic')
l2 = ax.plot(axes, asian, 'b:', label = 'Asian')
l3 = ax.plot(axes, black, 'm-', label = 'Black')
l4 = ax.plot(axes, total, 'k-', label = 'Total')
l5 = ax.plot(axes, white, 'm--', label = 'White')
ax.set_ylim(-3, 1.5)
ax.set_title('Intraurban NO2 Difference')
ax.legend()
plt.savefig('figure2a.png', dpi = 300)
