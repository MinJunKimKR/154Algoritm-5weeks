#1517
#분할정복
#플레5

#bubble sort는 n^2의 시간복잡도를 가지기 때문에 
#nlogn의 시간복잡도가 소요되는 merge sort를 이용해야함.
#merge sort를 이용하는데 swap 횟수를 어떻게 구하지?
#merge sort를 이용하기 때문에 분할정복이군아..!

def merge_sort(start,end):
    global cnt
    if start<end:
        mid=(start+end)//2
        merge_sort(start,mid)
        merge_sort(mid+1,end)
    
        a=start
        b=mid+1
        
        tmp=[]
        while a<=mid and b<=end:
            if arr[a]<=arr[b]:
                tmp.append(arr[a])
                a+=1
            else:
                tmp.append(arr[b])
                b+=1
                cnt+=(mid-a+1) #현재 a배열의 길이.
    
        if a<=mid:
            tmp+=arr[a:mid+1]
        if b<=end:
            tmp+=arr[b:end+1] #남은 요소 합치기.
        
        for i in range(len(tmp)):
            arr[start+i]=tmp[i] #원배열에 합치기(재귀방식이므로)
        
cnt=0
n=int(input())
arr=list(map(int,input().split()))
merge_sort(0,n-1)
print(cnt)


    


    
