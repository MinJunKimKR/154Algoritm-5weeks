'''
n = int(input())
for i in range(n):
  print(i+1)
'''

ran = range(1, int(input())+1) # 1~n까지 리스트
print('\n'.join(map(str,ran)))

# range(): 리스트 리턴
# A.join(B): A 문자열을 B 문자열과 합쳐 준다.
# map(): 여러 개의 매개 변수 반환