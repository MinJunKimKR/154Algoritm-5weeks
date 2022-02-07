#그리디

#11047
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
prices,output = [],0
for _ in range(N):
    prices.append(int(input()))
N -= 1
while(K > 0):
    p = prices[N]
    if(K-p >= 0):
        output += (K//p)
        K %= p
    N-=1
print(output)


#2875
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
maxteam = min(n//2, m)
n -= 2*maxteam
m -= maxteam
k -= (n+m)
if(k>0):
    maxteam -= k//3
    k %= 3
if(k>0):
    maxteam -= 1
print(maxteam)

#10610
n = input()
if('0' not in n):
    print(-1)
else:
    if(sum([int(a) for a in n])%3 != 0):
        print(-1)
    else:
        print(''.join(sorted(n, key = lambda x : int(x) ,reverse = True)))


#1783
N,M = map(int,input().split())
if(M==1 or N==1):
    print(1)
elif(N==2):
    print(min(4,(M-1)//2 + 1))
elif(M<4):
    print(M)
elif(M<7):
    print(4)
else:
    print(M-2)


#1931
import sys
input = sys.stdin.readline
n = int(input())
table = []
for _ in range(n):
    table.append(input().split())
table.sort(key = lambda x : (int(x[1]), int(x[0])))
start,output = table[0],1
for time in table[1:]:
    if(int(time[0])>=int(start[1])):
        start = time
        output += 1
print(output)


#11399 10초컷했다 기분 째지네
n = int(input())
p = sorted(list(map(int,input().split())))
print(sum([time*(n-i) for i, time in enumerate(p)]))


#2873 와 이걸맞다니 ㅠㅠㅠㅠ 2시간동안 풀었다 ㅅ
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
if(R%2 == 1):
    for _ in range(R):
        input()
    output = ''
    for i in range(R):
        if(i%2 == 0):
            output += 'R'*(C-1)
        else:
            output += ('D' + 'L'*(C-1) + 'D')
elif(C%2 == 1):
    for _ in range(R):
        input()
    output = ''
    for i in range(C):
        if(i%2 == 0):
            output += 'D'*(R-1)
        else:
            output += ('R' + 'U'*(R-1) + 'R')
else:
    joys = []
    for _ in range(R):
        joys.append(list(map(int,input().split())))
    output = ''
    minjoy = [0,1,joys[0][1]]
    for i in range(R):
        for j in range(C):
            if((i+j)%2 == 1 and joys[i][j] <= minjoy[2]):
                minjoy = [i,j,joys[i][j]]
    x,y = minjoy[0],minjoy[1]
    #빼야하는 점 전행까지 위와 같은방법으로 해결한 뒤 빼야하는 점까지 이동
    for i in range(0,x-1,2):
        output += ('R'*(C-1) + ('D' + 'L'*(C-1) + 'D'))
    for j in range(0,y-1,2):
        output += ('DRUR')
    #4칸중 빼야하는점을 빼고 다음4칸으로 이동해준다.
    if(x%2 == 0):
        output += ('DRR')        
    else:
        output += ('RDR')
    #빼야하는 점 다음칸부터 끝까지 처리.
    for i in range(y,C-2,2):
        output += 'URDR'
    #끝에R은 없애야하므로
    output = output[:-1]
    #그 밑행들 처리!
    for i in range(x,R-2,2):
        output += ('D' + 'L'*(C-1) + 'D' + 'R'*(C-1))
print(output)


#1744 위에꺼보다오니까 이지하네. 1은 곱하는것보다 더해야한다는 생각!
import sys
input = sys.stdin.readline
n = int(input())
minus, plus, output = [],[],0
for _ in range(n):
    num = int(input())
    if(num > 0):
        plus.append(num)
    else:
        minus.append(num)
minus.sort()
plus.sort()
for i in range(0,len(minus)-1,2):
    output += minus[i]*minus[i+1]
#1은 더해야돼!!!!
for j in range(len(plus)-1,0,-2):
    if(plus[j-1] > 1):
        output += plus[j]*plus[j-1]
    else:
        output += (plus[j] + plus[j-1])
if(len(minus)%2 == 1):
    output += minus[-1]
if(len(plus)%2 == 1):
    output += plus[0]

print(output)



























