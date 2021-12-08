import numpy as np

displays = np.loadtxt('input8.txt', dtype='str', delimiter=' ')

alldigits = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alldisplays = ['acdefg', 'eg', 'abcef', 'abceg', 'bdeg', 'abcdg', 'abcdfg', 'aeg', 'abcdefg', 'abcdeg'] # = 0, 1, .., 9
allsegments = np.int32([np.char.count(alldisplays, digit) for digit in alldigits])
histogram = np.sum(allsegments, 1)
digit_ids = [sum(allsegments[:, j] * histogram.T) for j in range(0, 10)]

s = 0
nlines, ndigits = displays.shape
for i in range(0, nlines):
   # compile lookup for this iteration
   isegments = np.int32([np.char.count(displays[i, 0:10], digit) for digit in alldigits])
   ihistogram = np.sum(isegments, 1)
   # decode and add value for each of the four digits
   for j in range(0, 4):
      jsegments = np.int32([np.char.count(displays[i, 11+j], digit)  for digit in alldigits])
      id = sum(ihistogram*jsegments)
      k = int(np.argwhere(digit_ids == id))
      s = s + k * 10 ** (3 - j)

print(s)



