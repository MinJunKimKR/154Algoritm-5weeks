import sys

n = int(input())
inputList = list(map(int, sys.stdin.readline().split()))
print(min(inputList), max(inputList))

# 입력을 리스트로 만들 때 list comprehension 사용 가능
# [ int(x) for x in sys.stdin.read().split() ]
# sys.stdin.read().split() : 리턴 값이 range()처럼 반환