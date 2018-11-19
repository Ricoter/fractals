import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
# returns coordinates on circle edge
def pos(N,array):
    return np.array([np.cos(array*(2*np.pi)/N), np.sin(array*(2*np.pi)/N)]).T

L, N = 210, 210 # lines, points
a = np.arange(L)

fig= plt.figure()
ax = plt.axes(xlim=(-2,2), ylim=(-2, 2))
#ax.set_xlim((-1,1))
#ax.set_ylim((-1,1))

# lines
lines = sum([ax.plot([],[], 'ro-', linewidth=1, markersize=1) for _ in range(L)], [])

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    b = a*(i+1)
    a_pos, b_pos = pos(N,a), pos(N,b)
    for j, line in enumerate(lines):
        x1, y1 = a_pos[j]
        x2, y2 = b_pos[j]
        line.set_data((x1,x2),(y1,y2))
    return lines

def animate2(i):
    b = a*(i+1)
    a_pos, b_pos = pos(N,a), pos(N,b)
    line.set_data(a_pos, b_pos)
    return line,
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)
plt.show()
#for i in range(0,10):
#    b = a*i
#    a_pos, b_pos = pos(N,a), pos(N,b)
#    plt.gcf().clear()
#    for j in range(L):
#        #frac1 = plt.plot(a_pos[j], b_pos[j], 'ro-', linewidth=0.1, markersize=0.1)
#        x1, y1 = a_pos[j]
#        x2, y2 = b_pos[j]
#        #im = plt.plot((x1,x2),(y1,y2),'ro-',linewidth=0.1, markersize=0.1)
#        im = plt.imshow((x1,x2),(y1,y2),linewidth=0.1, markersize=0.1, animated=True)
# #   f1.append(frac1)
#    f2.append(im)
#
#ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
#                                repeat_delay=1000)
#
#plt.show()
