def isEqual(l, a, b):
    sa = (h[a + l - 1] + h[b - 1] * x[l]) % p
    sb = (h[b + l - 1] + h[a - 1] * x[l]) % p
    return sa == sb


s = input()
n = int(input())
N = len(s)
p = 10 ** 9 + 7
x_ = 257
h = [0] * (N + 1)
x = [0] * (N + 1)
x[0] = 1
s = ' ' + s
for i in range(1, N + 1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p

for _ in range(n):
    l, a, b = map(int, input().split())
    res = isEqual(l, a + 1, b + 1)
    if res:
        print('yes')
    else:
        print('no')
