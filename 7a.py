import numpy as np

p = np.int32(np.genfromtxt('input7.txt',delimiter=','))
m = np.inf
for i in range(min(p), max(p) + 1):
   cost = sum(np.abs(p-i))
   if cost < m:
       m = cost

print(m)