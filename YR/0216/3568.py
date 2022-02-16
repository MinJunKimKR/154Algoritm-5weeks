#실버4
#3568

#변수를 뒤집을 때 대괄호 처리해줘야..

arr=list(map(str,input().split()))

ty=arr[0]
arr=arr[1:]


for a in arr:
    a=a[:-1] #,이나 ; 잘라내기
    
    s=len(a)+1 # s초기화
    for i in range(len(a)):
        if a[i]=='[':
            s=i
            break
        if a[i]=='*':
            s=i
            break
        if a[i]=='&':
            s=i
            break
    name=a[:s]
    variable=a[s:]
    
    variable=variable[::-1] #뒤집기
    
    variable=variable.replace("][","[]") #replace 사용(문자열 대체)
            
    print(ty+variable,end=' ')
    print(name+';')
