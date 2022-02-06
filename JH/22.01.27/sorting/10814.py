import sys

li = sys.stdin.readlines()[1:] # 테스트케이스부터 여러줄 입력받음

li.sort(key=lambda x: int(x.split()[0]))

print(''.join(li))