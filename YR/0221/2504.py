#2504
#실버2
#stack 이용

st=input() #문자열 입력받기
stack=[] 

temp=1
res=0

for i in range(len(st)):
    if st[i]=='(':
        stack.append(st[i])
        temp*=2
    elif st[i]=='[':
        stack.append(st[i])
        temp*=3
    elif st[i]==']':
        if stack[-1]=='(' or not stack:
            res=0
            break
        if st[i-1]=='[':
            res+=temp
        temp//=3
        stack.pop()
    elif st[i]==')':
        if stack[-1]=='[' or not stack:
            res=0
            break
        if st[i-1]=='(':
            res+=temp
        temp//=2
        stack.pop()
        


print(res)
