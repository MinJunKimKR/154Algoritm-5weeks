#좌표정렬하기

num = int(input())
arr = []
for i in range(num):
    a,b = map(int,input().split())
    arr.append((a,b))
arr = sorted(arr,key = lambda x:(x[0],x[1]))
for i in arr:
    print(i[0],i[1])