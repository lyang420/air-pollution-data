from utils import init
from utils import calc_pwm_diff

import matplotlib.pyplot as plt

df = init()

hispanic = calc_pwm_diff(df, 'Hispanic', 'PM25')
asian = calc_pwm_diff(df, 'Asian', 'PM25')
black = calc_pwm_diff(df, 'Black', 'PM25')
total = calc_pwm_diff(df, 'Total', 'PM25')
white = calc_pwm_diff(df, 'White', 'PM25')
axes = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
l1 = ax.plot(axes, hispanic, 'g--', label = 'Hispanic')
l2 = ax.plot(axes, asian, 'b:', label = 'Asian')
l3 = ax.plot(axes, black, 'm-', label = 'Black')
l4 = ax.plot(axes, total, 'k-', label = 'Total')
l5 = ax.plot(axes, white, 'm--', label = 'White')
ax.set_ylim(-0.4, 0.2)
ax.set_title('Intraurban PM2.5 Difference')
ax.legend()
plt.savefig('figure2b.png', dpi = 300)
