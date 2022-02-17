N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = [0]*3

def check(x,y,num):
    tmp = arr[x][y]
    for i in range(x,x+num):
        for j in range(y,y+num):
            if tmp != arr[i][j]:
                tmp = -2
                break
    if tmp == -2:
        num = num//3
        check(x,y,num)
        check(x,y+num,num)
        check(x,y+num*2,num)
        check(x+num, y, num)
        check(x+num, y + num, num)
        check(x+num, y + num * 2, num)
        check(x + num*2, y, num)
        check(x + num*2, y + num, num)
        check(x + num*2, y + num * 2, num)
    elif tmp == -1:
        result[0]+=1
    elif tmp == 0:
        result[1]+=1
    else:
        result[2]+=1

check(0,0,N)
for i in range(3):
    print(result[i])





# def check(start_x,start_y,n):
#     temp = arr[start_x][start_y]
#     for i in range(n):
#         for j in range(n):
#             if temp != arr[start_x+i][start_y+j]:
#                 return False
#     return True
#
#
#
# def divide(start_x,start_y,n):
#     if check(start_x,start_y,n):
#         result[arr[start_x][start_y]+1]+=1
#     else:
#         for i in range(3):
#             for j in range(3):
#                 divide(start_x+i*n//3,start_y+j*n//3,n//3)
#     return

# divide(0,0,N)
# for i in range(3):
#     print(result[i])