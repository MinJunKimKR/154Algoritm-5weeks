# 1:15 -> 1:45
# 1:35[Success]
A, P = map(int, input().split())
arr_num = [0]*1000000
arr_num[A] = 1


def get_num(num):
    arr_num = list(str(num))
    total = 0
    for i in arr_num:
        total += pow(int(i), P)
    return total


num = get_num(A)
while arr_num[num] < 3:
    arr_num[num] += 1
    num = get_num(num)

print(arr_num.count(1))
