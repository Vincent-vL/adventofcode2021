import numpy as np

paths = np.loadtxt('input12.txt',dtype='str',delimiter='-')
paths = np.concatenate((paths, paths[:, ::-1]))

def countpaths(point, blacklist):
    k = 0
    if blacklist[point]:
        k = 0
    elif point == 'end':
        k = 1
    else:
        if point.islower():
            blacklist[point] = True
        newpaths = np.argwhere(paths[:,0] == point)
        if len(newpaths) > 0:
            for p in newpaths:
                k += countpaths(paths[p,1][0], blacklist.copy())
    return k

blacklist = {}
for p in paths:
    blacklist[p[0]] = False
s = countpaths('start', blacklist)
print (s)