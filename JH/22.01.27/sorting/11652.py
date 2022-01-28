import sys
input = sys.stdin.readline

n = int(input())

dic = {}
for i in range(n):
  x = int(input())
  if x in dic:
    dic[x] += 1
  else:
    dic[x] = 1

print(dic.items())
print(sorted(dic.items()))

print(sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0])

# 딕셔너리 형태는 입력값을 키값으로 바로 접근 가능해서 유용하다.
# 딕셔너리.items(): 리스트 튜플 형태로 변환
# 변수앞에 -를 붙이면 내림차순 처럼 정렬된다.