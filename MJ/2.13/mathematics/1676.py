# 4:38 -> 5:08
# 4:47 [Success]

N = int(input())

fact = 1

for i in range(1, N + 1):
    fact *= i

reverse_str_facto = list(str(fact))
reverse_str_facto.reverse()

cnt_zro = 0
for num in reverse_str_facto:
    if num == '0':
        cnt_zro += 1
    else:
        break
print(cnt_zro)
