import numpy as np

p = np.loadtxt('input8.txt',dtype='str',delimiter=' ')
ndigits = np.char.str_len(p)
nlines, digits = p.shape
k = 0
for i in range(0, nlines):
   for j in range(1, 5):
      if ndigits[i,-j] in {2, 3, 4 , 7}:
         k = k  + 1

print(k)