# 9:50 -> 10:20
# GG
# 10:39[Success]
import sys
sys_input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys_input().strip().split())))
mi_one = 0
zero = 0
one = 0


def devide(x, y, n):
    global mi_one, zero, one
    check = paper[x][y]
    for i in range(n):
        for j in range(n):
            if check != paper[x+i][y+j]:
                check = -2
                break
    n = n//3
    if check == -2:
        devide(x, y, n)
        devide(x, y+n, n)
        devide(x, y+(n*2), n)
        devide(x+n, y, n)
        devide(x+n, y+n, n)
        devide(x+n, y+(n*2), n)
        devide(x+(n*2), y, n)
        devide(x+(n*2), y+n, n)
        devide(x+(n*2), y+(n*2), n)
    elif check == 0:
        zero += 1
    elif check == 1:
        one += 1
    else:
        mi_one += 1


devide(0, 0, N)
print(mi_one)
print(zero)
print(one)
