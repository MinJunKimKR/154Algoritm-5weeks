n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
#1,2,3,4,5,6,7

answer = []
num = 0

for _ in range(n):
    num+=m-1
    if num >= len(arr):
        num %= len(arr)

    answer.append(str(arr.pop(num)))

print("<",", ".join(answer),">",sep="")
