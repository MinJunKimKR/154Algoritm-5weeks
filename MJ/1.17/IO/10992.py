N = int(input())

  
for i in range(1,N+1):
    if i == N :
        for _ in range((i*2)-1):
            print('*', end = '')
        break
    for _ in range(N-i):
        print(' ', end = '')
    if i==1:
        print('*', end = '')
        print()
        continue
    for j in range((i*2)-1):
        if j == 0 or j == (i*2)-2:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()

# 1-1
# 2-3
# 3-5
# 4-7
# 5-9