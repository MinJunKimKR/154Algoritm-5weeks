#카드

n = int(input())
d = {}
for i in range(n):
    num = int(input())
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

d = sorted(d.items(),key = lambda x:(-x[1],x[0]))
print(d[0][0])


