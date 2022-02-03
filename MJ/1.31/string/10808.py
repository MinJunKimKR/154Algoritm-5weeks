# 7:50 -> 8:20
# 7:57 [Success]
askii_a = ord('a')
alpha = [0] * 26

str = list(input())

for s in str:
    idx = ord(s)-askii_a
    alpha[idx] += 1
for i in alpha:
    print(i, end=' ')
