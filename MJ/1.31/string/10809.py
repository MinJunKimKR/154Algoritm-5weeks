# 12:42 ->1:12
# 12:47 [Success]

askii_a = ord('a')
words = list(input())
alpa = [-1] * 26

for i in range(len(words)):
    idx = ord(words[i])-askii_a
    if alpa[idx] == -1:
        alpa[idx] = i
for a in alpa:
    print(a, end=' ')
