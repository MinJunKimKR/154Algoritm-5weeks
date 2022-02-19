# 8:30 -> 9:00
# 9:11 [Success]
N = int(input())
tri = [[' '] * (N*2-1) for _ in range(N)]


def stars(x, y, n):
    if n == 3:
        tri[x][y] = '*'
        tri[x+1][y-1] = tri[x+1][y+1] = '*'
        for i in range(-2, 3):
            tri[x+2][y+i] = '*'
        return
    next = n//2
    stars(x, y, next)
    stars(x+next, y-next, next)
    stars(x+next, y+next, next)


stars(0, N-1, N)

for i in range(len(tri)):
    print(''.join(tri[i]))
