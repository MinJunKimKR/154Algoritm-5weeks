# 2:03 -> 2:33
# 2:06 [Success]
import sys
sys_input = sys.stdin.readline

N = int(input())
score = [sys_input().split() for _ in range(N)]

sorted_score = sorted(
    score, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for score in sorted_score:
    print(score[0])
