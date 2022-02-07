#11728
#실버5
#간단한 문제지만 분할정복으로 어떻게 풀징?
#분할정복에는 대표적으로 이분탐색, merge sort,quick sort등이 있음.
#이문제는 merge sort,quick sort등으로 풀수 있겠군!

#merge sort: 하나의 그룹의 개수가 1이 될때까지 분할 진행.
#합칠때마다 정렬을 하면서 합침.
#합치는 알고리즘: 저장할 배열을 따로 선언하여 정렬된 결과를 저장.

n,m=map(int,input().split())


a=list(map(int,input().split()))
b=list(map(int,input().split()))

answer=[] #합쳐서 정렬된 결과를 담을 배열

a_idx=0
b_idx=0
while(a_idx!=n or b_idx!=m):
    if a_idx==n:
        answer.append(b[b_idx])
        b_idx+=1
    elif b_idx==m:
        answer.append(a[a_idx])
        a_idx+=1
    else:
        if a[a_idx]<b[b_idx]:
            answer.append(a[a_idx])
            a_idx+=1
        else:
            answer.append(b[b_idx])
            b_idx+=1

print(*answer)
