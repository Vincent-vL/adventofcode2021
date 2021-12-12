import numpy as np

paths = np.loadtxt('input12.txt',dtype='str',delimiter='-')
paths = np.concatenate((paths, paths[:, ::-1]))

def isvalid(blacklist):
    k=0
    for b in blacklist:
        if b != 'start':
            if blacklist[b] > 1:
                k+=1
    if k>1:
        return False
    return True

def countpaths(point, blacklist):
    if not isvalid(blacklist):
        return 0
    k = 0
    if point == 'end':
        k = 1
    elif blacklist[point] > 1:
        k = 0
    else:
        if point.islower():
            blacklist[point] += 1
        newpaths = np.argwhere(paths[:,0] == point)
        for p in newpaths:
            k += countpaths(paths[p,1][0], blacklist.copy())
    return k

blacklist = {}
for p in paths:
    blacklist[p[0]] = 0
blacklist['start'] = 1
s = countpaths('start', blacklist)
print (s)