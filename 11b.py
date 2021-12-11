import numpy as np
from scipy import signal

data = np.loadtxt('input11.txt', dtype='str')
nx = len(data[0])
ny = len(data)
map = np.zeros((ny, nx))
for j in range(ny):
   map[j, :] = np.array(list(data[j]), dtype=int)

g = np.asarray([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])

def neighbours(x, y, map):
    mask = map * 0
    mask[x, y] = 1
    conv = signal.convolve2d(mask, g) > 0
    return conv[1:-1, 1:-1]

def countflash(map):
    map += 1
    flashmap = np.zeros((ny, nx))
    while np.sum(np.sum(map > 9))> 0:
        f = [x for x in np.argwhere(map > 9)]
        p = f[0]
        grow = neighbours(p[0], p[1], map)
        map[grow] += 1
        flashmap[p[0], p[1]] = 1
        map[flashmap == 1] = 0

    ksum = np.sum(np.sum(map == 0))
    return ksum, map

i = 0
while np.sum(np.sum(map)) > 0:
    i+=1
    s, map = countflash(map)

print(i)
