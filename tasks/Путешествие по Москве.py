import math

xa, ya, xb, yb = list(map(int, input().split()))
ra = (xa ** 2 + ya ** 2) ** 0.5
rb = (xb ** 2 + yb ** 2) ** 0.5
min_r = min(ra, rb)
alpha = math.atan2(ya, xa)
beta = math.atan2(yb, xb)
x = abs(beta - alpha)
c = min_r * x
res = (max(rb, ra) - min(ra, rb)) + c
print(min(res, (rb + ra)))
