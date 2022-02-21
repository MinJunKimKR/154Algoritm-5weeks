#1062
#골드4
import itertools

n,k=map(int,input().split())
words=[0]*n #각 단어의 비트마스킹한 정수를 저장.
for i in range(n):
    temp=input()
    for x in temp: #ord의 반대는 chr
        words[i]|=(1<<(ord(x)-ord('a'))) #ord:문자를 인자로 받고 문자에 해당하는 유니코드 정수를 반환.
        print(words)

if k<5:
    print(0)
else:
    need=['a','c','i','t','n']
    candidate=['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    
    comb=list(itertools.combinations(candidate,k-5)) #필수글자 5개를 제외한 갯수를 뽑음.
    for c in comb:
        each=0
        res=0
        
        #각 조합에 대한 비트마스킹
        for n in need:
            each|=(1<<(ord(n)-ord('a'))) # |는 합집합(or)
        for i in c:
            each|=(1<<(ord(i)-ord('a')))
            
        #단어와 조합의 비교
        for j in words:
            if each&j==j: #&는 대응하는 두 비트가 모두 1일때 1 반환.
                res+=1
        
        if ans<res:
            ans=res
    print(ans)
