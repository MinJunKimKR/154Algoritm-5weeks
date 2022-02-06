#나이순 정렬
num = int(input())
arr = []
for i in range(num):
    a,b = input().split()
    arr.append((int(a),b))
arr = sorted(arr,key = lambda x:x[0])

for i in arr:
    print(i[0],i[1])

