# 11728번. 배열합치기

import sys

a, b = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
answer_list = a_list + b_list
answer = ' '.join(map(str, sorted(answer_list)))
print(answer)
