#2023
#골드5

#브루트포스로 하기에는 너무 범위가 커..

n=int(input())

def is_prime_num(n):
    n=int(n)
    for i in range(2, int(int(n)**0.5)+1):
        if n%i==0:
            return 0
    return 1

#한자리수 소수 2,3,5,7
#2,3,5,7로 조합한다음 소수인지 판별하는 방식으로 진행.

sosu=['1','2','3','5','7','9']
result=['']
answer=[]


for i in range(n):
    le=len(result)
    for j in range(le): 
        for s in sosu:
            temp=result[j]+s
            if is_prime_num(temp)==True and len(temp)==n and temp[0]!='1' and temp[0]!='9':
                print(temp)
            elif is_prime_num(temp):
                result.append(temp)
            


    20
