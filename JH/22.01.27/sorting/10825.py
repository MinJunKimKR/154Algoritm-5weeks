import sys
input = sys.stdin.readline # input()으로 사용 가능

def parse_input(x):
  name, kor, eng, math = x.split()
  kor, eng, math = int(kor), int(eng), int(math)
  return -kor, eng, -math, name #튜플로 리턴

N = int(input())

lst = [parse_input(input()) for i in range(N)] 
# 튜플을 담고 있는 배열


print(*map(lambda x:x[3], sorted(lst)), sep='\n')

"""
li = sys.stdin.readlines()[1:] # 테스트케이스부터 여러줄 입력받음

li.sort(key=lambda x: str(x.split()[0]))
li.sort(key=lambda x: int(x.split()[3]), reverse=True)
li.sort(key=lambda x: int(x.split()[2]))
li.sort(key=lambda x: int(x.split()[1]), reverse=True)"""
#print('\n'.join(map(lambda x: x.split()[0], li))) 
