#8911
#실버2

#구현문제

#지나간 영역을 모두 포함하는것을 어떻게 하지?? y좌표 최대- y좌표 최소 * x좌표 최대-x좌표 최소'

n=int(input())

for i in range(n):
    st=input()
    re=[[0,0]]
    cx,cy,d=0,0,'N'
    for i in range(len(st)):
        if st[i]=='F':
            if d=='N':
                cy+=1
            elif d=='S':
                cy-=1
            elif d=='E':
                cx+=1
            elif d=='W':
                cx-=1
        elif st[i]=='B':
            if d=='N':
                cy-=1
            elif d=='S':
                cy+=1
            elif d=='E':
                cx-=1
            elif d=='W':
                cx+=1
        elif st[i]=='L':
            if d=='N':
                d='W'
            elif d=='S':
                d='E'
            elif d=='E':
                d='N'
            elif d=='W':
                d='S'
        elif st[i]=='R':
            if d=='N':
                d='E'
            elif d=='S':
                d='W'
            elif d=='E':
                d='S'
            elif d=='W':
                d='N'
        re.append([cx,cy])

    re.sort(key=lambda x:x[0])
    xl=re[-1][0]-re[0][0]

    re.sort(key=lambda x:x[1])
    yl=re[-1][1]-re[0][1]

    print(xl*yl)
        
