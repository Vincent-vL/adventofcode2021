import numpy as np

p = np.int32(np.genfromtxt('input7.txt',delimiter=','))
costs = np.inf * np.ones(p.max() - p.min() + 1)
for i in range(min(p), max(p) + 1):
   n = np.abs(p-i)
   costs[i] = int(sum(n*(n+1)/2)) # sum a gaussian summation

print(int(costs.min()))