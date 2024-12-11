import pandas as pd

with open('1_input.txt') as e:
    d = e.readlines()

l_1 = []
l_2 = []

for l in d:
    vals = l.split('   ')
    l_1.append(int(vals[0]))
    l_2.append(int(vals[1].replace('\n', '')))

l_1.sort()
l_2.sort()

a = sum([abs(v1 - v2) for v1,v2 in zip(l_1, l_2)])

print(a)

