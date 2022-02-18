n,m = map(int,input().split())

# arr = [i for i in range(n,m+1)]
#
# for i in arr:
#     num=0
#     for j in range(1,i+1):
#         if i%j==0:
#             num+=1
#     if num == 2:
#         print(i)

arr = [True]*(m+1)

for i in range(2,int(m**1//2)+1):
    if arr[i]:
        for j in range(i*2,m+1,i):
            arr[j] = False

for i in range(n,m+1):
    if arr[i]:
        print(i)



