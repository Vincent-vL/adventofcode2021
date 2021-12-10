with open("input10.txt") as f:
    data = [x.strip() for x in f.readlines()]

score = {'': 0, ')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
closing = {'' : '', '(': ')', '[': ']', '<': '>', '{': '}'}
opening = ['(', '[', '<', '{']

def syntaxtcheck(line, last, current):
    if len(line) == current: # out of data
        ret = ''
    elif line[current] in opening: # open new
        ret = syntaxtcheck(line, last + 1, current + 1)
    elif line[current] == closing[line[last]]: # close one
        strip = line[0:last] + line[current + 1::]
        ret = syntaxtcheck(strip, last - 1, current - 1)
    else: # wrong chracter
        ret = line[current]
    return ret

k = sum([score[x] for x in [syntaxtcheck(line, 0, 1) for line in data]])

print(k)