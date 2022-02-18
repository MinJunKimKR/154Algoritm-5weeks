def draw_star(n):
    global Map
    if n == 3:
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1,0,1]
        return

    a = n//3
    draw_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]

n = int(input())
Map = [[0]*n for _ in range(n)]

draw_star(n)

for i in Map:
    for j in i:
        if j==1:
            print('*',end="")
        else:
            print(" ",end="")
    print()

#https://study-all-night.tistory.com/5