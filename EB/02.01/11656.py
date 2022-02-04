# 11656. 접미사 배열

import sys

line = sys.stdin.readline().rstrip('\n')
lst = []


for i in range(len(line)):
   lst.append(line[i:])


for s in sorted(lst):
    print(s)
