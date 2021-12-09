import numpy as np

m = np.loadtxt('input9.txt', dtype='str')
nx = len(m[0])
ny = len(m)
height = np.zeros((ny, nx))
for j in range(ny):
   height[j, :] = np.array(list(m[j]), dtype=int)

cnt = np.zeros((ny, nx))
cnt[:,0] = 1
cnt[:,-1] = 1
cnt[0, :] = 1
cnt[-1, :] = 1
cnt[0,0] = 2
cnt[0,-1] = 2
cnt[-1, 0] = 2
cnt[-1, -1] = 2

cnt[0:ny-1, 0:nx] += height[0:ny-1, 0:nx] < height[1:ny,0:nx]
cnt[1:ny, 0:nx] += height[1:ny, 0:nx] < height[0:ny-1,0:nx]
cnt[0:ny, 0:nx-1] += height[0:ny, 0:nx-1] < height[0:ny,1:nx]
cnt[0:ny, 1:nx] += height[0:ny, 1:nx] < height[0:ny,0:nx-1]

risk = sum((1 + height)[cnt == 4])

print(risk)



