N = int(input())

    
for i in range(N):
    for _ in range(i):
        print(' ', end = '')
    for _ in range(N-i):
        print('*', end='')
    print()