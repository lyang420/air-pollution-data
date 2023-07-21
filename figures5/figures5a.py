from utils import init
from utils import collect_city_pops

import matplotlib.pyplot as plt

df = init()
data = collect_city_pops(df, 'NO2', False, False)
axis = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
l1 = ax.plot(axis, data[0], 'g-', label = 'Small')
l2 = ax.plot(axis, data[1], 'y-', label = 'Medium')
l3 = ax.plot(axis, data[2], 'r-', label = 'Large')
ax.set_ylim(0, 25)
ax.set_title('Population-Weighted')
ax.legend()
plt.savefig('figures5a.png', dpi = 300)
