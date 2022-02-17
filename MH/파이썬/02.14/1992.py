n = int(input())
arr = [list(map(int,input())) for _ in range(n)]

#같은 묶음이면 print
#다르면 쪼개는데 쪼개는 위 아래에 괄호

def dnc(x,y,n):
    check = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != arr[i][j]:
                check = -1
                break
    if check == -1:
        print("(",end="")
        n = n//2
        dnc(x,y,n)
        dnc(x,y+n,n)
        dnc(x+n,y,n)
        dnc(x+n,y+n,n)
        print(")",end="")

    elif check == 1:
        print(1,end="")
    else:
        print(0,end="")

dnc(0,0,n)

# ans = ""
#
# def check(a,b,num2):
#     global ans
#     tmp = arr[a][b]
#     for i in range(num2):
#         for j in range(num2):
#             if tmp != arr[a+i][b+j]:
#                 ans+="("
#                 return False
#
#     return True
#
# def divide(x,y,num):
#     global ans
#     if check(x,y,num):
#         ans += str(arr[x][y])
#     else:
#         for i in range(2):
#             for j in range(2):
#                 divide(x+i*num//2,y+j*num//2,num//2)
#
# divide(0,0,n)
# print(ans)