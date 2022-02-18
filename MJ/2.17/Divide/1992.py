# 5:00 -> 5:30
# 5:12 [Success]
import sys
sys_input = sys.stdin.readline

N = int(input())
quad = []

for _ in range(N):
    quad.append(list(map(int, list(sys_input().strip()))))


def devide(x, y, n):
    checker = quad[x][y]
    for i in range(n):
        for j in range(n):
            if checker != quad[x+i][y+j]:
                checker = -1
                break
    if checker != -1:
        print(checker, end='')
    else:
        n = n//2
        print('(', end='')
        devide(x, y, n)
        devide(x, y+n, n)
        devide(x+n, y, n)
        devide(x+n, y+n, n)
        print(')', end='')


devide(0, 0, N)
