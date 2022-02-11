#10610
#실버5
#그리디

arr=list(map(int,input())) #리스트로 입력받음

arr.sort(reverse=True)
3
sum=0

for i in arr:
    sum+=i
    
if 0 not in arr or sum%3!=0:
    print(-1)
else: #모든자리의 합이 3의 배수이고 마지막자리가 0이면 30의 배수!
    print(''.join(map(str,arr)))
        


