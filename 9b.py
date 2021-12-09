import numpy as np
from skimage.measure import label

m = np.loadtxt('input9.txt', dtype='str')
nx = len(m[0])
ny = len(m)
height = np.zeros((ny, nx))
for j in range(ny):
   height[j, :] = np.array(list(m[j]), dtype=int)

basins = label(height < 9, connectivity=1)
(unique, counts) = np.unique(basins, return_counts=True)
f = np.sort(counts)
print(f[-4]*f[-3]*f[-2])





