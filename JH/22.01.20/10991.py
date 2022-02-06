N = int(input())
for i in range(1, N+1):
  '''star = ''
  for j in range(1, i+1):
    star = star + '* '
  #  star = '* '*i
    '''
  print(' '*(N-i)+'* '*i)
  
  # 새로 변수 쓸 필요 없이! 바로 '* '을 곱해서 출력 가능.