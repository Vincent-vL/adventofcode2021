import numpy as np

def strinstr(a, b):
   # return True when a is covered by b
   ret = True
   for i in range(0, len(a)):
      if a[i] not in b:
         ret = False
   return ret

displays = np.loadtxt('input8.txt',dtype='str',delimiter=' ')
numbers = np.zeros(10)
ndigits = np.char.str_len(displays)
nlines, digits = displays.shape
nlinesdict = {2:1, 3:7, 4:4, 7:8}
s = 0

# Sort each character string to be able to compare data
for i in range(0, nlines):
   for j in range(0, 15):
      sorted_characters = sorted(displays[i,j])
      displays[i,j] = "".join(sorted_characters)

# Process all four-segment displays
for i in range(0, nlines):
   # Find digits 7 and 4
   for j in range(0, 10):
      if ndigits[i,j] == 3:
         seven = displays[i,j]
      if ndigits[i, j] == 4:
         four = displays[i, j]

   # Fill lookup table for digits 1, 7, 4, 8 and for 6 and 9 and 0
   for j in range(0, 10):
      if ndigits[i,j] in {2, 3, 4, 7}:
         numbers[j] = nlinesdict[ndigits[i,j]]
      if ndigits[i,j] == 6:
         if strinstr(seven, displays[i, j]):
            if strinstr(four, displays[i, j]):
               numbers[j] = 9
            else:
               numbers[j] = 0
         else:
             numbers[j] = 6
             six = displays[i, j]

   # Finally handle digits 2, 3 or 5
   for j in range(0, 10):
      if ndigits[i,j] == 5:
         if strinstr(seven, displays[i, j]):
            numbers[j] = 3
         elif strinstr(displays[i, j], six):
               numbers[j] = 5
         else:
            numbers[j] = 2

   # lookup the numbers and add their values to the total sum s
   for j in range(0, 4):
      for jlookup in range(0, 10):
         if displays[i, 11+j] == displays[i, jlookup]:
            k = numbers[jlookup]
            break
      s = s + k * 10**(3-j)

print(s)