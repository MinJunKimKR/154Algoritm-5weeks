N = int(input())

  
for i in range(1,N+1):
    for _ in range(N-i):
        print(' ', end = '')
    for j in range(i):
        print('*', end = '')
        if j < i :
            print(' ', end = '')
    print()
