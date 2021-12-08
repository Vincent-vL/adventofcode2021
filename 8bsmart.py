import numpy as np

displays = np.loadtxt('input8.txt', dtype='str', delimiter=' ')
nlines, ndigits = displays.shape
defaultdigits = ['acdefg', 'eg', 'abcef', 'abceg', 'bdeg', 'abcdg', 'abcdfg', 'aeg', 'abcdefg', 'abcdeg'] #0, 1, 2, ..., 9
weights = np.int32([np.char.count(defaultdigits, chr(digit)) for digit in range(ord('a'), ord('h'))])
hist = np.sum(weights, 1)
ref_ids = [sum(weights[:, j] * hist.T) for j in range(0, 10)]
s = 0
for i in range(0, nlines):
   # compile lookup for this iteration
   h = np.int32([np.char.count(displays[i, 0:10], chr(digit)) for digit in range(ord('a'), ord('h'))])
   hist = np.sum(h, 1)
   # decode and add value for each of the four digits
   for j in range(0, 4):
      weights = np.int32([np.char.count(displays[i, 11+j], chr(digit)) for digit in range(ord('a'), ord('h'))])
      id = sum(hist*weights)
      n = np.argwhere(ref_ids == id)
      s = s + n * 10 ** (3 - j)

print(s)



