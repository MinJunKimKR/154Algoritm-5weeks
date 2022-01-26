#국영수

num = int(input())
arr = []
for i in range(num):
    a,b,c,d = input().split()
    arr.append((a,int(b),int(c),int(d)))
arr = sorted(arr,key = lambda x:(-x[1],x[2],-x[3],x[0]))
for i in arr:
    print(i[0])