#1744
#골드4

#수 묶는 규칙을 찾기!


n=int(input())
arr=[]
positivelst=[]
negativelst=[]

result=0

for i in range(n):
    a=(int(input()))
    if a<=0:
        negativelst.append(a)
    elif a==1:
        result+=1
    else:
        positivelst.append(a)



negativelst.sort() #음수는 내림차순
positivelst.sort(reverse=True) #양수는 오름차순



if len(positivelst)%2==0:
    for i in range(0,len(positivelst),2):
        result+=positivelst[i]*positivelst[i+1]
else:
    for i in range(0,len(positivelst)-1,2):
        result+=positivelst[i]*positivelst[i+1]
    result+=positivelst[-1]
    
if len(negativelst)%2==0:
    for i in range(0,len(negativelst),2):
        result+=negativelst[i]*negativelst[i+1]
else:
    for i in range(0,len(negativelst)-1,2):
        result+=negativelst[i]*negativelst[i+1]
    result+=negativelst[-1]

print(result)
    

    
    
    

