import sys

li = sys.stdin.readlines()[1:] # 테스트케이스부터 여러줄 입력받음

li.sort(key=lambda x: int(x.split()[0])) # 앞자리(x) 정렬
li.sort(key=lambda x: int(x.split()[1])) 
# 뒷자리 (y)정렬하며 앞도 바뀜
# 정렬은 무조건 int()로 감싸줘야함!!

print(''.join(li))

'''
n = int(sys.stdin.readline())

ls = []
for i in range(n):
  [y, x] = map(int, sys.stdin.readline().split())
  ls.append([x, y])
ls.sort()

for i in range(n):
  print(ls[i][1], ls[i][0])'''