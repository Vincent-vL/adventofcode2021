import numpy as np

p = np.int32(np.genfromtxt('input7.txt',delimiter=','))
cost = np.inf
for i in range(min(p), max(p) + 1):
   n = np.abs(p-i)
   cost = np.minimum(cost, sum(n * (n + 1) / 2))

print(int(cost))
