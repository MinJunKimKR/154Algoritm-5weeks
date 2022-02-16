#16113
#실버2

N=int(input())

arr=input()

num=len(arr)//5
st=[]
for i in range(5):
    st.append(list(arr[:num]))
    arr=arr[num:]
    
check=0

temp=''
answer=''

for i in range(num):
    for j in range(5):
        temp+=st[j][i]
    
    if len(temp)==10:
        if temp=='#####.....':
            answer+='1'
            temp=''
    if temp=='.....':
            temp=''
    if temp=='#####' and i==num-1:
        answer+='1'
            
    
    if len(temp)==15:
        
        #print(temp)
        if temp=='######.#.######':
            #print(i,j)
            answer+='8'
        if temp=='#.#.##.#.######':
            answer+='3'
        if temp=='#.####.#.####.#':
            answer+='2'
        if temp=='###.##.#.##.###':
            answer+='4'
        if temp=='###.##.#.##.###':
            answer+='5'
        if temp=='######.#.##.###':
            answer+='6'
        if temp=='######...######':
            answer+='0'
        if temp=='###.##.#.######':
            answer+='9'
        if temp=='#....#....#####':
            answer+='7'
        
        temp=''
print(answer)
    
        
        
    
