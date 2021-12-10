import statistics as stat

with open("input10.txt") as f:
    data = [x.strip() for x in f.readlines()]

score = {')': 1, ']': 2, '}': 3, '>': 4}
closing = {'' : '', '(': ')', '[': ']', '<': '>', '{': '}'}
opening = ['(', '[', '<', '{']

def syntaxcheck(line, last, current):
    if len(line) == current: # out of data
        sc = [score[closing[x]] for x in line[::-1]]
        s = 0
        f = lambda x, y : 5*x + y
        for k in sc:
            s = f(s, k)
        ret = s
    elif line[current] in opening: # open new one
        ret = syntaxcheck(line, last + 1, current + 1)
    elif line[current] == closing[line[last]]: # close one
        strip = line[0:last] + line[current + 1::]
        ret = syntaxcheck(strip, last - 1, current - 1)
    else: # wrong character
        ret = -1
    return ret

s = [x for x in [syntaxcheck(line, 0, 1) for line in data]]
answer = stat.median([p for p in s if p > -1])

print(answer)