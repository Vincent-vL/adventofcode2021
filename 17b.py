import numpy as np
import matplotlib.pyplot as plt

with open("input17.txt") as f:
    data = [x for x in f.readlines()]
word = data[0].strip().split(':')[1].split(',')
[[xmin, xmax], [ymin, ymax]] = [w.split('=')[1].split('..') for w in word]
xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)

def ishit(dx, dy):
    x=0
    y=0
    maxheight = ymin
    while x <= xmax and y >= ymin:
        x = x+dx
        y = y+dy
        maxheight = max(y, maxheight)
        dx = dx-1 if dx>0 else dx+1 if dx<0 else 0
        dy = dy-1
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return 1
    return 0

# Using matplotlib define search interval
nx = 100
ny = 1000
m = np.zeros([nx, 2*ny])
for i in range(nx):
    for j in range(-ny, ny):
        m[i,ny+j] = ishit(i,j)
print(np.sum(np.sum(m)))
plt.pcolormesh(m)
plt.draw()
plt.show()
