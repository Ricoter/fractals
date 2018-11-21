import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# returns coordinates on circle edge
def pos(N,array,i,j, k, l):
    return np.array([i*np.cos(array*(2*np.pi)/N/5+j/40),k*np.sin(array*(2*np.pi)/N/5 + l/35)]).T

# lines, points
L, N = 1000, 1000
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
lines = sum([ax.plot([],[], 'go-', alpha=0.5, linewidth=0.1, markersize=0.1) for _ in range(L)], [])

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    b = a*(i)/100
    a_pos, b_pos = pos(N,a,np.tanh(i),2*i,np.tanh(1000-i), 234-i), pos(N,b,np.tanh(i), i*2, np.tanh(i-i**2), i)
    for j, line in enumerate(lines):
        x1, y1 = a_pos[j]
        x2, y2 = b_pos[j]
        c = ((i/100)%1+j/len(lines))/2
        line.set_data((x1,x2),(y1,y2))
        line.set_color(((i/100)%1,1-c,c))
    return lines


anim = animation.FuncAnimation(fig, animate, init_func=init, 
                               frames=1000, interval=20, blit=True)

anim.save('mod_circle.mp4', fps=100, savefig_kwargs={'facecolor':'black'})
plt.show()
