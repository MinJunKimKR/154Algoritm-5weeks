# 3:00 -> 3:30
# 3:11 [Success]

import sys
sys_input = sys.stdin.readline

N = int(input())
docs = {}

for i in range(N):
    key = int(sys_input())
    if docs.get(key) == None:
        docs[key] = 1
    else:
        docs[key] += 1

zip_docs = sorted(list(zip(docs.keys(), docs.values())),
                  key=lambda x: (-x[1], x[0]))
print(zip_docs[0][0])
