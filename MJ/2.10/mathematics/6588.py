# 4:53 -> 5:23
# 5:30 [Success]
eratos = [True] * 1000001
eratos[0], eratos[1] = False, False
half = int(1000001/2)
for i in range(2, half + 1):
    if eratos[i] == False:
        continue
    for j in range(i+i, 1000001, i):
        eratos[j] = False
while True:
    num = int(input())
    if num == 0:
        break
    half = int(num/2)
    return_str = ''
    for a in range(2, half+1):
        if eratos[a] == False:
            continue
        b = num-a
        if eratos[b] == False:
            continue
        else:
            return_str = f'{num} = {a} + {b}'
            break
    if return_str == '':
        print('Goldbach\'s conjecture is wrong.')
    else:
        print(return_str)
