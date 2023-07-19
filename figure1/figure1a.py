from utils import init
from utils import collect_data

import matplotlib.pyplot as plt

df = init()

# Although plot customization details may appear mostly similar across scripts,
# I chose not to abstract them, since the number of small details (e.g.,
# dimensions, labels, etc.) are too great and too subtle.
data = collect_data(df, 'NO2', False)
labels = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']
colors = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue', 'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']

fig, ax = plt.subplots(nrows = 1, ncols = 1)
plot = ax.boxplot(data, labels = labels, patch_artist = True, showfliers = False, vert = True, whis = 0)

ax.set_title('Unadjusted: National Aggregation')
ax.set_ylim(0, 25)
for median in plot['medians']:
   median.set_color('black')
for patch, color in zip(plot['boxes'], colors):
   patch.set_facecolor(color)

plt.savefig('figure1a.png', dpi = 300)
