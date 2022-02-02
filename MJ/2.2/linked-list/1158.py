# 11:42 -> 12:12
# 12:10 [success]
from collections import deque

N, K = list(map(int, input().split()))

left = deque([i for i in range(1, N+1)])
right = deque([])
result = []
while len(left)+len(right) > 0:
    for _ in range(1, K):
        if len(left) == 0:
            left, right = right, left
        right.append(left.popleft())

    if len(left) == 0:
        left, right = right, left
    result.append(left.popleft())

print('<', end='')
for i in range(len(result)):
    if i != len(result)-1:
        print(result[i], end=', ')
        continue
    print(result[i], end='')
print('>', end='')


# N,K = map(int,input().split())
# arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

# answer = []   # 제거된 사람들을 넣을 배열
# num = 0  # 제거될 사람의 인덱스 번호

# for t in range(N):
#     num += K-1
#     if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
#         num = num%len(arr)

#     answer.append(str(arr.pop(num)))
# print("<",", ".join(answer)[:],">", sep='')
