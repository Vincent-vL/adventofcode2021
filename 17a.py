import numpy as np

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
            return maxheight
    return float('-inf')

# Using matplotlib define search interval
nx = 10
ny = 1000
m = np.zeros([nx, ny])
for i in range(nx):
    for j in range(ny):
        m[i,j] = ishit(i,j)
print(int(np.max(m)))
