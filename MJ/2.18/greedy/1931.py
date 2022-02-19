# 10:45 ->11:15
# 11:22 [Success]
import sys
sys_input = sys.stdin.readline
N = int(input())

cnt_meeting = 0
table = []
for i in range(N):
    table.append(list(map(int, sys_input().strip().split())))
table = sorted(table, key=lambda x: [x[1], x[0]])
this_time = 0

for times in table:
    if times[0] < this_time:
        continue
    cnt_meeting += 1
    this_time = times[1]
print(cnt_meeting)
