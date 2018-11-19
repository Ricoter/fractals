import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute areas and colors
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

d = ax.line((0,1),(0,2))

plt.show()
#

#circle = plt.Circle((0, 0), 1, color='r')

#fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

#ax.add_artist(circle)

#plt.show()
#fig.savefig('plotcircles.png')


