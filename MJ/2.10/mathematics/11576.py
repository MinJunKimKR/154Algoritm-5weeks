# 3:25 -> 3:55
# 3:48 [Success]
A, B = map(int, input().split())
m = int(input())
a_arr = list(map(int, input().split()))
a_arr.reverse()

ten_zin = 0
for i in range(m):
    ten_zin += a_arr[i]*pow(A, i)
b_zin = []

while ten_zin >= B:
    b_zin.append(str(ten_zin % B))
    ten_zin = ten_zin // B
b_zin.append(str(ten_zin))
b_zin.reverse()

print(' '.join(b_zin))


# 10 2
# 2
# 1 0
