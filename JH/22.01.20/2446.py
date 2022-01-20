N = int(input())
for i in range(N, 0, -1):
  print(' '*(N-i)+'*'*(i*2-1))
for i in range(2, N+1):
  print(' '*(N-i)+'*'*(i*2-1))