#완전탐색

#1476
e,s,m = map(int,input().split())
while(e!=s or s!=m):
    if(e<=s and e<=m):
        e+=15
    elif(s<=e and s<=m):
        s+=28
    else:
        m+=19
print(e)


#1107 내가 진짜 찾고싶었던 기능을 이문제덕에 찾았네
N = int(input())
M = int(input())
if(not M):
    print(min(abs(N-100), len(str(N))))
else:
    broken = input().split()
    #+ - 로만 이동한값
    output = abs(N-100)
    #50만을 9로만 표현하면 99999에서 올라오는게 빠르므로 888888까지만 확인하면됨. 
    #범위에 대한걸 나중에 더 줄일 수 있을듯.
    for num in range(888889):
        for n in str(num):
            if n in broken:
                break
        else:
            output = min(output, abs(num-N) + len(str(num)))
    print(output)








