import collections

with open("input14.txt") as f:
    data = [x for x in f.readlines()]
word = data[0].strip()
wordchars = [w for w in word]
rules = [x.strip().split('->') for x in data[2:len(data)]]

ins = {}
for r in rules:
    ins[r[0].strip()] = r[1].strip()

for i in range(10):
    insertions = [ins[word[j:j+2]] for j in range(len(word)-1)]
    for j in range(1, len(word)):
        wordchars.insert(2*j-1, insertions[j-1])
    word = ''.join(wordchars)

a = collections.Counter(word).most_common()
print(a[0][1] - a[-1][1])