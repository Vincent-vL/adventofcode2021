import numpy as np
import matplotlib.pyplot as plt

with open("input13.txt") as f:
    data = [x.strip() for x in f.readlines()]
    points = [data[i].split(',') for i in range(999)]
    folds =  [data[1000+i].split('=') for i in range(12)]

x = [int(p[0]) for p in points]
y = [int(p[1]) for p in points]
nx = max(x)+1
ny = max(y)+1

map = np.zeros((ny, nx))
npoints = len(x)
for i in range(npoints):
    map[y[i], x[i]] = 1

n = len(folds)
for i in range(n):
    ifold = folds[i]
    if ifold[0][-1] == 'x':
        k = int(ifold[1])
        newmap = map[:, 0:k+1]
        a = map[:, k-(nx-k)+1:k+1]
        b = np.fliplr(map[:,k:nx])
        newmap[:, k-(nx-k)+1:k+1] = np.maximum(a, b)
        map = newmap
        nx = k
    elif ifold[0][-1] == 'y':
        k = int(ifold[1])
        newmap = map[0:k + 1, :]
        a = map[k - (ny - k) + 1:k + 1, :]
        b = np.flipud(map[k:ny, :])
        map[k - (ny - k) + 1:k + 1, :] = np.maximum(a, b)
        map = newmap
        # no time left to simplify:
        # map = np.maximum(map[0:k+1, :], np.flipud(map[k+1:ny, :]))
        ny = k

plt.figure()
plt.pcolormesh(np.flipud(newmap))
plt.draw()
plt.show()

s = np.sum(np.sum(newmap[:,:] == 1))
print(s)


