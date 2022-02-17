n = int(input())
arr = list(map(int,input().split()))
cnt = 0

def mergeSort(start,end):
    global cnt
    if start < end:
        mid = (start+end)//2
        mergeSort(start,mid)
        mergeSort(mid+1,end)

        a = start
        b = mid+1
        tmp = []
        while a <= mid and b <= end:
            if arr[a] <= arr[b]: #맨 앞을 비교한다.
                tmp.append(arr[a])
                a+=1
            else:
                tmp.append(arr[b])
                b+=1
                cnt+=(mid-a+1) #b가 작으면 스와핑 하는 것이므로 개수추가 남은 a
                

        if a <= mid:
            tmp = tmp+arr[a:mid+1]

        if b <= end:
            tmp = tmp+arr[b:end+1]

        for i in range(len(tmp)):
            arr[start+i] = tmp[i]


#https://gaza-anywhere-coding.tistory.com/105
mergeSort(0,n-1)
print(cnt)




