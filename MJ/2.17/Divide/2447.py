# 5:40 -> 6:10
# 6:10 [Success]
N = int(input())
pattern = [[' '] * N for _ in range(N)]


def stars(x, y, n):
    if n == 1:
        pattern[x][y] = '*'
        return
    next = n//3
    for i in range(3):
        stars(x+(next*i), y, next)
    stars(x, y+next, next)
    stars(x+(next*2), y+next, next)
    for i in range(3):
        stars(x+(next*i), y+(next*2), next)


stars(0, 0, N)

for i in range(N):
    for j in range(N):
        print(pattern[i][j], end='')
    print()
