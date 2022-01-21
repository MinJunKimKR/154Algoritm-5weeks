N = int(input())
CNT = N*2 
for i in range(1, N):
  print('*'*i+' '*(CNT-i*2)+'*'*i)
for i in range(N, 0, -1):
  print('*'*i+' '*
  (CNT-i*2)+'*'*i)

# 새로운 변수(CNT)를 만들지 않고, 바로 N*2 를 써도 됨.