# 11:22 -> 11:51
n = int(input())

is_plus = True

zegop = 0
num = 0
two_zinsu = []

while n != 0:
    if is_plus:
        two_zinsu.append(n % 2)
        n = n // 2
        is_plus = False
    else:
        two_zinsu.append(n % -2)
        n = n // -2
        is_plus = True
print(two_zinsu)
