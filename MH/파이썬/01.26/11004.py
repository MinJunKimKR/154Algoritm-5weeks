#k번째 수

a,b = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
print(arr[b-1])