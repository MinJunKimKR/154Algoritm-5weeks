n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

if n % 2 == 1: #
    print(("R"*(m-1)+"D"+"L"*(m-1)+"D") * (n//2) + "R"*(m-1))
elif m % 2 == 1:
    print(("D"*(n-1)+"R"+"U"*(n-1)+"R") * (m//2) + "D"*(n-1))
elif n%2==0 and m%2==0:
    lowest = 1001 #가장 작은 값을 찾기 위해
    lowPosition = [-1,-1]
    for i in range(n):
        if i % 2 == 0:
            for j in range(1,m,2):
                if lowest > arr[i][j]:
                    lowest = arr[i][j]
                    lowPosition = [i,j]
        else:
            for k in range(0,m,2):
                if lowest > arr[i][k]:
                    lowest = arr[i][j]
                    lowPosition = [i,k]
    result = ("D"*(n-1)+"R"+"U"*(n-1)+"R")*(lowPosition[1]//2)
    x = 2 * (lowPosition[1]//2)+1
    y = 0
    xbound = 2*(lowPosition[1] //2) + 1
    while x != xbound or y != n-1:
        if x < xbound and [y,xbound] != lowPosition:
            x+=1
            result += "R"
        elif x == xbound and [y,xbound-1] != lowPosition:
            x-=1
            result += "L"
        if y != n-1:
            y+=1
            result+="D"

    result += ('R' + 'U' * (n - 1) + 'R' + 'D' * (n - 1)) * ((m - lowPosition[1] - 1) // 2)


