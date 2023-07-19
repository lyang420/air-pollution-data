from utils import init
from utils import collect_data

import matplotlib.pyplot as plt

df = init()

data = collect_data(df, 'PM25', True)
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']
colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue', 'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']

fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)
ax.set_title('Adjusted: Intraurban Variation')
ax.set_ylim(-0.8, 0.6)
for median in plot['medians']:
   median.set_color('black')
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

plt.savefig('figure1d.png', dpi = 300)
