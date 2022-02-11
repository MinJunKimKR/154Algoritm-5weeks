import sys
sys.setrecursionlimit(10000000)

def dfs(num):
    global result
    check[num] = True
    cycle.append(num)
    number = arr[num]
    if check[number]:
        if number in cycle:
            result+=cycle[cycle.index(number):]
        return
    else:
        dfs(number)


for _ in range(int(input())):
    num = int(input())
    arr = [0]+list(map(int,input().split()))
    check = [False] * (num+1)
    result = []

    for i in range(1,num+1):
        if not check[i]:
            cycle = []
            dfs(i)


    print(num - len(result))