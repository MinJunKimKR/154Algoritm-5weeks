n = int(input())
arr_pos=[]
arr_neg=[]
max_sum = 0

for i in range(n):
    a = int(input())
    if a > 1:
        arr_pos.append(a)
    elif a==1:
        max_sum+=1 #1은 무조건 더하는게 최댓값
    else:
        arr_neg.append(a)

arr_neg.sort()
arr_pos.sort(reverse=True)

if len(arr_pos) % 2 == 0: #양수가 짝수개라면 두개씩 곱한다.
    for i in range(0,len(arr_pos),2):
        max_sum+=arr_pos[i]*arr_pos[i+1]
else:
    for i in range(0,len(arr_pos)-1,2):
        max_sum+=arr_pos[i]*arr_pos[i+1]
    max_sum += arr_pos[len(arr_pos)-1] #마지막 수는 더해준다.

if len(arr_neg) % 2 == 0: #음수가 짝수개 일 경우 두개씩 곱해준다.
    for i in range(0,len(arr_neg),2):
        max_sum+=arr_neg[i]*arr_neg[i+1]
else:
    for i in range(0,len(arr_neg)-1,2):
        max_sum+=arr_neg[i]*arr_neg[i+1]
    max_sum += arr_neg[len(arr_neg)-1] #마지막 수는 더해준다.

print(max_sum)
