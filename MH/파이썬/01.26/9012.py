#괄호

a = int(input())
for i in range(a):
    b = input()
    sum = 0
    for i in b:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    print(sum)
    if sum == 0:
        print('YES')
    elif sum > 0:
        #sum != 0하면 위에서 break해도 여기서 또 걸려서 NO가 한번 더 출력됨.
        print('NO')

