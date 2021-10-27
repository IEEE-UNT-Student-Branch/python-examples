from matplotlib import pyplot as plt
import numpy as np

fig, axs = plt.subplots( nrows=2, ncols=2 )

# Plot 1 - Bargraph
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
axs[ 0, 0 ].bar( names, values )

# Plot 2 - Scatter plot
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

axs[ 0, 1 ].scatter('a', 'b', c='c', s='d', data=data)
axs[ 0, 1 ].set_xlabel('entry a')
axs[ 0, 1 ].set_ylabel('entry b')


# Plot 3 - Histogram
np.random.seed(19680801)	# Fixing random state for reproducibility

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = axs[ 1, 0 ].hist(x, 50, density=True, facecolor='g', alpha=0.75)

axs[ 1, 0 ].set_xlabel('Smarts')
axs[ 1, 0 ].set_ylabel('Probability')
axs[ 1, 0 ].title.set_text('Histogram of IQ')
axs[ 1, 0 ].axis([40, 160, 0, 0.03])
axs[ 1, 0 ].grid(True)


# Plot 4 - Line Graph
y = np.linspace( 0, 10, num=20 )
x = np.arange( 20 )
axs[ 1, 1 ].plot( x, y, color="magenta", linestyle="dashed", marker="o" )

plt.subplots_adjust(hspace=0.35, wspace=0.35)
plt.suptitle( "PyPlot Examples" )
plt.show()