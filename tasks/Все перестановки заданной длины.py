from itertools import permutations as p

n = int(input())
l = [i for i in range(1, n + 1)]
res = list(p(l, r=n))
for i in res:
    print(*i, sep='', end='\n')
