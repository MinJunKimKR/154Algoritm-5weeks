import sys
input = sys.stdin.readline
n = int(input())

chk_list = [0] * 10001

for i in range(n):
  x = int(input())
  chk_list[x] = chk_list[x]+1

for i in range(10001):
  if chk_list[i] != 0:
    for _ in range(chk_list[i]):
      print(i)
  
# 딱 필요한 부분만 저장해야 메모리를 절약할 수 있다!!
# 정렬을 하지 않고 구현해본다.
# 입력 데이터가 1000까지니 해당 배열을 만들어본다.

'''
lst = [int(input()) for i in range(n)]
lst.sort()
print(*map(lambda x:x, lst), sep='\n')

lst = sys.stdin.readlines()[1:]

lst.sort(key=lambda x: int(x))
print(''.join(lst))'''