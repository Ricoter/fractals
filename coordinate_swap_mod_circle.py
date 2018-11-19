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
ax = plt.axes(xlim=(-1.1,1.1), ylim=(-1.1, 1.1))

# lines
lines = sum([ax.plot([],[], 'ro-', linewidth=0.1, markersize=0.1) for _ in range(L)], [])

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    b = a*(i+1)/8
    a_pos, b_pos = pos(N,a), pos(N,b)
    for j, line in enumerate(lines):
        line.set_data(a_pos[j], b_pos[j])
    return lines


anim = animation.FuncAnimation(fig, animate, init_func=init, 
                               frames=100, interval=20, blit=True)

plt.show()
