n = int(input())
card = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

hashmap = {}

for i in card:
    if i in hashmap:
        hashmap[i]+=1
    else:
        hashmap[i] = 1

for i in check:
    if i in hashmap:
        print(hashmap[i], end=" ")
    else:
        print(0,end=" ")