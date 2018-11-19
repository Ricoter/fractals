import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# returns coordinates on circle edge
def pos(N,array):
    return np.array([np.cos(array*(2*np.pi)/N), np.sin(array*(2*np.pi)/N)]).T

# lines, points
L, N = 500, 500
a = np.arange(L)

# figure, axis
fig= plt.figure()
ax = plt.axes(xlim=(-1,1), ylim=(-1, 1))

# remove frame
ax.patch.set_visible(False)
ax.axis('off')

# background color
fig.patch.set_facecolor('black')

# lines
lines = sum([ax.plot([],[], 'ro-', linewidth=0.2, markersize=0.1) for _ in range(L)], [])

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    b = a*(i+1)/10
    a_pos, b_pos = pos(N,a), pos(N,b)
    for j, line in enumerate(lines):
        x1, y1 = a_pos[j]
        x2, y2 = b_pos[j]
        line.set_data((x1,x2),(y1,y2))
    return lines


anim = animation.FuncAnimation(fig, animate, init_func=init, 
                               frames=1000, interval=1, blit=True)

anim.save('mod_circle.mp4', fps=100, savefig_kwargs={'facecolor':'black'})
plt.show()
