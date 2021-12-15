import numpy as np

with open("input14.txt") as f:
    data = [x for x in f.readlines()]
word = data[0].strip()
wordchars = [w for w in word]
rules = [x.strip().split('->') for x in data[2:len(data)]]

insertname = {} # insertions dict
charname = {} # char
charid = {} # char number
for r in rules:
    insertname[r[0].strip()] = r[1].strip()

n = 0
m = 41
d = [x[1] for x in insertname]
for j in d:
    if j not in charname:
        charname[j] = 0
for j in charname:
    charname[j] = n
    charid[n] = j
    n += 1

map = np.zeros([n, n, m], dtype = np.int64)
for w in range(len(word)-1):
    map[charname[word[w]], charname[word[w+1]], 0] += 1
for i in range(1, m):
    for x in range(n):
        for y in range(n):
            q = map[x, y, i-1]
            if q > 0:
                z = charname[insertname[charid[x] + charid[y]]]
                map[x, z, i] += q
                map[z, y, i] += q

s = np.sum(map[:,:,-1], axis=0) + np.sum(map[:,:,-1], axis=1)
s[charname[word[0]]] += 1
s[charname[word[-1]]] += 1
s = np.int64(s/2)
print(max(s) - min(s))