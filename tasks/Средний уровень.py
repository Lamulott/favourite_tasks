n = int(input())
s = list(map(int, input().split()))
sum_n = [0]
sum_till_n = 0
for i in s:
    sum_till_n += i
    sum_n.append(sum_till_n)
d = []
for st in range(len(s)):
    scores = s[st]
    x1 = abs(scores * st) - sum_n[st]
    x2 = (sum_n[-1] - sum_n[st + 1]) - abs((scores * (len(s) - st - 1)))
    d.append(abs(x1 + x2))
print(*d)
