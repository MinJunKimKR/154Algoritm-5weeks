# 1:40 -> 2:10
# 1:45 [Success]
S = input()
pre_s = []
for i in range(len(S)):
    s = ''.join(S[i:])
    pre_s.append(s)

pre_s.sort()
for s in pre_s:
    print(s)
