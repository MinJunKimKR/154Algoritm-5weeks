# 10:28 -> 10:58
# 10:55 [success]
N, B = input().split()
N = list(N)[::-1]
B = int(B)
alpabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
zinsu = {}

for i in range(10):
    zinsu[str(i)] = i

for i in range(len(alpabet)):
    zinsu[alpabet[i]] = i+10

total = zinsu[N[0]]

for i in range(1, len(N)):
    total += zinsu[N[i]] * pow(B, i)

print(total)
