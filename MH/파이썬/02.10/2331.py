a,p = map(int,input().split())
arr = [a]
while True:
    tmp = 0
    for i in str(arr[-1]):
        tmp += int(i) ** p

    if tmp in arr:
        break
    arr.append(tmp)

print(arr.index(tmp))

