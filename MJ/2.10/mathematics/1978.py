# 3:50 -> 4:20
# 4:08[Success]
N = int(input())
N_arr = list(map(int, input().split()))
max_num = max(N_arr)
eratos = [True]*(max_num+1)
eratos[0], eratos[1] = False, False
sosu_arr = []
cnt_num = 0
for i in range(2, max_num+1):
    if eratos[i] == False:
        continue
    sosu_arr.append(i)
    num = i
    i += num
    while i <= max_num:
        eratos[i] = False
        i += num

for n in N_arr:
    if eratos[n]:
        cnt_num += 1
print(cnt_num)
