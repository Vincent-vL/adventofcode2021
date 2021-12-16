from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import dok_matrix
import numpy as np

data = np.loadtxt('input15.txt', dtype='str')
nx = len(data[0])
ny = len(data)
maze = np.zeros((ny, nx))
for j in range(ny):
    maze[j, :] = np.array(list(data[j]), dtype=int)

bigmap = np.zeros((5*ny, 5*nx))
bigmap[0:nx, 0:ny] = maze
for y in range(5):
    bigmap[y*nx:y*nx+ny,0:nx] = ((y+bigmap[0:ny,0:nx]-1 ) % 9) + 1
for x in range(5):
    bigmap[0:nx*ny,x*ny:x*ny+nx] = ((x+bigmap[0:nx*ny,0:nx]-1 ) % 9)+1
nx *= 5
ny *= 5

m = nx*ny
sparsemap = dok_matrix((m, m), dtype=np.int32)
for x in range(nx):
    for y in range(ny):
        if x > 0:
            sparsemap[y*nx+x-1, y*nx+x] = bigmap[x, y]
        if x < nx -1:
            sparsemap[y * nx + x + 1, y * nx + x] = bigmap[x, y]
        if y > 0:
            sparsemap[(y-1) * nx + x, y * nx + x] = bigmap[x, y]
        if y < ny -1:
            sparsemap[(y + 1) * nx + x, y * nx + x] = bigmap[x, y]

graph = csr_matrix(sparsemap)
dist_matrix, predecessors = dijkstra(csgraph=graph, directed=True, indices=0, return_predecessors=True)
print(dist_matrix[-1])
